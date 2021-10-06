import dataclasses
import requests
import bs4
import typing 
from .metadata import (
  Metadata,
  ScrapeMetadata,
)
from .composition import (
  Composition,
  ScrapeComposition,
)
from .tag import (
  Tag,
  ScrapeTag,
)



@dataclasses.dataclass
class Anime():
  anime_id: int
  metadata: Metadata
  composition: Composition
  tags: typing.List[Tag]



class ScrapeAnime():

  def __call__(
    self,
    anime_id: int,
  ) -> Anime:
    self.__id = anime_id
    self.__make_soup()
    self.__scrape()
    return self.__anime
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'http://ruijianime.com/'
      'main/ind/'
    )


  def __make_soup(
    self,
  ) -> typing.NoReturn:
    url = self.__base_url
    id_ = self.__id
    url = f'{url}{id_}.php'
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
    scrapes = (
      ScrapeMetadata(),
      ScrapeComposition(),
      ScrapeTag(),
    )
    self.__anime = Anime(
      self.__id,
      *(
        f(self.__soup)
        for f in scrapes
      ),
    )