import time
from datetime import datetime
import numpy as np
import requests
import pandas as pd
import re
from pprint import (
  pprint,
)


import bs4
import dataclasses
import typing



from \
  lib.ruijianime \
  .scrape.comic \
import (
  Comic,
)

from \
  lib.ruijianime \
  .scrape.comics \
import (
  ScrapeComics,
)



'''TODO
Adam
'''

from \
  lib.adam.filter_comic_ids \
import (
  FilterComicIds,
)




@dataclasses.dataclass
class Metadata():
  title: str
  start_year: int
  authors: typing.List[str]
  magazine: typing.Optional[
    str
  ]
  publishers: typing.List[str]
  anime_id: typing.Optional[
    int
  ]
  overview: str


@dataclasses.dataclass
class Tag():
  name: str 
  tag_id: int
  featured: bool = False
  ratio: typing.Optional[
    float
  ] = None


'''schema
metadata
 comic_id
 title
 start_year
 magazine: Optional
 anime_id: Optional
 overview

tags
  comic_id
  tag_id
  name
  featured: 1/0
  ratio: Optional float


'''



class MakeMetaDF():
  def __call__(
    self,
    comic: Comic,
  ) -> pd.DataFrame:
    self.__comic = comic
    self.__make()
    return self.__df
  

  def __make(
    self,
  ) -> typing.NoReturn:
    comic = self.__comic
    meta = comic.metadata
    data = {
      'comic_id': comic.comic_id,
      'title': meta.title,
      'start_year': meta.start_year,
      'magazine': meta.magazine,
      'anime_id': meta.anime_id,
      'overview': meta.overview,
    }
    self.__df = pd.DataFrame(
      [[*data.values()]],
      columns=[*data.keys()],
    )



class MakeTagDF():
  def __call__(
    self,
    comic: Comic,
  ) -> pd.DataFrame:
    self.__comic = comic
    self.__make()
    return self.__df
  

  def __make(
    self,
  ) -> typing.NoReturn:
    comic = self.__comic
    tags = comic.tags
    df = pd.DataFrame(tags)
    df['comic_id'] = (
      comic.comic_id
    )
    df['featured'] = (
      df.featured.astype(int)
    )
    self.__df = df



class MakeAuthorDF():
  def __call__(
    self,
    comic: Comic,
  ) -> pd.DataFrame:
    self.__comic = comic
    self.__make()
    return self.__df
  

  def __make(
    self,
  ) -> typing.NoReturn:
    comic = self.__comic
    meta = comic.metadata
    id_ = comic.comic_id
    authors = meta.authors
    self.__df = pd.DataFrame({
      'comic_id': id_,
      'author': authors,
    })


@dataclasses.dataclass
class ComicDF():
  metadata: pd.DataFrame
  tag: pd.DataFrame
  author: pd.DataFrame



class MakeComicDF():
  
  def __call__(
    self,
    comic: Comic,
  ) -> ComicDF:
    self.__comic = comic
    self.__make()
    return self.__df
    

  def __make(
    self,
  ) -> typing.NoReturn:
    makes = (
      MakeMetaDF(),
      MakeTagDF(),
      MakeAuthorDF(),
    )
    self.__df = ComicDF(*(
      make(self.__comic) 
      for make in makes
    ))




def main():
  site_url = (
    'https://ruijianime.com/'
    'comic/'
  )

  find = FilterComicIds()
  ids = find()
  # print(ids)
  make = MakeComicDF()
  comics = ScrapeComics()(ids)
  for comic in comics:
    print(comic)
    df = make(comic)
    print(df.metadata)
    print(df.tag)
    print(df.author)
    break
  



if __name__ == '__main__':
  main()
