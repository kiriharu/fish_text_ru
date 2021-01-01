from typing import Optional, Dict

from requests.sessions import Session
from requests.models import Response

from fishtext.types import TextType, TextFormat, JsonAPIResponse
from fishtext.errors import (
    TooManyContentExceeded,
    CallLimitExceeded,
    BannedForever,
    InternalServerError,
)


FISH_TEXT_API_URL = "https://fish-text.ru/get"
FISH_TEXT_API_DOCS = "https://fish-text.ru/api"


class FishTextAPI:
    def __init__(
        self, *,
        api_url: str,
        text_type: TextType,
        text_format: TextFormat,
        session: Optional[Session] = None,
    ):
        self.session = session or Session()
        self.api_url = api_url
        self.text_type = text_type
        self.text_format = text_format

    def process_response(self, response) -> None:
        raise NotImplementedError

    def get(self, number: int = 100):
        raise NotImplementedError


class FishTextJson(FishTextAPI):
    def __init__(
        self, *,
        session: Optional[Session] = None,
        api_url: str = FISH_TEXT_API_URL,
        text_type: TextType = TextType.Sentence,
    ):
        super().__init__(
            session=session,
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

    def get(self, number: int = 100) -> JsonAPIResponse:
        json_response = self.session.get(
            FISH_TEXT_API_URL,
            params=dict(
                format=self.text_format, number=number, type=self.text_type
            ),
        ).json()
        json_api_response_object = JsonAPIResponse(
            status=json_response.get("status"),
            text=json_response.get("text"),
            errorCode=json_response.get("errorCode", None),
        )
        self.process_response(json_api_response_object)
        return json_api_response_object


class FishTextHtml(FishTextAPI):

    TOO_MUCH_CONTENT_EXCEEDED = (
        "You requested too much content. Be more moderate."
    )

    def __init__(
        self, *,
        session: Optional[Session] = None,
        api_url: str = FISH_TEXT_API_URL,
        text_type: TextType = TextType.Sentence,
    ):
        super().__init__(
            session=session,
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

    def get(self, number: int = 100) -> str:
        response = self.session.get(
            FISH_TEXT_API_URL,
            params=dict(
                format=self.text_format, number=number, type=self.text_type
            ),
        )
        self.process_response(response)
        return response.text
