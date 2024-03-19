import uuid
from dataclasses import dataclass

import httpx
from fastapi import HTTPException
from pydantic import TypeAdapter
from typing_extensions import Any


@dataclass
class MicroserviceOption:
    is_json: bool = True
    headers: dict = None


@dataclass
class ReplaceMicroserviceConfig:
    url: str


def serialize_uuid_to_str(data: Any = None):
    if data is None:
        return None

    if isinstance(data, dict):
        return {key: serialize_uuid_to_str(value) for key, value in data.items()}

    if isinstance(data, list):
        return [serialize_uuid_to_str(item) for item in data]

    if isinstance(data, uuid.UUID):
        return str(data)

    return data


class BaseMicroserviceClient:
    def filter_none_values(self, query_params: dict | None):
        return {key: value for key, value in query_params.items() if value is not None} if query_params else None

    async def send(
        self, url: str, query_params: dict, body_params: any, response_type: any, option: MicroserviceOption = None
    ):
        if not ReplaceMicroserviceConfig.url:
            raise Exception("Please config microservice url")

        url = ReplaceMicroserviceConfig.url + url
        if not option:
            option = MicroserviceOption()

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=url,
                headers=option.headers,
                params=self.filter_none_values(query_params),
                data=body_params if not option.is_json else None,
                json=serialize_uuid_to_str(body_params) if option.is_json else None,
            )
            data = response.json()
            if response.status_code < 200 or response.status_code > 299:
                raise HTTPException(status_code=response.status_code, detail=data)
            if not response_type:
                return data

            return TypeAdapter(response_type).validate_python(data)
