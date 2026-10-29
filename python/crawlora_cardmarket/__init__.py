"""Typed Cardmarket client for the Crawlora hosted API."""

from .platform import CardmarketClient, AsyncCardmarketClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = CardmarketClient
AsyncClient = AsyncCardmarketClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Cardmarket'
PLATFORM = 'cardmarket'
CONTRACT_REVISION = 'sha256:1626894d49b099a4c2e5f26ffd7437052fb854af8f775db8e5e01271ccc7a705'

__all__ = [
    "CardmarketClient", "AsyncCardmarketClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
