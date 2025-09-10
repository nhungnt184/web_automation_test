import pdfplumber, re

def test_3_create_report(run_job, create_report):
	job_run_status = run_job
	report_file = create_report

	text = ""
	with pdfplumber.open(report_file) as pdf:
		for page in pdf.pages:
			text += page.extract_text() + "\n"

	job_run_status_successful = re.search(".*Status.*Successful.*", text)
	job_run_status_failed = re.search(".*Status.*Failed.*", text)
	job_run_status_stopped = re.search(".*Status.*Stopped.*", text)
	job_run_status_other = (not job_run_status_successful and not job_run_status_failed and not job_run_status_stopped)
	
	assert job_run_status == "finished" and job_run_status_successful \
		or job_run_status == "failed" and job_run_status_failed \
		or job_run_status == "stopped" and job_run_status_stopped \
		or job_run_status == "other" and job_run_status_other, "verify if the report correctly reflects the job run status"
