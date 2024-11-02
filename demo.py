from TorqueManager import Job

for i in range(10):
    job = Job()
    job.add_cmd('sleep', '5')
    job.add_cmd('ls')
    job.add_cmd('echo', f'{i}')
    job.run(dir_path = './DIR', file_name = f'FILE{i % 3}', wall_time = '24:00:00', job_name = f'JOB{i % 3}')

