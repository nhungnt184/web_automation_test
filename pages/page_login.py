from playwright.sync_api import Page

class PageLogin:
	def __init__(self, page: Page):
		self.page = page
		self.url = "https://13.251.147.160:4443/c/login"
		self.username = "input[name='username']"
		self.password = "input[type='password']"
		self.login_button = "[title='Log In']"

	def enter_username(self, username: str):
		self.page.locator(self.username).fill(username)

	def enter_password(self, password: str):
		self.page.locator(self.password).fill(password)

	def click_login(self):
		self.page.locator(self.login_button).click()

	def login(self, username: str, password: str):
		self.page.goto(self.url)
		self.enter_username(username)
		self.enter_password(password)
		self.click_login()
		
		self.page.wait_for_url("**/c/overview**")