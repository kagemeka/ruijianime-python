import typing
import dataclasses
import bs4
import re
import pandas as pd



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