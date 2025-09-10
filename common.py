import csv
import random
# from playwright.sync_api import sync_playwright

LOCATOR_MAP = {
	"id": lambda locator: f"#{locator}",
	"name": lambda locator: f"[name='{locator}']",
	"class_name": lambda locator: f".{locator}",
	"css_selector": lambda locator: locator,
	"xpath": lambda locator: f"xpath={locator}",
	"tag_name": lambda locator: locator,
	"link_text": lambda locator: f"text={locator}",
	"partial_link_text": lambda locator: f"text={locator}",
}

MAIN_LISTBOX_LOCATOR = "div.list-ct"

def select_from_list(page, list_container_id, value_to_select): 
	page.locator(f"#{list_container_id}").click()
	item = page.locator(f"#{list_container_id} li[role='option'] div[title='{value_to_select}']")	
	item.wait_for(state="visible")	
	item.click()

def control_element(page, control_type, locator_type, locator, locator_ext, value):
	selector = LOCATOR_MAP[locator_type.lower()](locator)
	element = page.locator(selector)

	if not element.is_visible() or not element.is_enabled():
		print(f"element with locator {locator} not displayed")
		return

	readonly = element.get_attribute("readonly")
	if readonly:
		print(f"element with locator {locator} readonly")
		return

	if control_type.lower() == "textbox":
		element.fill("")
		if value not in ["", "none", "empty"]:
			element.fill(value)

	elif control_type.lower() == "checkbox":
		if value.lower() in ["true", "checked", "yes"]:
			element.check()
		elif value.lower() in ["false", "unchecked", "no"]:
			element.uncheck()

	elif control_type.lower() == "listbox":
		element.click()
		if MAIN_LISTBOX_LOCATOR in locator_ext:
			dropdown = page.locator(MAIN_LISTBOX_LOCATOR).last
			sub_locator = locator_ext[len(MAIN_LISTBOX_LOCATOR):]
			dropdown.locator(sub_locator, has_text=f'{value}').click()
		else:
			print(f"locator {locator} not supported")
			return

	elif control_type.lower() == "button":
		element.click()

	else:
		print(f"control type '{control_type}' not supported.")

def control_elements(page, data_file):
	with open(data_file, newline = "", encoding = "utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			control_type = row["control_type"].strip()
			locator_type = row["locator_type"].strip()
			locator = row["locator"].strip()
			locator_ext = row["locator_ext"].strip()
			value = row["value"].strip()
			if "6d" in value:
				random_6_digits = "".join([str(random.randint(0, 9)) for _ in range(6)])
				value = value.replace("6d", random_6_digits)

			control_element(page, control_type, locator_type, locator, locator_ext, value)