# TORQUE Manager
+ Python から TORQUE にジョブを submit する
  + .sh ファイルを陽に介さない

## 依存ライブラリ
+ Numpy
+ Pandas

## 使用方法
`TorqueManager.py` を作業ディレクトリに置いておく. 

```python
from TorqueManager import Job

# 新しいジョブの作成
job = Job()

# コマンドの追加
job.add_cmd('echo', '998244353')

# ジョブの submit
job.run()

"""
次のオプションがある
+ dir_path : .sh ファイルを生成するディレクトリ
+ file_name: .sh ファイル名
+ wall_time: ジョブの最大実行時間
+ job_name : ジョブの名前

job.run(dir_path = './DIR', file_name = f'FILE', wall_time = '24:00:00', job_name = f'JOB')
"""
```

```python
from TorqueManager import jobs_stat
jobs_stat() # ジョブの統計を出力する
```

