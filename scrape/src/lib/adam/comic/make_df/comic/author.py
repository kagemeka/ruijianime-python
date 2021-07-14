import pandas as pd
import typing
from \
  kgmk.ruijianime \
  .scrape.comic \
import (
  Comic,
)



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