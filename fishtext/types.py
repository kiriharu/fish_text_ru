from typing import Optional
from dataclasses import dataclass
from enum import Enum


class StrEnum(Enum, str):
    pass


class TextType(StrEnum):
    Sentence = "sentence"
    Paragraph = "paragraph"
    Title = "title"


class TextFormat(StrEnum):
    json = "json"
    html = "html"


@dataclass
class JsonAPIResponse:
    status: str
    text: str
    errorCode: Optional[int]
