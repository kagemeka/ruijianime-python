import pandas as pd
import dataclasses
import typing
from \
  lib.ruijianime \
  .scrape.comic \
import (
  Comic,
)
from .author import (
  MakeAuthorDF,
)
from .metadata import (
  MakeMetaDF,
)
from .tag import (
  MakeTagDF,
)



@dataclasses.dataclass
class ComicDF():
  meta: pd.DataFrame
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
