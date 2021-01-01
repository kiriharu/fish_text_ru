from fishtext import FishTextJson
from fishtext.types import TextType

api = FishTextJson(text_type=TextType.Title)
titles = api.get(10)

for title in titles.text.split("\\n\\n"):
    print(title)