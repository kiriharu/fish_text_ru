# -*- coding: utf-8 -*-
#
#  fish_text_ru: Async API.
#  Created by LulzLoL231 at 17/08/22
#
from typing import Optional

try:
    from httpx import AsyncClient, Response
except ImportError:
    raise ImportError('Before use async API, please install httpx package.')

from fishtext.types import TextType, TextFormat, JsonAPIResponse
from fishtext.errors import (
    TooManyContentExceeded,
    CallLimitExceeded,
    BannedForever,
    InternalServerError,
)


FISH_TEXT_API_URL = "https://fish-text.ru/get"
FISH_TEXT_API_DOCS = "https://fish-text.ru/api"


class AsyncFishTextAPI:
    def __init__(
        self, *,
        api_url: str,
        text_type: TextType,
        text_format: TextFormat,
        client: Optional[AsyncClient] = None,
    ):
        self.client = client or AsyncClient()
        self.api_url = api_url
        self.text_type = text_type
        self.text_format = text_format

    def process_response(self, response) -> None:
        raise NotImplementedError

    def get(self, number: int = 100):
        raise NotImplementedError


class AsyncFishTextJson(AsyncFishTextAPI):
    def __init__(
        self, *,
        client: Optional[AsyncClient] = None,
        api_url: str = FISH_TEXT_API_URL,
        text_type: TextType = TextType.Sentence,
    ):
        super().__init__(
            client=client,
            api_url=api_url,
            text_type=text_type,
            text_format=TextFormat.json,
        )

    def process_response(self, response: JsonAPIResponse) -> None:

        if response.errorCode is None:
            return

        error_codes = {
            11: TooManyContentExceeded,
            21: CallLimitExceeded,
            22: BannedForever,
            31: InternalServerError,
        }

        exception = error_codes.get(response.errorCode, None)
        if exception:
            raise exception(response.text)

    async def get(self, number: int = 100) -> JsonAPIResponse:
        json_response = (await self.client.get(
            FISH_TEXT_API_URL,
            params=dict(
                format=self.text_format, number=number,
                type=self.text_type
            ),
        )).json()
        json_api_response_object = JsonAPIResponse(
            status=json_response.get("status"),
            text=json_response.get("text"),
            errorCode=json_response.get("errorCode", None),
        )
        self.process_response(json_api_response_object)
        return json_api_response_object


class AsyncFishTextHtml(AsyncFishTextAPI):

    TOO_MUCH_CONTENT_EXCEEDED = (
        "You requested too much content. Be more moderate."
    )

    def __init__(
        self, *,
        client: Optional[AsyncClient] = None,
        api_url: str = FISH_TEXT_API_URL,
        text_type: TextType = TextType.Sentence,
    ):
        super().__init__(
            client=client,
            api_url=api_url,
            text_type=text_type,
            text_format=TextFormat.html,
        )

    def process_response(self, response: Response) -> None:
        if response.text == self.TOO_MUCH_CONTENT_EXCEEDED:
            raise TooManyContentExceeded(response.text)
        if response.status_code == 403:
            raise CallLimitExceeded(response.text)
            # TODO: дописать BannedForever
        if response.status_code == 500:
            raise InternalServerError(response.text)

    async def get(self, number: int = 100) -> str:
        response = (await self.client.get(
            FISH_TEXT_API_URL,
            params=dict(
                format=self.text_format, number=number,
                type=self.text_type
            ),
        ))
        self.process_response(response)
        return response.text
