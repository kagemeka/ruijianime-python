import os
import pandas as pd
from datetime import (
  datetime,
)
import boto3



def merge():
  cfd = os.path.dirname(
    __file__,
  )
  cfd = os.path.abspath(cfd)
  root = f'{cfd}/../'
  data_dir = f'{root}/data/'

  ls = os.listdir(
    f'{data_dir}/0/',
  )
  print(ls)
  dt = datetime.now()
  date = dt.date()
  for file in ls:
    df1 = pd.read_csv(
      f'{data_dir}/0/{file}',
    )
    df2 = pd.read_csv(
      f'{data_dir}/1/{file}',
    ) 
    df = pd.concat([df2, df1])
    path = f'{data_dir}/{file}'
      
    df.to_csv(
      path,
      index=False,
    )
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    bucket.Object(
      'ruijianime/comic/'
      f'{date}/{file}'
    ).upload_file(path)
    
    
    
  



if __name__ == '__main__':
  merge()
