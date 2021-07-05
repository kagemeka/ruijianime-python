import pandas as pd
import typing
from .comic import (
  MakeComicDF,
  ComicDF,
)
from lib.adam import (
  FilterComicIds,
)
from \
  lib.ruijianime \
  .scrape.comics \
import (
  ScrapeComics,
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
    get = FilterComicIds()
    self.__ids = get()
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    f = ScrapeComics()
    self.__comics = f(
      self.__ids,
    )
  

  def __make(
    self,
  ) -> typing.NoReturn:
    f = MakeComicDF()
    comics = self.__comics
    meta = []
    tag = []
    author = []
    for comic in comics:
      df = f(comic)
      meta.append(df.meta)
      tag.append(df.tag)
      author.append(df.author)
    meta = pd.concat(meta)
    tag = pd.concat(tag)
    author = pd.concat(author)
    self.__df = ComicDF(
      meta,
      tag,
      author,
    )