import typing
from lib.adam.comic import (
  add_new_comics,
  update_comics,
)
from lib.adam.tags.comic import update_all_comic_tags


def main() -> typing.NoReturn:
  add_new_comics()
  update_comics()
  update_all_comic_tags()


def lambda_handler(event, context) -> typing.NoReturn:
  add_new_comics()
  update_comics()
  update_all_comic_tags()


if __name__ == '__main__':
  main()
