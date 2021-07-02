from urllib.robotparser import RobotFileParser
import time
from datetime import datetime
import numpy as np
import requests
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re



import bs4
import dataclasses
import typing


@dataclasses.dataclass
class Metadata():
  title: str
  start_year: int
  authors: typing.List[str]
  magazine: typing.Optional[
    str
  ]
  publisher: str
  anime_id: typing.Optional[
    int
  ]
  overview: str

  


@dataclasses.dataclass
class Tag():
  name: str 
  tag_id: int
  featured: bool
  ratio: typing.Optional[float]



import re
from unicodedata import (
  normalize,
)

class ScrapeMetadata():

  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> Metadata:
    self.__section = section
    self.__scrape()
    return self.__meta
  

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
    self.__start_year = int(
      m.group(1),
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

  def __get_publisher(
    self,
  ) -> typing.NoReturn:
    elm = self.__abst.find_all(
      'p',
    )[2].text.split(
      '/',
    )[-1].strip()
    self.__publisher = elm


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
    self.__get_publisher()
    self.__get_overview()
    self.__get_anime_id()
    self.__meta = Metadata(
      self.__title,
      self.__start_year,
      self.__authors,
      self.__magazine,
      self.__publisher,
      self.__anime_id,
      self.__overview,
    )


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
    self.__find_section()
    self.__scrape()
  

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
  

  def __find_section(
    self,
  ) -> typing.NoReturn:
    section = self.__soup.find(
      id='ind_comic',
    )
    self.__section = section


  def __scrape(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    meta = ScrapeMetadata()
    res = meta(section)
    print(res)
    


def main():
  site_url = (
    'https://ruijianime.com/'
    'comic/'
  )

  id_ = 26785
  id_ = 303

  scrape = ScrapeComic()
  scrape(id_)
  



if __name__ == '__main__':
  main()
