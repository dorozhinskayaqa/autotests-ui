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
- Reusable page components and UI elements
- Pytest fixtures
- Test parametrization
- Positive and negative UI scenarios
- Cross-browser testing
- Parallel test execution with pytest-xdist
- Browser state management
- Test data handling
- Environment-based configuration
- Dependency management with `requirements.txt`
- Allure reporting
- Screenshots, tracing and video recording
- Environment information in Allure reports
- Static resource blocking using Playwright routing to optimize test execution
- Structured logging for UI interactions and assertions

## Project Structure

- `tests/` — automated test scenarios
- `pages/` — Page Object classes
- `components/` — reusable page components
- `elements/` — reusable UI element abstractions
- `fixtures/` — reusable Pytest fixtures
- `testdata/` — test data and files
- `tools/` — helper utilities
- `config.py` — project configuration and environment settings
- `requirements.txt` — project dependencies
- `.env.example` — environment configuration template

## Installation

Clone the repository and navigate to the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Configuration

The project uses environment variables for configuration.

Create a local `.env` file based on `.env.example` and configure the required values.

The `.env` file is used for local configuration and is not committed to the repository.

## Running Tests

Run the full test suite:

```bash
python -m pytest
```

Run tests by marker:

```bash
python -m pytest -m "smoke"
```

Run regression tests:

```bash
python -m pytest -m "regression"
```

Run regression tests in parallel using 5 workers:

```bash
python -m pytest -m "regression" --numprocesses=5 --dist=loadgroup
```

Run a specific test module:

```bash
python -m pytest tests/test_example.py
```

Run a specific test:

```bash
python -m pytest tests/test_example.py::test_name
```

Tests can also be filtered by name using the `-k` option:

```bash
python -m pytest -k "test_name"
```

## Reports

The project uses Allure for test reporting.

Test execution artifacts such as screenshots, Playwright traces, and video recordings are collected to help investigate test failures.

Allure reports also include environment information, such as test configuration, operating system details, and Python version.