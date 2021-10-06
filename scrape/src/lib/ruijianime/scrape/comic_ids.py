import typing 
import bs4
import requests
import tqdm 



def scrape_all_comic_ids() -> typing.List[int]:
  URL = 'http://ruijianime.com/comic/title/all_title.php?q='
  QUERY = (
    'a', 'ka', 'sa', 'ta', 'na', 
    'ha', 'ma', 'ya', 'ra', 'wa',
  )

  def find_per_page(query: str) -> typing.NoReturn:
    response = requests.get(f'{URL}{query}')
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    elms = soup.find(id='all_title').find('ul').find_all('li')
    for elm in elms:
      url = elm.find('a').get('href')
      ids.append(int(url.split('=')[-1]))

  ids = []
  for q in tqdm.tqdm(QUERY):
    find_per_page(q)
  return sorted(ids)