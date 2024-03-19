from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.list_locations_sort import ListLocationsSort
from ...models.locations_paginated_list import LocationsPaginatedList
from ...types import Response, UNSET, Unset


def _get_kwargs(
    *,
    client: Client,
    sort: Union[Unset, ListLocationsSort] = ListLocationsSort.MODIFIEDAT,
    schema_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ancestor_storage_id: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    barcodes: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    namesany_ofcase_sensitive: Union[Unset, str] = UNSET,
    creator_ids: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/locations".format(client.base_url)

    headers: Dict[str, Any] = client.httpx_client.headers
    headers.update(client.get_headers())

    cookies: Dict[str, Any] = client.httpx_client.cookies
    cookies.update(client.get_cookies())

    json_sort: Union[Unset, int] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params: Dict[str, Any] = {}
    if not isinstance(json_sort, Unset) and json_sort is not None:
        params["sort"] = json_sort
    if not isinstance(schema_id, Unset) and schema_id is not None:
        params["schemaId"] = schema_id
    if not isinstance(name, Unset) and name is not None:
        params["name"] = name
    if not isinstance(name_includes, Unset) and name_includes is not None:
        params["nameIncludes"] = name_includes
    if not isinstance(ancestor_storage_id, Unset) and ancestor_storage_id is not None:
        params["ancestorStorageId"] = ancestor_storage_id
    if not isinstance(ids, Unset) and ids is not None:
        params["ids"] = ids
    if not isinstance(barcodes, Unset) and barcodes is not None:
        params["barcodes"] = barcodes
    if not isinstance(namesany_of, Unset) and namesany_of is not None:
        params["names.anyOf"] = namesany_of
    if not isinstance(namesany_ofcase_sensitive, Unset) and namesany_ofcase_sensitive is not None:
        params["names.anyOf.caseSensitive"] = namesany_ofcase_sensitive
    if not isinstance(creator_ids, Unset) and creator_ids is not None:
        params["creatorIds"] = creator_ids

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[LocationsPaginatedList, BadRequestError]]:
    if response.status_code == 200:
        response_200 = LocationsPaginatedList.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json(), strict=False)

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[LocationsPaginatedList, BadRequestError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sort: Union[Unset, ListLocationsSort] = ListLocationsSort.MODIFIEDAT,
    schema_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ancestor_storage_id: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    barcodes: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    namesany_ofcase_sensitive: Union[Unset, str] = UNSET,
    creator_ids: Union[Unset, str] = UNSET,
) -> Response[Union[LocationsPaginatedList, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        sort=sort,
        schema_id=schema_id,
        name=name,
        name_includes=name_includes,
        ancestor_storage_id=ancestor_storage_id,
        ids=ids,
        barcodes=barcodes,
        namesany_of=namesany_of,
        namesany_ofcase_sensitive=namesany_ofcase_sensitive,
        creator_ids=creator_ids,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    sort: Union[Unset, ListLocationsSort] = ListLocationsSort.MODIFIEDAT,
    schema_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ancestor_storage_id: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    barcodes: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    namesany_ofcase_sensitive: Union[Unset, str] = UNSET,
    creator_ids: Union[Unset, str] = UNSET,
) -> Optional[Union[LocationsPaginatedList, BadRequestError]]:
    """ List locations """

    return sync_detailed(
        client=client,
        sort=sort,
        schema_id=schema_id,
        name=name,
        name_includes=name_includes,
        ancestor_storage_id=ancestor_storage_id,
        ids=ids,
        barcodes=barcodes,
        namesany_of=namesany_of,
        namesany_ofcase_sensitive=namesany_ofcase_sensitive,
        creator_ids=creator_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    sort: Union[Unset, ListLocationsSort] = ListLocationsSort.MODIFIEDAT,
    schema_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ancestor_storage_id: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    barcodes: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    namesany_ofcase_sensitive: Union[Unset, str] = UNSET,
    creator_ids: Union[Unset, str] = UNSET,
) -> Response[Union[LocationsPaginatedList, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        sort=sort,
        schema_id=schema_id,
        name=name,
        name_includes=name_includes,
        ancestor_storage_id=ancestor_storage_id,
        ids=ids,
        barcodes=barcodes,
        namesany_of=namesany_of,
        namesany_ofcase_sensitive=namesany_ofcase_sensitive,
        creator_ids=creator_ids,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    sort: Union[Unset, ListLocationsSort] = ListLocationsSort.MODIFIEDAT,
    schema_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_includes: Union[Unset, str] = UNSET,
    ancestor_storage_id: Union[Unset, str] = UNSET,
    ids: Union[Unset, str] = UNSET,
    barcodes: Union[Unset, str] = UNSET,
    namesany_of: Union[Unset, str] = UNSET,
    namesany_ofcase_sensitive: Union[Unset, str] = UNSET,
    creator_ids: Union[Unset, str] = UNSET,
) -> Optional[Union[LocationsPaginatedList, BadRequestError]]:
    """ List locations """

    return (
        await asyncio_detailed(
            client=client,
            sort=sort,
            schema_id=schema_id,
            name=name,
            name_includes=name_includes,
            ancestor_storage_id=ancestor_storage_id,
            ids=ids,
            barcodes=barcodes,
            namesany_of=namesany_of,
            namesany_ofcase_sensitive=namesany_ofcase_sensitive,
            creator_ids=creator_ids,
        )
    ).parsed
