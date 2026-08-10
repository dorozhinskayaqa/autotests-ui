import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar_title = Text(page, 'create-course-toolbar-title-text', 'Toolbar title')
        self.toolbar_button = Button(page, 'create-course-toolbar-create-course-button', 'Create course button')

    @allure.step("Check visible create course toolbar")
    def check_visible(self, is_create_course_disabled: bool=True):
        self.toolbar_title.check_visible()
        self.toolbar_title.check_has_text('Create course')

        if is_create_course_disabled:
            self.toolbar_button.check_disabled()

        if not is_create_course_disabled:
            self.toolbar_button.check_enabled()

    def click_create_course_button(self):
        self.toolbar_button.click()