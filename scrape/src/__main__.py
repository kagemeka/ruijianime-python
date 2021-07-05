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
  .scrape.comic \
import (
  Comic,
)

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



'''schema
metadata
 comic_id
 title
 start_year
 magazine: Optional
 anime_id: Optional
 overview

tags
  comic_id
  tag_id
  name
  featured: 1/0
  ratio: Optional float


'''



import pandas as pd
from \
  lib.ruijianime \
  .scrape.comic \
import (
  Comic,
)

from \
  lib.adam.make_df.comic \
import (
  MakeComicDF,
)



def main():
  site_url = (
    'https://ruijianime.com/'
    'comic/'
  )

  find = FilterComicIds()
  ids = find()
  # print(ids)
  make = MakeComicDF()
  comics = ScrapeComics()(ids)
  for comic in comics:
    print(comic)
    df = make(comic)
    print(df.metadata)
    print(df.tag)
    print(df.author)
    break
  



if __name__ == '__main__':
  main()
