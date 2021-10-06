import typing
import dataclasses
import bs4 
import requests
import re 



def scrape_all_anime_ids() -> typing.List[int]:
  
  URL = 'http://ruijianime.com/main/all_title.php'
  response = requests.get(URL)
  soup = bs4.BeautifulSoup(response.content, 'html.parser')
    
  def parse_id(elm: bs4.element.Tag) -> int:
    url = elm.get('href')
    ptn = re.compile(r'^.*/(\d+)\..*$')
    m = re.match(ptn, url)
    return int(m.group(1))

  ls = soup.find(id='all_title').find_all(class_='link_list')
  return sorted([parse_id(elm.find('a')) for elm in ls])