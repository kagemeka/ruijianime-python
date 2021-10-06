import typing 
import sys 


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/../..')


set_globals()
sys.path.append(f'{root}/src')
from lib.ruijianime.scrape import (
  scrape_comics,
  scrape_all_comic_ids,
  scrape_comic_tags,
  scrape_anime_tags,
  scrape_all_anime_ids,
)


def test_scrape_comics() -> typing.NoReturn:
  comic_ids = [27691, 27688]
  for comic in scrape_comics(comic_ids):
    print(comic)


def test_scrape_comic_ids() -> typing.NoReturn:
  comic_ids = scrape_all_comic_ids()
  print(comic_ids)


def test_scrape_comic_tags() -> typing.NoReturn:
  comic_tags = scrape_comic_tags()
  print(comic_tags)



def test_scrape_anime_tags() -> typing.NoReturn:
  anime_tags = scrape_anime_tags()
  print(anime_tags)


def test_scrape_anime_ids() -> typing.NoReturn:
  anime_ids = scrape_all_anime_ids()
  print(anime_ids)


if __name__ == '__main__':
  # test_scrape_comics()
  # test_scrape_comic_ids()
  # test_scrape_comic_tags()
  # test_scrape_anime_tags()
  test_scrape_anime_ids()