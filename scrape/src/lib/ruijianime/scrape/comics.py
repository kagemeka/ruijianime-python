import typing
from .comic import (
  Comic,
  ScrapeComic,
)


class ScrapeComics():

  def __call__(
    self,
    comic_ids: typing.List[
      int
    ],
  ) -> typing.Iterator[Comic]:
    self.__ids = comic_ids
    return self.__scrape()


  def __scrape(
    self,
  ) -> typing.Iterator[Comic]:
    f = ScrapeComic()
    for i in self.__ids:
      yield f(i)