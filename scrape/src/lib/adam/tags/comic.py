import typing 
import pandas as pd
import datetime  
from lib.ruijianime.scrape.tags import (
  scrape_comic_tags,
  scrape_anime_tags,
)
from lib.aws_util.s3.upload import upload_to_s3




def update_all_comic_tags() -> typing.NoReturn:
  tags = scrape_comic_tags()
  df = pd.DataFrame(tags)
  print(df)
  __store_to_s3(df)



def __store_to_s3(df: pd.DataFrame) -> typing.NoReturn:
  bucket = 'av-adam-store'
  save_path = '/tmp/comic_taglist.csv'
  upload_obj = 'ruijianime/comic/comic_taglist.csv'
  
  dt = datetime.datetime.now()
  df['updated_at'] = dt.date()
  df.to_csv(save_path, index=False)
  upload_to_s3(bucket, upload_obj, save_path)
  
  