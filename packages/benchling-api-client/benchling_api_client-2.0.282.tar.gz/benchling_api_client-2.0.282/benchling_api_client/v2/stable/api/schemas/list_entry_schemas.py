from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.entry_schemas_paginated_list import EntrySchemasPaginatedList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/entry-schemas".format(client.base_url)

    headers: Dict[str, Any] = client.httpx_client.headers
    headers.update(client.get_headers())

    cookies: Dict[str, Any] = client.httpx_client.cookies
    cookies.update(client.get_cookies())

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[EntrySchemasPaginatedList, BadRequestError]]:
    if response.status_code == 200:
        response_200 = EntrySchemasPaginatedList.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json(), strict=False)

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[EntrySchemasPaginatedList, BadRequestError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[EntrySchemasPaginatedList, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[EntrySchemasPaginatedList, BadRequestError]]:
    """ List entry schemas """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[EntrySchemasPaginatedList, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[EntrySchemasPaginatedList, BadRequestError]]:
    """ List entry schemas """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
