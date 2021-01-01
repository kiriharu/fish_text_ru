from typing import Optional
from dataclasses import dataclass
from enum import Enum


class TextType(str, Enum):
    Sentence = "sentence"
    Paragraph = "paragraph"
    Title = "title"


class TextFormat(str, Enum):
    json = "json"
    html = "html"


@dataclass
class JsonAPIResponse:
    status: str
    text: str
    errorCode: Optional[int]
