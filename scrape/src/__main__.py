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
  .scrape.comic_id \
import (
  FindAllComicIds,
)
from \
  lib.ruijianime \
  .scrape.comics \
import (
  ScrapeComics,
)
from \
  lib.ruijianime \
  .scrape.comic_tags \
import (
  ScrapeTags,
)






def main():
  site_url = (
    'https://ruijianime.com/'
    'comic/'
  )

  id_ = 26785

  # find = FindAllComicIds()
  # ids = find()
  # comics = ScrapeComics()(ids)
  # for comic in comics:
  #   print(comic)
  #   # break
  find = ScrapeTags()
  tags = find()
  pprint(tags)



if __name__ == '__main__':
  main()
