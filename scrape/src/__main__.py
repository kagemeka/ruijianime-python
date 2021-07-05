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
  .scrape.comic_ids \
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
  ScrapeComicTags,
)
from \
  lib.ruijianime \
  .scrape.anime_tags \
import (
  ScrapeAnimeTags,
)
from \
  lib.ruijianime \
  .scrape.anime_ids \
import (
  ScrapeAllAnimeIds,
)


from \
  lib.ruijianime \
  .scrape.anime \
import (
  ScrapeAnime,
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

  # find = ScrapeComicTags()
  # tags = find()
  # pprint(tags)

  find = ScrapeAnimeTags()
  tags = find()
  pprint(tags)

  # scrape = ScrapeAllAnimeIds()
  # ids = scrape()
  # pprint(ids)



  # ids = [
  #   3354,
  #   3362,
  # ]
  # for i in ids:
  #   scrape = ScrapeAnime()
  #   pprint(scrape(i))

  



if __name__ == '__main__':
  main()
