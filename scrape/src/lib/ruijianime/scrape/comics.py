import typing
from .comic import Comic, scrape_comic
import tqdm



def scrape_comics(
  comic_ids: typing.List[int],
) -> typing.Iterator[Comic]:
  for i in tqdm.tqdm(comic_ids): yield scrape_comic(i)



# class ScrapeComics():
#   def __call__(
#     self,
#     comic_ids: typing.List[
#       int
#     ],
#   ) -> typing.Iterator[Comic]:
#     fn = ScrapeComic()
#     for i in tqdm.tqdm(comic_ids):
#       yield fn(i)
