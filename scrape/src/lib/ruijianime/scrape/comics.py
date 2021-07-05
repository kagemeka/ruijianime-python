import typing
from .comic import (
  Comic,
  ScrapeComic,
)
from tqdm import (
  tqdm,
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
    for i in tqdm(self.__ids):
      yield f(i)
