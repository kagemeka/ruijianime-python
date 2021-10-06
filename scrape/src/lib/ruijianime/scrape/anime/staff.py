import typing
import dataclasses
import bs4



@dataclasses.dataclass
class Staff:
  name: str
  role: str



class ScrapeStaff():
  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> typing.NoReturn:
    self.__section = section
    self.__scrape()
    return self.__staffs
  

  def __find_elements(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    elms = section.find_all(
      'p',
    )[2:-1]
    self.__elms = elms


  def __get_role(
    self,
    elm: bs4.element.Tag,
  ) -> str:
    return elm.text.split(
      ':',
    )[0]


  def __get_names(
    self,
    elm: bs4.element.Tag,
  ) -> typing.List[str]:
    elms = elm.find_all('a')
    return [
      elm.text for elm in elms
    ]


  def __get_staffs(
    self,
    elm: bs4.element.Tag,
  ) -> typing.NoReturn:
    role = self.__get_role(elm)
    names = self.__get_names(
      elm,
    )
    for name in names:
      self.__staffs.append(
        Staff(name, role),
      )


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__find_elements()
    self.__staffs = []
    for elm in self.__elms:
      self.__get_staffs(elm)