from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelCardmarketPriceGuideCategoriesResponseDoc = TypedDict('ModelCardmarketPriceGuideCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCardmarketPriceGuideCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCardmarketPriceGuideCategoriesResponse = TypedDict('ModelCardmarketPriceGuideCategoriesResponse', {
    'category_ids': NotRequired[list[ModelCardmarketPriceGuideCategory]],
    'created_at': NotRequired[str],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[int],
    'kind': NotRequired[str],
    'price_redistribution_policy_status': NotRequired[str],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
    'version': NotRequired[int],
}, total=False)

ModelCardmarketPriceGuideCategory = TypedDict('ModelCardmarketPriceGuideCategory', {
    'id': NotRequired[int],
    'item_count': NotRequired[int],
}, total=False)

ModelCardmarketPriceGuideResponseDoc = TypedDict('ModelCardmarketPriceGuideResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCardmarketPriceGuideResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCardmarketPriceGuideResponse = TypedDict('ModelCardmarketPriceGuideResponse', {
    'category_id': NotRequired[int],
    'category_ids': NotRequired[list[ModelCardmarketPriceGuideCategory]],
    'created_at': NotRequired[str],
    'empty_state': NotRequired[str],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[int],
    'items': NotRequired[list[ModelCardmarketPriceGuideEntry]],
    'kind': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'price_redistribution_policy_status': NotRequired[str],
    'product_id': NotRequired[int],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
    'version': NotRequired[int],
}, total=False)

ModelCardmarketPriceGuideEntry = TypedDict('ModelCardmarketPriceGuideEntry', {
    'average': NotRequired[float],
    'average_1d': NotRequired[float],
    'average_1d_foil': NotRequired[float],
    'average_1d_holo': NotRequired[float],
    'average_30d': NotRequired[float],
    'average_30d_foil': NotRequired[float],
    'average_30d_holo': NotRequired[float],
    'average_7d': NotRequired[float],
    'average_7d_foil': NotRequired[float],
    'average_7d_holo': NotRequired[float],
    'average_foil': NotRequired[float],
    'average_holo': NotRequired[float],
    'category_id': NotRequired[int],
    'low': NotRequired[float],
    'low_foil': NotRequired[float],
    'low_holo': NotRequired[float],
    'product_id': NotRequired[int],
    'trend': NotRequired[float],
    'trend_foil': NotRequired[float],
    'trend_holo': NotRequired[float],
}, total=False)

ModelCardmarketGamesResponseDoc = TypedDict('ModelCardmarketGamesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCardmarketGamesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCardmarketGamesResponse = TypedDict('ModelCardmarketGamesResponse', {
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelCardmarketGame]],
    'total': NotRequired[int],
}, total=False)

ModelCardmarketGame = TypedDict('ModelCardmarketGame', {
    'catalog_available': NotRequired[bool],
    'catalog_kinds': NotRequired[list[str]],
    'id': NotRequired[int],
    'price_guide_available': NotRequired[bool],
}, total=False)

ModelCardmarketCatalogCategoriesResponseDoc = TypedDict('ModelCardmarketCatalogCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCardmarketCatalogCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCardmarketCatalogCategoriesResponse = TypedDict('ModelCardmarketCatalogCategoriesResponse', {
    'categories': NotRequired[list[ModelCardmarketCatalogCategory]],
    'category_total': NotRequired[int],
    'created_at': NotRequired[str],
    'expansion_total': NotRequired[int],
    'expansions': NotRequired[list[ModelCardmarketCatalogExpansion]],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[int],
    'kind': NotRequired[str],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'version': NotRequired[int],
}, total=False)

ModelCardmarketCatalogExpansion = TypedDict('ModelCardmarketCatalogExpansion', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'product_count': NotRequired[int],
}, total=False)

ModelCardmarketCatalogCategory = TypedDict('ModelCardmarketCatalogCategory', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'product_count': NotRequired[int],
}, total=False)

