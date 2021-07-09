import typing

from .make_df import (
  MakeComicsDF,
)

from .store import (
  Store,
)



class AdamComic():
  def __call__(
    self,
  ) -> typing.NoReturn:
    df = MakeComicsDF()()
    if df is None: return
    Store()(df)