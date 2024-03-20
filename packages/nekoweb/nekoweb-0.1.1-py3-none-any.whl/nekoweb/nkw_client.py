from typing import Any

import attr
import httpx
import tcrutils as tcr

from . import nkw_core as core
from . import nkw_types as types


@attr.s(frozen=True)
class Client:
  """Main component of the Nekoweb API Wrapper. Initialise it with or without api key (you will not be able to access key-required features without an api key).

  Args:
  ---
  api_key (str): Your API Key. Create a new Client instance for each user/apikey when needed.
  """

  api_key: str | None = attr.ib(default=None, validator=attr.validators.instance_of(str))

  async def api(
    self,
    *parts: str,
    method: str = 'GET',
    body: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
  ) -> httpx.Response:
    """### Make an asynchronous HTTP request to BASE_URL/*parts using the httpx library. Perform rate limiting if needed.

    Args:
    ---
    url (str): The URL to send the request to.
    method (str): The HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE'). Default is 'GET'.
    body (dict): The request body to be sent as JSON. Default is {}.
    headers (dict): Headers to be included in the request. Default is {}.

    Returns:
    ---
    httpx.Response: The response object containing the status code, headers, and body.
    """
    url = core.join_url(*parts)

    if headers is None:
      headers = {}

    if body is None:
      body = {}

    async with httpx.AsyncClient() as client:
      return await client.request(method, url, json=body, headers=headers)

  async def site_info(self, username: str) -> types.Info200 | types.InfoError:
    """### nekoweb.org/api/site/info/{username}.

    Args:
        - username (str): Username of the user/site to get information about.

    Return:
        - types.Info200: Successful request
        - types.InfoError: Error response (for example: not found, rate limit exceeded, etc.)
    """
    r = await self.api(f'site/info/{username}')

    return core.finalize_response_for_return(r)
