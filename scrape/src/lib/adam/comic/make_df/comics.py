import pandas as pd
import typing
from .comic import (
  MakeComicDF,
  ComicDF,
)
from lib.ruijianime.scrape \
import (
  ScrapeComics,
  ScrapeAllComicIds,
)
from .fetch_scraped_ids import(
  FetchScrapedIds,
)


class MakeComicsDF():
  def __call__(
    self,
  ) -> typing.Optional[
    ComicDF
  ]:
    self.__get_ids()
    if not self.__ids: return
    self.__scrape()
    self.__make()
    return self.__df

  
  def __get_ids(
    self,
  ) -> typing.NoReturn:
    ids = ScrapeAllComicIds()()
    ids = set(ids)
    ids -= FetchScrapedIds()()
    self.__ids = list(ids)
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    fn = ScrapeComics()
    ids = self.__ids
    self.__comics = fn(ids)
  

  def __make(
    self,
  ) -> typing.NoReturn:
    fn = MakeComicDF()
    comics = self.__comics
    meta = []
    tag = []
    author = []
    for comic in comics:
      df = fn(comic)
      meta.append(df.meta)
      tag.append(df.tag)
      author.append(df.author)
    self.__df = ComicDF(
      pd.concat(meta),
      pd.concat(tag),
      pd.concat(author),
    )