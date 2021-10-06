import typing 
import pandas as pd
from lib.aws_util.s3.csv.read import read_csv_on_s3
from lib.ruijianime.scrape import (
  scrape_all_comic_ids, 
  scrape_comics,
)
from .make_df import MakeComicDataFrame
from .store_to_s3 import store
import logging



def _fetch_scraped_ids() -> typing.List[int]:
  df = read_csv_on_s3(
    'av-adam-store', 
    'ruijianime/comic/meta.csv',
  )
  return list(df.comic_id.values)


def add_new_comics() -> typing.NoReturn:
  comic_ids = scrape_all_comic_ids()
  comic_ids = list(set(comic_ids) - set(_fetch_scraped_ids()))
  comics = scrape_comics(comic_ids)
  df = MakeComicDataFrame().from_comics(comics)
  logging.info('scraped new comics.')  
  print(df)
  if df is None: return
  store(df)
  logging.info('new comics have been stored on S3')  
