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
    fn = ScrapeComic()
    for i in tqdm(comic_ids):
      yield fn(i)
