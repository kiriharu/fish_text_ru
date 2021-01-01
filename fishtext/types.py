from enum import Enum
from typing import Optional
from dataclasses import dataclass


class TextType(Enum):
    Sentence = "sentence"
    Paragraph = "paragraph"
    Title = "title"


class TextFormat(Enum):
    json = "json"
    html = "html"


@dataclass
class JsonAPIResponse:
    status: str
    text: str
    errorCode: Optional[int]
