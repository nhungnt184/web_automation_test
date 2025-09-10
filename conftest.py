import pytest, time, os
from playwright.sync_api import sync_playwright
from pathlib import Path
from pages.page_login import PageLogin
from pages.page_main import PageMain
from pages.page_job_editor import PageJobEditor

USERNAME = "admin"
PASSWORD = "123456"
INSTANCE = "i-0b9631eceffa6646f"
TIMEOUT = 60000 # millisecond
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(PROJECT_ROOT, "tests", "data", "test_data.csv")
DOWNLOAD_DIR = Path(__file__).parent / "downloads"
REPORT_FILE_NAME_PATTERN = "job_report_*.pdf"

@pytest.fixture(scope="session")
def browser_page():
	with sync_playwright() as p:
		browser = p.chromium.launch(headless=False, slow_mo=500)
		context = browser.new_context(ignore_https_errors=True)
		page = context.new_page()
		page.set_viewport_size({"width": 1920, "height": 1080})
		page.set_default_timeout(TIMEOUT)
		yield page
		browser.close()

@pytest.fixture(scope="session")
def login(browser_page):
	page = browser_page
	login_page = PageLogin(page)
	login_page.login(USERNAME, PASSWORD)
	yield page

@pytest.fixture(scope="session")
def create_job(login):
	page = login
	main_page = PageMain(page)
	main_page.go_to_job_editor()
	
	job_editor = PageJobEditor(page)
	job_editor.job_editor_step1(INSTANCE)
	job_editor.job_editor_step2()
	job_editor.job_editor_step3()
	job_editor.job_editor_step4(DATA_FILE)
	
	job_name = job_editor.get_job_name()
	job_editor.click_finish_button()
	job_created_successful = 0
	try:
		main_page.wait_job(job_name)
		job_created_successful = 1
	except TimeoutError:
		job_created_successful = 0

	yield job_name, job_created_successful
	
@pytest.fixture(scope="session")
def run_job(login):
	page = login	
	main_page = PageMain(page)
	main_page.run_job(INSTANCE)
	while 1:
		time.sleep(1)
		job_run_status = main_page.get_job_run_status()
		if job_run_status == -1:
			main_page.stop_job()
			main_page.page.locator(main_page.run_button).wait_for()
			break
		elif job_run_status == 1:
			break
	
	yield main_page.get_job_run_status()

@pytest.fixture(scope="session")
def create_report(login):
	page = login
	main_page = PageMain(page)

	for f in DOWNLOAD_DIR.glob("job_report_*.pdf"):
		f.unlink()

	# main_page.create_report()
	with page.expect_download() as download_info:
		main_page.create_report()

	download = download_info.value
	save_path = DOWNLOAD_DIR / download.suggested_filename
	download.save_as(save_path)

	yield save_path