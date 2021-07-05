from .tags import (
  ScrapeTags,
)
import typing


class ScrapeAnimeTags(
  ScrapeTags,
):
  def _set_url(
    self,
  ) -> typing.NoReturn:
    self._url = (
      'http://ruijianime.com/'
      'main/keyword.php'
    )
