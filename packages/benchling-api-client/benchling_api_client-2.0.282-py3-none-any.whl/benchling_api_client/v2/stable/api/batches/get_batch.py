from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.batch import Batch
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    batch_id: str,
) -> Dict[str, Any]:
    url = "{}/batches/{batch_id}".format(client.base_url, batch_id=batch_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Batch, BadRequestError]]:
    if response.status_code == 200:
        response_200 = Batch.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json(), strict=False)

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Batch, BadRequestError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    batch_id: str,
) -> Response[Union[Batch, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        batch_id=batch_id,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    batch_id: str,
) -> Optional[Union[Batch, BadRequestError]]:
    """ Get a batch """

    return sync_detailed(
        client=client,
        batch_id=batch_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    batch_id: str,
) -> Response[Union[Batch, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        batch_id=batch_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    batch_id: str,
) -> Optional[Union[Batch, BadRequestError]]:
    """ Get a batch """

    return (
        await asyncio_detailed(
            client=client,
            batch_id=batch_id,
        )
    ).parsed
