import pandas as pd
import dataclasses
import typing
from lib.ruijianime.scrape.comic import Comic
from lib.ruijianime.scrape.comic.tag import Tag



@dataclasses.dataclass
class ComicDataFrame():
  meta: pd.DataFrame
  tag: pd.DataFrame
  author: pd.DataFrame



class MakeComicDataFrame():
  def __make(self) -> typing.NoReturn:
    self.__make_meta()
    self.__make_tag()
    self.__make_author()
    self.__df = ComicDataFrame(
      self.__meta,
      self.__tag,
      self.__author,
    )

  
  def __make_meta(self) -> typing.NoReturn:
    comic = self.__comic
    meta = comic.metadata
    data = {
      'comic_id': comic.comic_id,
      'title': meta.title,
      'start_year': meta.start_year,
      'magazine': meta.magazine,
      'anime_id': meta.anime_id,
      'overview': meta.overview,
    }
    self.__meta = pd.DataFrame(
      [[*data.values()]],
      columns=[*data.keys()],
    )
  

  def __make_tag(self) -> typing.NoReturn:
    comic = self.__comic
    df = pd.DataFrame(
      comic.tags,
      columns=list(Tag.__annotations__.keys()),
    )
    df['comic_id'] = comic.comic_id
    df['featured'] = df.featured.astype(int)
    self.__tag = df


  def __make_author(self) -> typing.NoReturn:
    comic = self.__comic
    self.__author = pd.DataFrame({
      'comic_id': comic.comic_id,
      'author': comic.metadata.authors,
    })
  

  def from_comic(self, comic: Comic) -> ComicDataFrame:
    self.__comic = comic
    self.__make()
    return self.__df


  def from_comics(
    self, 
    comics: typing.Iterable[Comic],
  ) -> typing.Optional[ComicDataFrame]:
    meta, tag, author = [], [], []
    for comic in comics:
      print(comic)
      df = self.from_comic(comic)
      meta.append(df.meta)
      tag.append(df.tag)
      author.append(df.author)
    if not meta: return None
    return ComicDataFrame(
      pd.concat(meta), 
      pd.concat(tag),
      pd.concat(author),
    )
