from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_have_text("Dashboard")

    context.storage_state(path='course-state.json')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='course-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    no_results_block = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text('There is no results')

    courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    no_results_info = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(no_results_info).to_be_visible()
    expect(no_results_info).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)