from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.list_unit_types_response_200 import ListUnitTypesResponse_200
from ...types import Response, UNSET, Unset


def _get_kwargs(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
) -> Dict[str, Any]:
    url = "{}/unit-types".format(client.base_url)

    headers: Dict[str, Any] = client.httpx_client.headers
    headers.update(client.get_headers())

    cookies: Dict[str, Any] = client.httpx_client.cookies
    cookies.update(client.get_cookies())

    params: Dict[str, Any] = {}
    if not isinstance(next_token, Unset) and next_token is not None:
        params["nextToken"] = next_token
    if not isinstance(page_size, Unset) and page_size is not None:
        params["pageSize"] = page_size

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ListUnitTypesResponse_200]:
    if response.status_code == 200:
        response_200 = ListUnitTypesResponse_200.from_dict(response.json(), strict=False)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ListUnitTypesResponse_200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
) -> Response[ListUnitTypesResponse_200]:
    kwargs = _get_kwargs(
        client=client,
        next_token=next_token,
        page_size=page_size,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
) -> Optional[ListUnitTypesResponse_200]:
    """List all unit types in the tenant Unit Dictionary, including their constituent units."""

    return sync_detailed(
        client=client,
        next_token=next_token,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
) -> Response[ListUnitTypesResponse_200]:
    kwargs = _get_kwargs(
        client=client,
        next_token=next_token,
        page_size=page_size,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
) -> Optional[ListUnitTypesResponse_200]:
    """List all unit types in the tenant Unit Dictionary, including their constituent units."""

    return (
        await asyncio_detailed(
            client=client,
            next_token=next_token,
            page_size=page_size,
        )
    ).parsed
