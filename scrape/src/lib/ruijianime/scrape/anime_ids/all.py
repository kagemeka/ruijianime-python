import typing
import dataclasses
import bs4 
import requests
import re 


class ScrapeAllAnimeIds():
  def __call__(
    self,
  ) -> typing.NoReturn:
    self.__make_soup()
    self.__scrape()
    return self.__ids
  
  
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__url = (
      'http://ruijianime.com/'
      'main/all_title.php'
    )
  

  def __make_soup(
    self,
  ) -> typing.NoReturn:
    response = requests.get(
      self.__url,
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup
  

  def __parse_id(
    self,
    elm: bs4.element.Tag,
  ) -> int:
    url = elm.get('href')
    ptn = re.compile(
      r'^.*/(\d+)\..*$',
    )
    m = re.match(ptn, url)
    return int(m.group(1))
  

  def __find_(
    self,
  ) -> typing.NoReturn:
    ls = self.__soup.find(
      id='all_title',
    ).find_all(
      class_='link_list',
    )
    

  def __scrape(
    self,
  ) -> typing.NoReturn:
    ls = self.__soup.find(
      id='all_title',
    ).find_all(
      class_='link_list',
    )
    self.__ids = [
      self.__parse_id(
        elm.find('a'),
      )
      for elm in ls
    ]