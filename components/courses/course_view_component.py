from dataclasses import dataclass

import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.image import Image
from elements.text import Text


@dataclass
class CourseParams:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'course-widget-title-text', 'Title')
        self.preview_image = Image(page, 'course-preview-image', 'Image')
        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text = Text(page,'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'Estimated time')
        self.menu = CourseViewMenuComponent(page)

    @allure.step('Check visible course view at index "{params.index}"')
    def check_visible(self, params : CourseParams):
        self.preview_image.check_visible(nth=params.index)

        self.title.check_visible(nth=params.index)
        self.title.check_has_text(params.title, nth=params.index)

        self.max_score_text.check_visible(nth=params.index)
        self.max_score_text.check_has_text(f"Max score: {params.max_score}", nth=params.index)

        self.min_score_text.check_visible(nth=params.index)
        self.min_score_text.check_has_text(f"Min score: {params.min_score}", nth=params.index)

        self.estimated_time_text.check_visible(nth=params.index)
        self.estimated_time_text.check_has_text(f"Estimated time: {params.estimated_time}", nth=params.index)


