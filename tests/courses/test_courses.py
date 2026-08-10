import allure
import pytest
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage, CourseParams
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
            courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
            courses_list_page.sidebar.check_visible()
            courses_list_page.navbar.check_visible("username")
            courses_list_page.toolbar_view.check_visible()
            courses_list_page.check_visible_empty_view()


    @pytest.mark.parametrize(
        "params",
        [
            CourseParams(
                index=0,
                title="Playwright",
                max_score="10",
                min_score="2",
                estimated_time="1h20m"
            )
        ]
    )
    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage, params: CourseParams):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.image_upload_widget.upload_preview_image('testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.check_visible("", "", "", "0", "0")
        create_course_page.create_course_form.fill(
            title=params.title,
            estimated_time=params.estimated_time,
            description="Some description",
            max_score=params.max_score,
            min_score=params.min_score
        )
        create_course_page.exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.exercises_toolbar.click_create_exercise_button()
        create_course_page.course_toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_course_card(params)

    @pytest.mark.parametrize(
        "initial_params, edited_params",
        [
            (
                    CourseParams(
                        index=0,
                        title="Testing",
                        max_score="15",
                        min_score="5",
                        estimated_time="2h10m"
                    ),
                    CourseParams(
                        index=0,
                        title="Edited title",
                        max_score="20",
                        min_score="10",
                        estimated_time="3h"
                    )
            )
        ]
    )
    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage, initial_params: CourseParams,
    edited_params: CourseParams):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.image_upload_widget.upload_preview_image('testdata/files/image2.png')
        create_course_page.create_course_form.fill(
            title=initial_params.title,
            estimated_time=initial_params.estimated_time,
            description="Some description",
            max_score=initial_params.max_score,
            min_score=initial_params.min_score
        )
        create_course_page.course_toolbar.click_create_course_button()
        courses_list_page.check_visible_course_card(initial_params)
        courses_list_page.course_view.menu.click_edit(index=initial_params.index)
        create_course_page.create_course_form.fill(
            title=edited_params.title,
            estimated_time=edited_params.estimated_time,
            description="Edited description",
            max_score=edited_params.max_score,
            min_score=edited_params.min_score
        )
        create_course_page.course_toolbar.click_create_course_button()
        courses_list_page.check_visible_course_card(edited_params)