ModelCardmarketCatalogResponseDoc = TypedDict('ModelCardmarketCatalogResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCardmarketCatalogResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCardmarketCatalogResponse = TypedDict('ModelCardmarketCatalogResponse', {
    'categories': NotRequired[list[ModelCardmarketCatalogCategory]],
    'category_id': NotRequired[int],
    'created_at': NotRequired[str],
    'empty_state': NotRequired[str],
    'expansion_id': NotRequired[int],
    'expansions': NotRequired[list[ModelCardmarketCatalogExpansion]],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[int],
    'items': NotRequired[list[ModelCardmarketProduct]],
    'kind': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'q': NotRequired[str],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
    'version': NotRequired[int],
}, total=False)

ModelCardmarketProduct = TypedDict('ModelCardmarketProduct', {
    'category': NotRequired[str],
    'category_id': NotRequired[int],
    'date_added': NotRequired[str],
    'expansion': NotRequired[str],
    'expansion_id': NotRequired[int],
    'id': NotRequired[int],
    'metacard_id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

CardmarketCatalogResponse = ModelCardmarketCatalogResponseDoc
CardmarketCatalogParams = TypedDict('CardmarketCatalogParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': NotRequired[Literal['singles', 'nonsingles', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']],
    'category_id': NotRequired[int],
    'expansion_id': NotRequired[int],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

CardmarketCatalogCategoriesResponse = ModelCardmarketCatalogCategoriesResponseDoc
CardmarketCatalogCategoriesParams = TypedDict('CardmarketCatalogCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': NotRequired[Literal['singles', 'nonsingles', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']],
}, total=False)

CardmarketGamesResponse = ModelCardmarketGamesResponseDoc
CardmarketGamesParams = TypedDict('CardmarketGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

CardmarketPriceGuideResponse = ModelCardmarketPriceGuideResponseDoc
CardmarketPriceGuideParams = TypedDict('CardmarketPriceGuideParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': NotRequired[Literal['game', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']],
    'category_id': NotRequired[int],
    'product_id': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

CardmarketPriceGuideCategoriesResponse = ModelCardmarketPriceGuideCategoriesResponseDoc
CardmarketPriceGuideCategoriesParams = TypedDict('CardmarketPriceGuideCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': NotRequired[Literal['game', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']],
}, total=False)

class CardmarketGroup:
    @overload
    def catalog(self, **params: Unpack[CardmarketCatalogStreamParams]) -> BinaryIO: ...
    @overload
    def catalog(self, **params: Unpack[CardmarketCatalogTextResponseParams]) -> str: ...
    @overload
    def catalog(self, **params: Unpack[CardmarketCatalogDefaultParams]) -> CardmarketCatalogResponse: ...
    @overload
    def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesTextResponseParams]) -> str: ...
    @overload
    def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesDefaultParams]) -> CardmarketCatalogCategoriesResponse: ...
    @overload
    def games(self, **params: Unpack[CardmarketGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[CardmarketGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[CardmarketGamesDefaultParams]) -> CardmarketGamesResponse: ...
    @overload
    def price_guide(self, **params: Unpack[CardmarketPriceGuideStreamParams]) -> BinaryIO: ...
    @overload
    def price_guide(self, **params: Unpack[CardmarketPriceGuideTextResponseParams]) -> str: ...
    @overload
    def price_guide(self, **params: Unpack[CardmarketPriceGuideDefaultParams]) -> CardmarketPriceGuideResponse: ...
    @overload
    def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesTextResponseParams]) -> str: ...
    @overload
    def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesDefaultParams]) -> CardmarketPriceGuideCategoriesResponse: ...

OperationId = Literal[
    'cardmarket-catalog',
    'cardmarket-catalog-categories',
    'cardmarket-games',
    'cardmarket-price-guide',
    'cardmarket-price-guide-categories',
]

class CrawloraClient:
    cardmarket: CardmarketGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cardmarket-catalog'],
        params: CardmarketCatalogParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketCatalogResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cardmarket-catalog-categories'],
        params: CardmarketCatalogCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketCatalogCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cardmarket-games'],
        params: CardmarketGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cardmarket-price-guide'],
        params: CardmarketPriceGuideParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketPriceGuideResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cardmarket-price-guide-categories'],
        params: CardmarketPriceGuideCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketPriceGuideCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['cardmarket-catalog'],
        params: CardmarketCatalogParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketCatalogResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cardmarket-catalog-categories'],
        params: CardmarketCatalogCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketCatalogCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cardmarket-games'],
        params: CardmarketGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cardmarket-price-guide'],
        params: CardmarketPriceGuideParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketPriceGuideResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cardmarket-price-guide-categories'],
        params: CardmarketPriceGuideCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CardmarketPriceGuideCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class CardmarketClient(CrawloraClient):
    def __enter__(self) -> CardmarketClient: ...
    @overload
    def catalog(self, **params: Unpack[CardmarketCatalogStreamParams]) -> BinaryIO: ...
    @overload
    def catalog(self, **params: Unpack[CardmarketCatalogTextResponseParams]) -> str: ...
    @overload
    def catalog(self, **params: Unpack[CardmarketCatalogDefaultParams]) -> CardmarketCatalogResponse: ...
    @overload
    def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesTextResponseParams]) -> str: ...
    @overload
    def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesDefaultParams]) -> CardmarketCatalogCategoriesResponse: ...
    @overload
    def games(self, **params: Unpack[CardmarketGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[CardmarketGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[CardmarketGamesDefaultParams]) -> CardmarketGamesResponse: ...
    @overload
    def price_guide(self, **params: Unpack[CardmarketPriceGuideStreamParams]) -> BinaryIO: ...
    @overload
    def price_guide(self, **params: Unpack[CardmarketPriceGuideTextResponseParams]) -> str: ...
    @overload
    def price_guide(self, **params: Unpack[CardmarketPriceGuideDefaultParams]) -> CardmarketPriceGuideResponse: ...
    @overload
    def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesTextResponseParams]) -> str: ...
    @overload
    def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesDefaultParams]) -> CardmarketPriceGuideCategoriesResponse: ...

class AsyncCardmarketClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncCardmarketClient: ...
    cardmarket: _AsyncCardmarketGroup
    @overload
    async def catalog(self, **params: Unpack[CardmarketCatalogStreamParams]) -> BinaryIO: ...
    @overload
    async def catalog(self, **params: Unpack[CardmarketCatalogTextResponseParams]) -> str: ...
    @overload
    async def catalog(self, **params: Unpack[CardmarketCatalogDefaultParams]) -> CardmarketCatalogResponse: ...
    @overload
    async def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesTextResponseParams]) -> str: ...
    @overload
    async def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesDefaultParams]) -> CardmarketCatalogCategoriesResponse: ...
    @overload
    async def games(self, **params: Unpack[CardmarketGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[CardmarketGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[CardmarketGamesDefaultParams]) -> CardmarketGamesResponse: ...
    @overload
    async def price_guide(self, **params: Unpack[CardmarketPriceGuideStreamParams]) -> BinaryIO: ...
    @overload
    async def price_guide(self, **params: Unpack[CardmarketPriceGuideTextResponseParams]) -> str: ...
    @overload
    async def price_guide(self, **params: Unpack[CardmarketPriceGuideDefaultParams]) -> CardmarketPriceGuideResponse: ...
    @overload
    async def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesTextResponseParams]) -> str: ...
    @overload
    async def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesDefaultParams]) -> CardmarketPriceGuideCategoriesResponse: ...

