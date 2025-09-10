def test_2_run_job(run_job):
	job_run_status = run_job
	assert job_run_status == "finished", "tried to run the job created; job_run_status 'finished' means job run is successful, and vice versa"