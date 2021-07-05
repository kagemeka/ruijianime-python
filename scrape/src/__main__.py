import time
from datetime import datetime
import numpy as np
import requests
import pandas as pd
import re
from pprint import (
  pprint,
)


import bs4
import dataclasses
import typing




from \
  lib.ruijianime \
  .scrape.comics \
import (
  ScrapeComics,
)



'''TODO
Adam
'''

from \
  lib.adam.filter_comic_ids \
import (
  FilterComicIds,
)


def main():
  site_url = (
    'https://ruijianime.com/'
    'comic/'
  )

  find = FilterComicIds()
  ids = find()
  print(ids)
  comics = ScrapeComics()(ids)
  for comic in comics:
    print(comic)
    break
  



if __name__ == '__main__':
  main()
