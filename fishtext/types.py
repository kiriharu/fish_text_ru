from typing import Optional
from dataclasses import dataclass


class TextType:
    Sentence = "sentence"
    Paragraph = "paragraph"
    Title = "title"


class TextFormat:
    json = "json"
    html = "html"


@dataclass
class JsonAPIResponse:
    status: str
    text: str
    errorCode: Optional[int]
