# UI Test Automation Project

UI test automation project developed as part of my QA Automation training.

The repository is currently a work in progress and is continuously updated as I learn and implement new testing approaches.

## Tech Stack

- Python
- Pytest
- Playwright
- Allure
- Pydantic / Pydantic Settings

## Implemented

- Page Object Model
- Pytest fixtures
- Test parametrization
- Positive and negative UI scenarios
- Browser state management
- Test data handling
- Allure reporting
- Screenshots, tracing and video recording

## Project Structure

- `tests/` — automated test scenarios
- `pages/` — Page Object classes
- `fixtures/` — reusable Pytest fixtures
- `testdata/` — test data and files
- `tools/` — helper utilities

## Configuration

The project uses environment variables for configuration.

Create a local `.env` file based on `.env.example`.

The `.env` file is used for local configuration and is not committed to the repository.

## Running Tests

Run the full test suite:

```bash
pytest
```

Individual tests, test modules, or groups of tests can also be executed separately using standard Pytest options and markers.

## Reports 

The project uses Allure for test reporting.

Test execution artifacts such as screenshots, traces, and video recordings are collected to help investigate failed tests.

## Installation

Install the required Python packages:

```bash
pip install pytest playwright allure-pytest pydantic pydantic-settings