import typing
import dataclasses
import bs4 



@dataclasses.dataclass
class Tag():
  name: str
  tag_id: int



class ScrapeTag():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> typing.List[Tag]:
    self.__soup = soup
    self.__scrape()
    return self.__tags
  

  def __find_elements(
    self,
  ) -> typing.NoReturn:
    elms = self.__soup.find(
      id='major_keyword',
    ).find_all('a')
    self.__elms = elms
  

  def __get_tag(
    self,
    elm: bs4.element.Tag,
  ) -> Tag:
    name = elm.text
    url = elm.get('href')
    id_ = url.split('=')[-1]
    return Tag(name, int(id_))


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__find_elements()
    self.__tags = [
      self.__get_tag(elm)
      for elm in self.__elms
    ]