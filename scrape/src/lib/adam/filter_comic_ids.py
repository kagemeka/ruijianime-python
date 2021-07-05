import boto3
import typing
from \
  lib.ruijianime \
  .scrape.comic_ids \
import (
  FindAllComicIds,
)



class FilterComicIds():
  def __call__(
    self,
  ) -> typing.List[int]:
    ids = self.__scrape()
    ids -= (
      self.__fetch_from_cloud()
    )
    return list(ids)
  

  def __scrape(
    self,
  ) -> typing.Set[int]:
    return set(
      FindAllComicIds()(),
    )
    

  def __fetch_from_cloud(
    self,
  ) -> typing.Set[int]:
    ...
    '''TODO
    change pseudo to real
    '''
    return set()