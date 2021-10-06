import typing
import datetime
import pandas as pd
from .make_df import ComicDataFrame
from lib.aws_util.s3.upload import upload_to_s3
from lib.aws_util.s3.download import download_from_s3



def store(df: ComicDataFrame) -> typing.NoReturn:
  dt = datetime.datetime.now()
  bucket = 'av-adam-store'
  save_dir = '/tmp/'
  upload_dir = f'ruijianime/comic/'
  meta_path = f'{save_dir}meta.csv'
  meta_obj = f'{upload_dir}meta.csv'
  tag_path = f'{save_dir}tag.csv'
  tag_obj = f'{upload_dir}tag.csv'
  author_path = f'{save_dir}author.csv'
  author_obj = f'{upload_dir}author.csv'


  def add_timestamp() -> typing.NoReturn:
    df.meta['updated_at'] = dt
    df.tag['updated_at'] = dt
    df.author['updated_at'] = dt

  def download() -> typing.NoReturn:
    download_from_s3(bucket, meta_obj, meta_path)
    download_from_s3(bucket, tag_obj, tag_path)
    download_from_s3(bucket, author_obj, author_path)

  def merge() -> typing.NoReturn:
    meta_old = pd.read_csv(meta_path)
    meta = pd.concat((meta_old, df.meta), ignore_index=True)
    meta.drop_duplicates(
      subset=['comic_id'], 
      keep='last',
      inplace=True,
    )
    print(meta)
    meta.to_csv(meta_path, index=False)

    tag_old = pd.read_csv(tag_path)
    tag = pd.concat((tag_old, df.tag), ignore_index=True)
    tag.drop_duplicates(
      subset=['comic_id', 'tag_id'], 
      keep='last',
      inplace=True,
    )
    print(tag)
    tag.to_csv(tag_path, index=False)

    author_old = pd.read_csv(author_path)
    author = pd.concat(
      (author_old, df.author), 
      ignore_index=True,
    )
    author.drop_duplicates(
      subset=['comic_id', 'author'], 
      keep='last',
      inplace=True,
    )
    print(author)
    author.to_csv(author_path, index=False)


  def upload() -> typing.NoReturn:
    upload_to_s3(bucket, meta_obj, meta_path)
    upload_to_s3(bucket, tag_obj, tag_path)
    upload_to_s3(bucket, author_obj, author_path)

  add_timestamp()
  download()
  merge()
  upload()
  
