def test_1_create_job(create_job):
	job_name, job_created_successfully = create_job
	assert job_created_successfully == True, f"tried to create job {job_name}; job_created_successfully True means job creation is successful, and vice versa"