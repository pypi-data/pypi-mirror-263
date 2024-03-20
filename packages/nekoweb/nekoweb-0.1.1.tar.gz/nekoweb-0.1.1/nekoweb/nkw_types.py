from typing import Literal, TypedDict


class Info200(TypedDict):
  status_code: Literal[200]
  error: Literal[False]
  id: int
  username: str
  title: str
  updates: int
  followers: int
  views: int
  created_at: int
  updated_at: int


class InfoError(TypedDict):
  status_code: int
  error: Literal[True]
