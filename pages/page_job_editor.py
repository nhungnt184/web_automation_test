import os
import common
from playwright.sync_api import Page

class PageJobEditor:
	def __init__(self, page: Page):
		self.page = page
		
		# step 1
		self.search_textbox = "input[placeholder='Search']"
		self.source_checkbox = "xpath=//table/tbody/tr[4]//input[@class='x-tree-checkbox']"
		self.next_button = "xpath=//div[@title='Next']"

		# step 2
		self.onboard_label = "xpath=//div[text()='Onboard repository']"

		# step 3
		self.unschedule_checkbox = "#ext-gen1080"
		self.next_button = "xpath=//div[@title='Next']"

		# step 4
		self.job_name = "#ext-gen1133"
		self.finish_button = "xpath=//div[@title='Finish']"

	# step 1
	def enter_search_key(self, key: str):
		textbox = self.page.locator(self.search_textbox)
		textbox.fill(key)
		textbox.press("Enter")

	def click_source_checkbox(self):
		self.page.locator(self.source_checkbox).click(force=True)

	# step 3
	def click_unschedule_checkbox(self):
		self.page.locator(self.unschedule_checkbox).click(force=True)

	def click_next_button(self):
		self.page.locator(self.next_button).click(force=True)

	# step 4
	def fill_up_form(self, data_file):
		common.control_elements(self.page, data_file)

	def get_job_name(self):
		return self.page.locator(self.job_name).input_value()
	
	def click_finish_button(self):
		self.page.locator(self.finish_button).click(force=True)	   

	# common
	def click_next_button(self):
		self.page.locator(self.next_button).click(force=True)

	# step 1
	def job_editor_step1(self, instance: str):
		self.enter_search_key(instance)
		self.click_source_checkbox()
		self.click_next_button()
		self.page.locator(self.onboard_label).wait_for()

	# step 2
	def job_editor_step2(self):	
		self.click_next_button()

	# step 3
	def job_editor_step3(self):		
		self.click_unschedule_checkbox()
		self.click_next_button()
		self.page.locator(self.finish_button).wait_for()
			
	# step 4
	def job_editor_step4(self, data_file):
		self.fill_up_form(data_file)