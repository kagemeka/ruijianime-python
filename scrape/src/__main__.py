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
  publishers: typing.List[str]
  anime_id: typing.Optional[
    int
  ]
  overview: str

  




import re
from unicodedata import (
  normalize,
)

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


from pprint import (
  pprint,
)

@dataclasses.dataclass
class Tag():
  name: str 
  tag_id: int
  featured: bool = False
  ratio: typing.Optional[
    float
  ] = None



class ScrapeTag():
  
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> typing.NoReturn:
    self.__soup = soup
    self.__scrape()
    return self.__tags
  

  def __get_featured_tags(
    self,
  ) -> typing.NoReturn:
    js = self.__soup.find_all(
      'script', 
      type='text/javascript',
    )[1]
    js = ''.join(
      str(js).split(),
    )
    ptn = re.compile(
      r'.*world_data.addRows\('
      r'([^;]*)\);.*',
    )
    m = re.match(ptn, js)
    tags = eval(m.group(1))
    df = pd.DataFrame(
      tags,
      columns=[
        'name', 
        'amount',
      ],
    )
    tot = df.amount.sum()
    df['ratio'] = (
      df.amount / tot
    )
    tags = dict(zip(
      df.name, 
      df.ratio,
    ))
    self.__tags = tags


  def __get_tags(
    self,
  ) -> typing.NoReturn:
    self.__get_featured_tags()
    featured = self.__tags
    elms = self.__soup.find(
      id='ind_main_keyword',
    ).find_all('a')
    tags = []
    for elm in elms:
      name = elm.text
      url = elm.get('href')
      tag_id = int(
        url.split('=')[-1],
      )
      tag = Tag(
        name,
        tag_id,
      )
      if name in featured:
        tag.featured = True
        tag.ratio = featured[
          name
        ]
      tags.append(tag)
    self.__tags = tags


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_tags()




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
    


# class FindComicId():
  
  # def __cl


class ScrapeComics():

  def __call__(
    self,
  ) -> typing.Iterator[Comic]:
    return self.__scrape()
  

  def __get_comic_ids(
    self,
    query: str,
  ) -> typing.NoReturn:
    ids = self.__ids
    response = requests.get(
      f'{self.__base_url}'
      f'{query}',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    elms = soup.find(
      id='all_title',
    ).find('ul').find_all('li')
    for elm in elms:
      url = elm.find(
        'a',
      ).get('href')
      id_ = url.split('=')[-1]
      ids.append(id_)


  def __find_comic_ids(
    self,
  ) -> typing.NoReturn:
    query = (
      'a', 'ka', 'sa', 'ta',
      'na', 'ha', 'ma', 'ya',
      'ra', 'wa',
    )
    self.__ids = []
    for q in query:
      self.__get_comic_ids(q)


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'http://ruijianime.com/'
      'comic/title/all_title'
      '.php?q='
    )


  def __scrape(
    self,
  ) -> typing.Iterator[Comic]:
    self.__find_comic_ids()
    f = ScrapeComic()
    for i in self.__ids:
      yield f(i)



def main():
  site_url = (
    'https://ruijianime.com/'
    'comic/'
  )

  id_ = 26785
  # id_ = 303
  # id_ = 1

  # scrape = ScrapeComic()
  # scrape(id_)
  comics = ScrapeComics()()
  for comic in comics:
    print(comic)
    # break
  



if __name__ == '__main__':
  main()
