def test_1_create_job(create_job):
	job_name, job_created_successfully = create_job
	assert job_created_successfully == 1
	if job_created_successfully == 1:
		print(f"job created successfully: {job_name}")
	else:
		print("fail to create job")