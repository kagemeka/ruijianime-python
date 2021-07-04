
import bs4
import typing
from itertools import (
  chain,
)
import dataclasses
import requests 



@dataclasses.dataclass
class Tag():
  name: str
  tag_id: int



class ScrapeTags():
  def __call__(
    self,
  ) -> typing.List[Tag]:
    self.__make_soup()
    self.__scrape()
    return self.__tags


  def __get_new_tags(
    self,
  ) -> typing.NoReturn:
    ls = self.__soup.find(
      id='new_keyword',
    ).find_all('a')
    for elm in ls:
      t = self.__get_tag(elm)
      self.__tags.append(t)
    

  def __get_tag(
    self,
    elm: bs4.element.Tag,
  ) -> Tag:
    url = elm.get('href')
    id_ = url.split('=')[-1]
    name = elm.text
    return Tag(name, int(id_))
  

  def __get_tags(
    self,
  ) -> typing.NoReturn:
    ls = self.__soup.find_all(
      class_='group_key_ul',
    )
    elms = chain.from_iterable(
      elm.find_all('a')
      for elm in ls      
    )
    for elm in elms:
      t = self.__get_tag(elm)
      self.__tags.append(t)
    
  
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__url = (
      'http://ruijianime.com/'
      'comic/keyword/'
      'keyword.php'
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

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__tags = []
    self.__get_new_tags()
    self.__get_tags()
