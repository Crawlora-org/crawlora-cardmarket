"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class CardmarketClient(CrawloraClient):
    """Synchronous Cardmarket API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-cardmarket-python/0.1.0')
        super().__init__(*args, **kwargs)

    def catalog(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cardmarket-catalog', params, response_type=response_type, timeout=timeout, headers=headers)

    def catalog_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cardmarket-catalog-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cardmarket-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def price_guide(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cardmarket-price-guide', params, response_type=response_type, timeout=timeout, headers=headers)

    def price_guide_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cardmarket-price-guide-categories', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncCardmarketClient(AsyncCrawloraClient):
    """Asynchronous Cardmarket API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-cardmarket-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def catalog(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cardmarket-catalog', params, response_type=response_type, timeout=timeout, headers=headers)

    async def catalog_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cardmarket-catalog-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cardmarket-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def price_guide(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cardmarket-price-guide', params, response_type=response_type, timeout=timeout, headers=headers)

    async def price_guide_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cardmarket-price-guide-categories', params, response_type=response_type, timeout=timeout, headers=headers)
