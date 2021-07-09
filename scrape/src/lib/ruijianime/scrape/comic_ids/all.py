import typing 
import bs4
import requests



class ScrapeAllComicIds():
  
  def __call__(
    self,
  ) -> typing.List[int]:
    self.__find()
    return self.__ids
  

  def __find(
    self,
  ) -> typing.NoReturn:
    self.__ids = []
    for q in self.__query:
      self.__find_per_page(q)


  def __find_per_page(
    self,
    query: str,
  ) -> typing.NoReturn:
    response = requests.get(
      f'{self.__base_url}'
      f'{query}',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    elms = soup.find(
      id='all_title',
    ).find('ul').find_all('li')
    for elm in elms:
      url = elm.find(
        'a',
      ).get('href')
      self.__ids.append(
        int(url.split('=')[-1])
      )


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'http://ruijianime.com/'
      'comic/title/all_title'
      '.php?q='
    )
    self.__query = (
      'a', 'ka', 'sa', 'ta',
      'na', 'ha', 'ma', 'ya',
      'ra', 'wa',
    )