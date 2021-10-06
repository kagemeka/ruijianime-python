import typing 
from lib.aws_util.s3.csv.read import read_csv_on_s3
from lib.ruijianime.scrape import scrape_comics
from .make_df import MakeComicDataFrame
from .store_to_s3 import store
import logging


def _fetch_old_ids() -> typing.List[int]:
  df = read_csv_on_s3(
    'av-adam-store', 
    'ruijianime/comic/meta.csv',
  )
  df.sort_values(by=['updated_at'], inplace=True)
  return list(df.iloc[:100].comic_id.values)


def update_comics() -> typing.NoReturn:
  comic_ids = _fetch_old_ids()
  comics = scrape_comics(comic_ids)
  df = MakeComicDataFrame().from_comics(comics)
  logging.info('scraped new comics.')  
  print(df)
  if df is None: return
  store(df)
  logging.info('new comics have been stored on S3')  
