class Job:
    def __init__(self):
        self.cmds = []
        self.cmds += ['#!/bin/sh' + '\n']
        self.cmds += ['cd $PBS_O_WORKDIR' + '\n']

    def add_cmd(self, *cmd):
        self.cmds.append(' '.join(cmd) + '\n')

    def run(self, dir_path = '.', file_name = 'TorqueManager', **kwargs):
        import os
        os.makedirs(dir_path, exist_ok = True)

        file_path = dir_path + '/' + file_name + '.sh'
        with open(file_path, mode = 'w') as f:
            for cmd in self.cmds:
                f.write(cmd)
        os.chmod(file_path, 0o777)

        cmd = ['qsub']
        if 'wall_time' in kwargs:
            cmd += ['-l', 'walltime=' + kwargs['wall_time']]
        if 'job_name' in kwargs:
            assert len(kwargs['job_name']) <= 16
            cmd += ['-N', kwargs['job_name']]
        cmd += [file_path]

        import subprocess
        subprocess.run(cmd)


def jobs_stat():
    import os
    import subprocess
    qstat_str = subprocess.run(['qstat'], capture_output = True, text = True, cwd = os.path.dirname(__file__)).stdout

    if qstat_str:
        qstat = qstat_str.split('\n')
        data = []
        for i in range(2, len(qstat)):
            if qstat[i]:
                data.append(qstat[i].split())
        import pandas as pd
        df = pd.DataFrame(data = data, columns = ['Job ID', 'Name', 'User', 'Time Use', 'S', 'Queue'])
        print(pd.crosstab([df['User'], df['Name']], df['S']))
    else:
        print("NO JOBS")
