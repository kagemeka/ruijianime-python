import typing 
import sys 


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/..')


set_globals()
sys.path.append(f'{root}/src')
from lib.adam.tags.comic import (
  update_all_comic_tags,
)
from lib.adam.comic import (
  add_new_comics,
  update_comics,
)



def test_update_comic_tags() -> typing.NoReturn:
  update_all_comic_tags()


def test_add_new_comics() -> typing.NoReturn:
  add_new_comics()


def test_update_comics() -> typing.NoReturn:
  update_comics()


if __name__ == '__main__':
  # test_update_comic_tags()
  test_add_new_comics()
  test_update_comics()