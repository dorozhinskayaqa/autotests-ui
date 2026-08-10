import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar_title = Text(page,'create-course-exercises-box-toolbar-title-text', 'Title')
        self.toolbar_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Button')

    @allure.step("Check visible create course exercises toolbar")
    def check_visible(self):
        self.toolbar_title.check_visible()
        self.toolbar_title.check_has_text('Exercises')

        self.toolbar_button.check_visible()

    def click_create_exercise_button(self):
        self.toolbar_button.click()
        