from typing import Literal, TypedDict

from .. import nkw_core as core


async def readfolder():
  return await core.api('files/readfolder')
