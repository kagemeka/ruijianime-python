from .tags import (
  ScrapeTags,
)
import typing


class ScrapeComicTags(
  ScrapeTags,
):
  def _set_url(
    self,
  ) -> typing.NoReturn:
    self._url = (
      'http://ruijianime.com/'
      'comic/keyword/'
      'keyword.php'
    )

