from playwright.sync_api import Page

class PageMain:
	def __init__(self, page: Page):
		self.page = page
		self.url = "https://13.251.147.160:4443/c/main"
		self.create_job_button = "div.create-btn.simple-link"
		self.backup_link_text = "text=Backup for Amazon EC2"
		self.job_table = "table.x-grid-table tbody tr.x-grid-row"
		self.run_button = "div.sllMain.jvabButton[title='Run']"		
		self.popup_run_option2 = "xpath=//label[text()='Run for selected instances']"
		self.popup_run_button = "xpath=//button[span[text()='Run']]" 
		self.event_table = "table.x-grid-table"	
		self.stop_button = "div.sllMain.jvabButton[title='Stop']"
		self.popup_stop_button = "//button[.//span[normalize-space(.)='Stop']]"
		self.manage_button = "div[title='Manage']"
		self.create_report_menu_item = "div.title-report:has-text('Create Report')"
		self.last_run_report = "//a[normalize-space(.)='Last run report']"
		self.create_report_button = "//button[.//span[normalize-space(.)='Create']]"

	def click_create_job_button(self):
		self.page.locator(self.create_job_button).click()

	def click_backup_link_text(self):
		self.page.locator(self.backup_link_text).click()

	def wait_job(self, job_name):
		return self.page.locator(self.job_table).locator(f"text={job_name}").wait_for()
	
	def check_job(self, job_name):
		return self.page.locator(self.job_table).locator(f"text={job_name}").count()
	
	def click_job(self, job_name):
		self.page.locator(self.job_table).locator(f"text={job_name}").click()	
		
	def click_run_button(self):
		self.page.locator(self.run_button).click()
		
	def click_stop_button(self):
		self.page.locator(self.run_button).click()		
		
	def click_popup_run_option2(self):
		self.page.locator(self.popup_run_option2).click()

	def click_popup_checkbox(self, instance):
		popup_checkbox = f"xpath=//label[contains(text(),'{instance}')]"
		self.page.locator(popup_checkbox).click()
	
	def click_popup_run_button(self):
		self.page.locator(self.popup_run_button).click()

	def click_manage_button(self):
		self.page.locator(self.manage_button).click()

	def click_create_report_menu_item(self):
		self.page.locator(self.create_report_menu_item).click()

	def click_last_run_report_menu_item(self):
		self.page.locator(self.last_run_report).click()

	def click_create_report_button(self):
		self.page.locator(self.create_report_button).click()

	def get_job_run_status(self):
		table = self.page.locator(self.event_table)
		if table.filter(has_text="The job has finished").count() > 0:
			return "finished"
		elif table.filter(has_text="The job has failed").count() > 0:			
			return "failed"
		elif table.filter(has_text="The job was stopped").count() > 0:
			return "stopped"
		elif table.filter(has_text="Job action has failed").count() > 0:			
			return "temp_failed"
		else:
			return "other"
	
	def go_to_job_editor(self):
		self.page.goto(self.url)
		self.page.wait_for_url("**/c/main**")
		
		self.click_create_job_button()
		self.click_backup_link_text()
		self.page.wait_for_url("**/c/jobEditor**")

	def run_job(self, instance, job_name = None):
		if job_name:
			self.click_job(job_name)
		self.click_run_button()
		self.click_popup_run_option2()
		self.click_popup_checkbox(instance)
		self.click_popup_run_button()

	def stop_job(self):
		self.page.locator(self.stop_button).click()
		self.page.locator(self.popup_stop_button).click()

	def create_report(self):
		self.click_manage_button()
		self.click_create_report_menu_item()
		self.click_last_run_report_menu_item()
		self.click_create_report_button()			