class _AsyncCardmarketGroup:
    @overload
    async def catalog(self, **params: Unpack[CardmarketCatalogStreamParams]) -> BinaryIO: ...
    @overload
    async def catalog(self, **params: Unpack[CardmarketCatalogTextResponseParams]) -> str: ...
    @overload
    async def catalog(self, **params: Unpack[CardmarketCatalogDefaultParams]) -> CardmarketCatalogResponse: ...
    @overload
    async def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesTextResponseParams]) -> str: ...
    @overload
    async def catalog_categories(self, **params: Unpack[CardmarketCatalogCategoriesDefaultParams]) -> CardmarketCatalogCategoriesResponse: ...
    @overload
    async def games(self, **params: Unpack[CardmarketGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[CardmarketGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[CardmarketGamesDefaultParams]) -> CardmarketGamesResponse: ...
    @overload
    async def price_guide(self, **params: Unpack[CardmarketPriceGuideStreamParams]) -> BinaryIO: ...
    @overload
    async def price_guide(self, **params: Unpack[CardmarketPriceGuideTextResponseParams]) -> str: ...
    @overload
    async def price_guide(self, **params: Unpack[CardmarketPriceGuideDefaultParams]) -> CardmarketPriceGuideResponse: ...
    @overload
    async def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesTextResponseParams]) -> str: ...
    @overload
    async def price_guide_categories(self, **params: Unpack[CardmarketPriceGuideCategoriesDefaultParams]) -> CardmarketPriceGuideCategoriesResponse: ...

CardmarketCatalogDefaultParams = TypedDict('CardmarketCatalogDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'kind': NotRequired[Literal['singles', 'nonsingles', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']],
    'category_id': NotRequired[int],
    'expansion_id': NotRequired[int],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

CardmarketCatalogTextResponseParams = TypedDict('CardmarketCatalogTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'kind': NotRequired[Literal['singles', 'nonsingles', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']],
    'category_id': NotRequired[int],
    'expansion_id': NotRequired[int],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

CardmarketCatalogStreamParams = TypedDict('CardmarketCatalogStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'kind': NotRequired[Literal['singles', 'nonsingles', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']],
    'category_id': NotRequired[int],
    'expansion_id': NotRequired[int],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

CardmarketCatalogCategoriesDefaultParams = TypedDict('CardmarketCatalogCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'kind': NotRequired[Literal['singles', 'nonsingles', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']],
}, total=False)

CardmarketCatalogCategoriesTextResponseParams = TypedDict('CardmarketCatalogCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'kind': NotRequired[Literal['singles', 'nonsingles', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']],
}, total=False)

CardmarketCatalogCategoriesStreamParams = TypedDict('CardmarketCatalogCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'kind': NotRequired[Literal['singles', 'nonsingles', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']],
}, total=False)

CardmarketGamesDefaultParams = TypedDict('CardmarketGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

CardmarketGamesTextResponseParams = TypedDict('CardmarketGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

CardmarketGamesStreamParams = TypedDict('CardmarketGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

CardmarketPriceGuideDefaultParams = TypedDict('CardmarketPriceGuideDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'kind': NotRequired[Literal['game', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']],
    'category_id': NotRequired[int],
    'product_id': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

CardmarketPriceGuideTextResponseParams = TypedDict('CardmarketPriceGuideTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'kind': NotRequired[Literal['game', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']],
    'category_id': NotRequired[int],
    'product_id': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

CardmarketPriceGuideStreamParams = TypedDict('CardmarketPriceGuideStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'kind': NotRequired[Literal['game', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']],
    'category_id': NotRequired[int],
    'product_id': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

CardmarketPriceGuideCategoriesDefaultParams = TypedDict('CardmarketPriceGuideCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'kind': NotRequired[Literal['game', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']],
}, total=False)

CardmarketPriceGuideCategoriesTextResponseParams = TypedDict('CardmarketPriceGuideCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'kind': NotRequired[Literal['game', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']],
}, total=False)

CardmarketPriceGuideCategoriesStreamParams = TypedDict('CardmarketPriceGuideCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'kind': NotRequired[Literal['game', 'accessories']],
    'game_id': NotRequired[Literal['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']],
}, total=False)
