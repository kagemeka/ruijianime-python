import typing
import boto3
from datetime import (
  datetime,
)
from .filter_comic_ids import (
  FilterComicIds,
)
from .make_df.comics import (
  MakeComicsDF,
)



class Adam():
  def __call__(
    self,
  ) -> typing.NoReturn:
    self.__make_df()
    self.__add_timestamp()
    self.__store()
    self.__upload()

  
  def __init__(
    self,
  ) -> typing.NoReturn:
    dt = datetime.now()
    self.__dt = dt
    date = dt.date()
    self.__save_dir = (
      '/tmp/'
    )
    self.__upload_dir = (
      'ruijianime/comic/'
      f'{date}/'
    )


  def __make_df(
    self,
  ) -> typing.NoReturn:
    f = MakeComicsDF()
    self.__df = f()
  
  
  def __add_timestamp(
    self,
  ) -> typing.NoReturn:
    df = self.__df
    dt = self.__dt
    df.meta['datetime'] = dt
    df.tag['datetime'] = dt
    df.author['datetime'] = dt
    self.__df = df
  
  
  def __store(
    self,
  ) -> typing.NoReturn:
    d = self.__save_dir
    df = self.__df
    meta_path = (
      f'{d}ruijimanga_meta.csv'
    )
    df.meta.to_csv(
      meta_path, 
      index=False,
    )
    tag_path = (
      f'{d}ruijimanga_tag.csv'
    )
    df.tag.to_csv(
      tag_path,
      index=False,
    )
    author_path = (
      f'{d}ruijimanga_author.csv'
    )
    df.author.to_csv(
      author_path,
      index=False,
    )
    (
      self.__meta_path,
      self.__tag_path,
      self.__author_path,
    ) = (
      meta_path,
      tag_path,
      author_path,
    )


  def __upload(
    self,
  ) -> typing.NoReturn:
    (
      meta_path,
      tag_path,
      author_path,
    ) = (
      self.__meta_path,
      self.__tag_path,
      self.__author_path,
    )
    d = self.__upload_dir
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    bucket.Object(
      f'{d}ruijimanga_meta.csv',
    ).upload_file(
      meta_path,
    )
    bucket.Object(
      f'{d}ruijimanga_tag.csv',
    ).upload_file(
      tag_path,
    )
    bucket.Object(
      f'{d}ruijimanga_author.csv',
    ).upload_file(
      author_path,
    )
  