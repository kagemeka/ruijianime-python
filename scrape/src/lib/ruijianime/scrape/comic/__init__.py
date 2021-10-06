import dataclasses
import typing 
from .metadata import Metadata, _scrape_metadata
from .tag import Tag, _scrape_tags
import requests
import bs4



@dataclasses.dataclass
class Comic():
  comic_id: int
  metadata: Metadata
  tags: typing.List[Tag]



def scrape_comic(comic_id: int) -> Comic:
  URL = 'http://ruijianime.com/comic/title/index.php?number='
  response = requests.get(f'{URL}{comic_id}')
  soup = bs4.BeautifulSoup(response.content, 'html.parser')
  return Comic(
    comic_id,
    _scrape_metadata(soup),
    _scrape_tags(soup),
  )