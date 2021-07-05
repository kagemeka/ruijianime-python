import typing
import dataclasses
import bs4 
import re 
import numpy as np



@dataclasses.dataclass
class Composition():
  story: float
  drawing: float
  direction: float
  character: float
  sound: float
  voice_actor: float



class ScrapeComposition():
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Composition:
    self.__soup = soup
    self.__scrape()
    return self.__comp


  def __find_elements(
    self,
  ) -> typing.NoReturn:
    js = self.__soup.find_all(
      'script',
      type='text/javascript',
    )[2]
    js = ''.join(
      str(js).split(),
    )
    ptn = re.compile(
      r'.*res_data.addRows\('
      r'([^;]*)\);.*',
    )
    m = re.match(ptn, js)
    comp = eval(m.group(1))
    comp = np.array(
      comp,
    )[:, 1].astype(float) / 100
    self.__elms = comp


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__find_elements()
    self.__comp = Composition(
      *self.__elms,
    )