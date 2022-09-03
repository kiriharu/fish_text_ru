from asyncio import get_event_loop

from fishtext import AsyncFishTextJson
from fishtext.types import TextType

loop = get_event_loop()
api = AsyncFishTextJson(text_type=TextType.Title)
titles = loop.run_until_complete(api.get(10))

for title in titles.text.split("\\n\\n"):
    print(title)
