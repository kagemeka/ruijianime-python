import dataclasses
import typing 
from .metadata import (
  Metadata,
  ScrapeMetadata,
)
from .tag import (
  Tag,
  ScrapeTag,
)
import requests
import bs4



@dataclasses.dataclass
class Comic():
  comic_id: int
  metadata: Metadata
  tags: typing.List[Tag]


class ScrapeComic():
  
  def __call__(
    self,
    comic_id: int,
  ) -> Comic:
    self.__id = comic_id
    self.__make_soup()
    self.__scrape()
    return self.__comic
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'http://ruijianime.com/'
      'comic/title/index.php?'
      'number='
    )


  def __make_soup(
    self,
  ) -> typing.NoReturn:
    url = self.__base_url
    id_ = self.__id
    url = f'{url}{id_}'
    response = requests.get(
      url,
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    soup = self.__soup
    self.__comic = Comic(
      self.__id,
      ScrapeMetadata()(soup),
      ScrapeTag()(soup),
    )