import pdfplumber, re

def test_3_create_report(create_report):
	report_file = create_report

	text = ""
	with pdfplumber.open(report_file) as pdf:
		for page in pdf.pages:
			text += page.extract_text() + "\n"

	assert re.search(".*Status.*Successful.*", text)
