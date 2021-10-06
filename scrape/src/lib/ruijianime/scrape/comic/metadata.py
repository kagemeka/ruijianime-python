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



def _scrape_metadata(soup: bs4.BeautifulSoup) -> Metadata:
  def find_section() -> typing.NoReturn:
    return soup.find(id='ind_comic')

  def get_title(section: bs4.element.Tag) -> str:
    return section.find('h1').text
  
  def get_authors(
    abstract: bs4.element.Tag,
  ) -> typing.List[str]:
    return [
      elm.text 
      for elm in abstract.find_all('p')[1].find_all('a')
    ]

  def get_start_year(
    abstract: bs4.element.Tag,
  ) -> typing.Optional[int]:
    s = abstract.find(class_='date').text
    s = normalize('NFKD', s)
    ptn = re.compile(r'^.*:(\d+)年$')
    m = re.match(ptn, s)
    return int(m.group(1)) if m else None

  def find_abstract(
    section: bs4.element.Tag
  ) -> bs4.element.Tag:
    return section.find(id='abst-str')
  
  def get_magazine(
    abstract: bs4.element.Tag,
  ) -> typing.Optional[str]:
    elm = abstract.find_all('p')[2].find('a')
    return elm.text if elm else None

  def get_publishers(
    abstract: bs4.element.Tag
  ) -> typing.List[str]:
    return [
      e.strip() 
      for e in abstract.find_all('p')[2].text.split('/')[1:]
    ]

  def get_overview(section: bs4.element.Tag) -> str:
    s = section.find(id='abst_exp').find('p').text
    return ' '.join(s.split()[:-1])

  def get_anime_id(
    abstract: bs4.element.Tag,
  ) -> typing.Optional[int]:
    elm = abstract.find_all('p')[4].find('a')
    if elm is None: return None
    url = elm.get('href')
    ptn = r'^.*/(\d+)\.php$'
    m = re.match(ptn, url)
    return int(m.group(1))

  section = find_section()
  abstract = find_abstract(section)
  return Metadata(
    title=get_title(section),
    start_year=get_start_year(abstract),
    authors=get_authors(abstract),
    magazine=get_magazine(abstract),
    publishers=get_publishers(abstract),
    anime_id=get_anime_id(abstract),
    overview=get_overview(section),
  )
