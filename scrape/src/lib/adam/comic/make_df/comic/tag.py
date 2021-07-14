import pandas as pd
import typing
from dataclasses import (
  fields,
)
from \
  kgmk.ruijianime \
  .scrape.comic \
import (
  Comic,
  Tag,
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
    df = pd.DataFrame(
      tags,
      columns=list(
        Tag.__annotations__
        .keys(),
      ),
    )
    df['comic_id'] = (
      comic.comic_id
    )
    df['featured'] = (
      df.featured.astype(int)
    )
    self.__df = df