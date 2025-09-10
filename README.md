# Web Automation Test Project

This project is an automated web testing suite built with **Python**, **Pytest**, and **Playwright**.  
It demonstrates login, job creation, job execution, and report generation workflows for a sample web application.  

---

## Requirements

- Python **3.9+**
- Git
- Browsers supported by Playwright (Chromium, Firefox, WebKit)

---

## Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/nhungnt184/web_automation_test
   cd web_automation_test
   ```

2. **Create and activate a virtual environment**  
   - Windows  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```  
   - Linux / MacOS  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**  
   ```bash
   playwright install
   ```

---

## Running Tests

- Run **all tests**:
  ```bash
  pytest
  ```

- Run a **specific test file**:
  ```bash
  pytest tests/test_1_create_job.py
  ```

- Run a **single test function**:
  ```bash
  pytest tests/test_1_create_job.py::test_1_create_job
  ```

---

## Test Reports

To generate an **HTML test report**:

Just open `test_report.html`, which is automatically generated, in your browser to view results.

---

## Project Structure

```
web_automation_test/
│
├── pages/                 # Page Object classes (Login, Main, Job Editor)
│   ├── page_login.py
│   ├── page_main.py
│   ├── page_job_editor.py
│   └── __init__.py
│
├── tests/                 # Test cases and data
│   ├── data/
│   │   └── test_data.csv
│   ├── test_1_create_job.py
│   ├── test_2_run_job.py
│   ├── test_3_create_report.py
│   └── __init__.py
│
├── conftest.py            # Pytest fixtures
├── common.py              # Shared helper functions
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Python dependencies
└── test_report.html       # Example test report
```

---

## Notes

- The project uses the **Page Object Model (POM)** for better maintainability.  
- Fixtures in `conftest.py` manage browser sessions, login, and job setup.  
- Test data is stored in `tests/data/test_data.csv`. 
- For the test 3, report files are stored in the 'downloads' folder under the project root instead of being stored in the default downloads folder.