from lib.adam import (
  AdamComic,
)



def main():
  AdamComic()()


def lambda_handler(
  event,
  context,
):
  main()


if __name__ == '__main__':
  main()
