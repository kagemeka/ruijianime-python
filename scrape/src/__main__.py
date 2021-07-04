import time
from datetime import datetime
import numpy as np
import requests
import pandas as pd
import re
from pprint import (
  pprint,
)


import bs4
import dataclasses
import typing



from \
  lib.ruijianime \
  .scrape.comic_ids \
import (
  FindAllComicIds,
)
from \
  lib.ruijianime \
  .scrape.comics \
import (
  ScrapeComics,
)
from \
  lib.ruijianime \
  .scrape.comic_tags \
import (
  ScrapeTags,
)
from \
  lib.ruijianime \
  .scrape.anime_ids \
import (
  ScrapeAllAnimeIds,
)


import typing
import dataclasses
import bs4 
import requests
import re 




@dataclasses.dataclass
class Staff:
  name: str
  role: str



class ScrapeStaff():
  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> typing.NoReturn:
    self.__section = section
    self.__scrape()
    return self.__staffs
  

  def __find_elements(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    elms = section.find_all(
      'p',
    )[2:-1]
    self.__elms = elms


  def __get_role(
    self,
    elm: bs4.element.Tag,
  ) -> str:
    return elm.text.split(
      ':',
    )[0]


  def __get_names(
    self,
    elm: bs4.element.Tag,
  ) -> typing.List[str]:
    elms = elm.find_all('a')
    return [
      elm.text for elm in elms
    ]


  def __get_staffs(
    self,
    elm: bs4.element.Tag,
  ) -> typing.NoReturn:
    role = self.__get_role(elm)
    names = self.__get_names(
      elm,
    )
    for name in names:
      self.__staffs.append(
        Staff(name, role),
      )


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__find_elements()
    self.__staffs = []
    for elm in self.__elms:
      self.__get_staffs(elm)
    



from unicodedata import (
  normalize,
)


@dataclasses.dataclass
class Metadata():
  title: str
  year: int
  season: int
  media: str
  staffs: typing.List[Staff]
  links: typing.List[str]



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
    self.__meta = Metadata(
      self.__title,
      self.__year,
      self.__season,
      self.__media,
      self.__staffs,
      self.__links,
    )
  



@dataclasses.dataclass
class Anime():
  metadata: Metadata




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
    soup = self.__soup
    scrape = ScrapeMetadata()
    res = scrape(soup)
    print(res)
    self.__anime = None
  






def main():
  site_url = (
    'https://ruijianime.com/'
    'comic/'
  )

  id_ = 26785

  # find = FindAllComicIds()
  # ids = find()
  # comics = ScrapeComics()(ids)
  # for comic in comics:
  #   print(comic)
  #   # break

  # find = ScrapeTags()
  # tags = find()
  # pprint(tags)

  # scrape = ScrapeAllAnimeIds()
  # ids = scrape()
  # pprint(ids)


  id_ = 3354
  id_ = 3362

  scrape = ScrapeAnime()
  scrape(id_)

  



if __name__ == '__main__':
  main()
