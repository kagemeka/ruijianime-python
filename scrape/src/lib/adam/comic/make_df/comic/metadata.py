
import pandas as pd
import typing
from \
  kgmk.ruijianime \
  .scrape.comic \
import (
  Comic,
)



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