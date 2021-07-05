import bs4
import typing
from itertools import (
  chain,
)
import dataclasses
import requests 
from abc import (
  ABC,
  abstractmethod,
)



@dataclasses.dataclass
class Tag():
  name: str
  tag_id: int



class ScrapeTags(
  ABC,
):
  def __call__(
    self,
  ) -> typing.List[Tag]:
    self._make_soup()
    self._scrape()
    return self._tags


  def _get_new_tags(
    self,
  ) -> typing.NoReturn:
    ls = self._soup.find(
      id='new_keyword',
    ).find_all('a')
    for elm in ls:
      t = self._get_tag(elm)
      self._tags.append(t)
    

  def _get_tag(
    self,
    elm: bs4.element.Tag,
  ) -> Tag:
    url = elm.get('href')
    id_ = url.split('=')[-1]
    name = elm.text
    return Tag(name, int(id_))
  

  def _get_tags(
    self,
  ) -> typing.NoReturn:
    ls = self._soup.find_all(
      class_='group_key_ul',
    )
    elms = chain.from_iterable(
      elm.find_all('a')
      for elm in ls      
    )
    for elm in elms:
      t = self._get_tag(elm)
      self._tags.append(t)
    
  
  def __init__(
    self,
  ) -> typing.NoReturn:
    self._set_url()


  @abstractmethod  
  def _set_url(
    self,
  ) -> typing.NoReturn:
    ... 
    self._url: str
  

  def _make_soup(
    self,
  ) -> typing.NoReturn:
    response = requests.get(
      self._url,
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self._soup = soup

  
  def _scrape(
    self,
  ) -> typing.NoReturn:
    self._tags = []
    self._get_new_tags()
    self._get_tags()
