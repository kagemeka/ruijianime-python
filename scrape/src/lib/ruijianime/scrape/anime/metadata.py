import typing
import dataclasses
import bs4 
import re 
from unicodedata import (
  normalize,
)
from .voice_actor import (
  VoiceActor,
)
from .staff import (
  Staff,
  ScrapeStaff,
)



@dataclasses.dataclass
class Metadata():
  title: str
  year: int
  season: int
  media: str
  staffs: typing.List[Staff]
  links: typing.List[str]
  voice_actors: typing.List[
    VoiceActor
  ]
  overview: str



class ScrapeMetadata():
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Metadata:
    self.__soup = soup
    self.__scrape()
    return self.__meta
  

  def __find_section(
    self,
  ) -> typing.NoReturn:
    section = self.__soup.find(
      id='ind_anime',
    )
    self.__section = section
  

  def __find_abst(
    self,
  ) -> typing.NoReturn:
    abst = self.__section.find(
      id='abst-str',
    )
    self.__abst = abst


  def __get_title(
    self,
  ) -> typing.NoReturn:
    elm = self.__section.find(
      'h1',
    )
    self.__title = elm.text

  
  def __get_media(
    self,
  ) -> typing.NoReturn: 
    s = self.__abst.find_all(
      'p',
    )[1].text
    s = normalize('NFKD', s)
    s = s.split(':')[1].strip()
    self.__media = s


  def __get_staffs(
    self,
  ) -> typing.NoReturn:
    f = ScrapeStaff()
    self.__staffs = f(
      self.__abst,
    )
  

  def __get_voice_actors(
    self,
  ) -> typing.NoReturn:
    elms = self.__abst.find(
      class_='origin_cast',
    ).find_all('li')
    ls = []
    for elm in elms:
      s = elm.text.strip()
      actor = VoiceActor(
        *s.split(':')[::-1],
      )
      ls.append(actor)
    self.__voice_actors = ls 
    
  
  def __get_year_season(
    self,
  ) -> typing.NoReturn:
    elm = self.__abst.find(
      class_='date',
    )
    url = elm.find('a').get(
      'href',
    )
    ptn = re.compile(
      r'^.*/(\d+)-(\d)\..*$',
    )
    m = re.match(ptn, url)
    year = int(m.group(1))
    season = int(m.group(2))
    self.__year = year
    self.__season = season
  

  def __get_links(
    self,
  ) -> typing.NoReturn:
    elm = self.__abst.find_all(
      'p',
    )[-1]
    elms = elm.find_all('a')
    self.__links = [
      elm.get('href')
      for elm in elms
    ]
  

  def __get_overview(
    self,
  ) -> typing.NoReturn:
    s = self.__section.find(
      id='abst_exp',
    ).find('p').text
    self.__overview = ' '.join(
      s.split()[:-1],
    )


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__find_section()
    self.__get_title()
    self.__find_abst()
    self.__get_year_season()
    self.__get_staffs()
    self.__get_links()
    self.__get_media()
    self.__get_voice_actors()
    self.__get_overview()
    self.__meta = Metadata(
      self.__title,
      self.__year,
      self.__season,
      self.__media,
      self.__staffs,
      self.__links,
      self.__voice_actors,
      self.__overview,
    )