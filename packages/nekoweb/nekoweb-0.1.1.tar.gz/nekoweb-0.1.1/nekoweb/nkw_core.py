import asyncio
import time
from typing import Any

import httpx

from .nkw_constants import *


def join_url(*parts: str):
  """Concatenates url parts with '/' and prepends consts.URL."""
  if not parts:
    ValueError('At least 1 part is required')

  return URL + '/'.join(parts)


async def perform_rate_limiting(rate_limit: float):
  """Wait until the rate limit has been satisfied."""
  await asyncio.sleep(rate_limit)


def finalize_response_for_return(r: httpx.Response) -> dict[str, Any]:
  match r.status_code:
    case 200:
      data = r.json()
    case status_code:
      data = {
        'status_code': status_code,
        'error': True,
      }

  return {'status_code': r.status_code, 'error': False, **data}
