__version__ = "2.1.0"
from .api import FishTextJson, FishTextHtml, FishTextAPI
try:
    from .async_api import (
        AsyncFishTextJson, AsyncFishTextHtml, AsyncFishTextAPI
    )
except ImportError:
    pass
