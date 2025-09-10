# WEB AUTOMATION TEST PROJECT

[cite_start]This project is an automated web testing suite using Python, Pytest, and Playwright[cite: 1].

## REQUIREMENTS

- [cite_start]Python 3.9 or higher [cite: 2]
- [cite_start]Git [cite: 2]
- [cite_start]Playwright supported browsers (Chromium, Firefox, WebKit) [cite: 2]

## SETUP

1. Clone the repository:
   `git clone https://github.com/nhungnt184/web_automation_test`
   [cite_start]`cd web_automation_test` [cite: 2]

2. Create a virtual environment:
   [cite_start]`python -m venv venv` [cite: 2]

3. Activate the virtual environment:
   - [cite_start]Windows: `venv\Scripts\activate` [cite: 2]
   - [cite_start]Linux/Mac: `source venv/bin/activate` [cite: 2]

4. Install dependencies:
   [cite_start]`pip install -r requirements.txt` [cite: 2]

5. Install Playwright browsers:
   [cite_start]`playwright install` [cite: 2]

## RUNNING TESTS

- Run all tests:
  [cite_start]`pytest` [cite: 2]

- Run a specific test file:
  [cite_start]`pytest tests/test_1_create_job.py` [cite: 2]

- Run a single test function:
  [cite_start]`pytest tests/test_1_create_job.py::test_1_create_job` [cite: 2]

## TEST REPORT

[cite_start]Test report named "test_report.html" is automatically generated in the project root[cite: 2].

## PROJECT STRUCTURE

web_automation_test/
  pages/        -> Page Object classes
  tests/        -> Test scripts and test data
  conftest.py   -> Pytest fixtures
  common.py     -> Shared helper functions
  pytest.ini    -> Pytest configuration
  requirements.txt -> Dependencies
  test_report.html -> Example test report