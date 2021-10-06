import bs4
import typing
from itertools import (
  chain,
)
import dataclasses
import requests 
import abc 
from abc import (
  ABC,
  abstractmethod,
)


@dataclasses.dataclass
class Tag():
  name: str
  tag_id: int




def scrape_comic_tags():
  URL = 'http://ruijianime.com/comic/keyword/keyword.php'
  return __scrape_tags(URL)


def scrape_anime_tags():
  URL = 'http://ruijianime.com/main/keyword.php'
  return __scrape_tags(URL)


def __scrape_tags(url: str) -> typing.List[Tag]:
  response = requests.get(url)
  soup = bs4.BeautifulSoup(response.content, 'html.parser')

  def _extract(elm: bs4.element.Tag) -> Tag:
    url = elm.get('href')
    id_ = url.split('=')[-1]
    name = elm.text
    return Tag(name, int(id_))
  
  def get_new_tags() -> typing.NoReturn:
    for elm in soup.find(id='new_keyword').find_all('a'): 
      tags.append(_extract(elm))
    
  def get_general_tags() -> typing.NoReturn:
    for elm in chain.from_iterable(
      elm.find_all('a')
      for elm in soup.find_all(class_='group_key_ul')
    ): tags.append(_extract(elm))
  
  tags = []
  get_new_tags()
  get_general_tags()
  return tags 
