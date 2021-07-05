import dataclasses
import typing
import re
from unicodedata import (
  normalize,
)
import bs4



@dataclasses.dataclass
class Metadata():
  title: str
  start_year: typing.Optional[
    int
  ]
  authors: typing.List[str]
  magazine: typing.Optional[
    str
  ]
  publishers: typing.List[str]
  anime_id: typing.Optional[
    int
  ]
  overview: str


  
class ScrapeMetadata():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Metadata:
    self.__soup = soup 
    self.__find_section()
    self.__scrape()
    return self.__meta


  def __find_section(
    self,
  ) -> typing.NoReturn:
    section = self.__soup.find(
      id='ind_comic',
    )
    self.__section = section
  

  def __get_title(
    self,
  ) -> typing.NoReturn:
    elm = self.__section.find(
      'h1',
    )
    self.__title = elm.text
  

  def __get_authors(
    self,
  ) -> typing.NoReturn:
    ls = self.__abst.find_all(
      'p',
    )[1].find_all('a')
    self.__authors = [
      elm.text
      for elm in ls
    ]


  def __get_start_year(
    self,
  ) -> typing.NoReturn:
    s = self.__abst.find(
      class_='date',
    ).text
    s = normalize('NFKD', s)
    ptn = re.compile(
      r'^.*:(\d+)年$'
    )
    m = re.match(ptn, s)
    self.__start_year = (
      int(m.group(1)) if m
      else None
    )


  def __find_abst(
    self,
  ) -> typing.NoReturn:
    abst = self.__section.find(
      id='abst-str',
    )
    self.__abst = abst

  
  def __get_magazine(
    self,
  ) -> typing.NoReturn:
    elm = self.__abst.find_all(
      'p',
    )[2].find('a')
    self.__magazine = (
      elm.text if elm else None
    )

  def __get_publishers(
    self,
  ) -> typing.NoReturn:
    ls = self.__abst.find_all(
      'p',
    )[2].text.split(
      '/',
    )[1:]
    self.__publishers = [
      e.strip() for e in ls
    ]


  def __get_overview(
    self,
  ) -> typing.NoReturn:
    s = self.__section.find(
      id='abst_exp',
    ).find('p').text
    s = ' '.join(
      s.split()[:-1],
    )
    self.__overview = s
  

  def __get_anime_id(
    self,
  ) -> typing.NoReturn:
    elm = self.__abst.find_all(
      'p',
    )[4].find('a')
    if elm is None:
      self.__anime_id = None
      return
    ptn = r'^.*/(\d+)\.php$'
    url = elm.get('href')
    m = re.match(ptn, url)
    self.__anime_id = int(
      m.group(1),
    )


  def __scrape(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    self.__get_title()
    self.__find_abst()
    self.__get_start_year()
    self.__get_authors()
    self.__get_magazine()
    self.__get_publishers()
    self.__get_overview()
    self.__get_anime_id()
    self.__meta = Metadata(
      self.__title,
      self.__start_year,
      self.__authors,
      self.__magazine,
      self.__publishers,
      self.__anime_id,
      self.__overview,
    )