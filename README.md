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

job.run(dir_path = './DIR', file_name = 'FILE', wall_time = '24:00:00', job_name = 'JOB')
"""
```

```python
from TorqueManager import jobs_stat
jobs_stat() # ジョブの統計を出力する
```

## 使用例
ファイル `PROGRAM.py` に記述された関数 `FUNC()` の引数を様々に変化させて実行したいとする. 
```python
import click
@click.command()
@click.option('-a')
@click.option('-b')
def FUNC(a, b):
  print(f'a = {a}, b = {b}')

if __name__ == '__main__': FUNC()
```
click などでコマンドから実行できるようにしておく.
次のようにできる. 

```python
from TorqueManager import Job
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        job = Job()
        job.add_cmd('python', 'PROGRAM.py', '-a', f'{a}', '-b', f'{b}')
        job.run()
```


