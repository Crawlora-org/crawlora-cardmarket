# Crawlora Cardmarket Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `5`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cardmarket | `cardmarket.catalog` | `cardmarket-catalog` | `GET /cardmarket/catalog` | `kind` (query String enum{singles, nonsingles, accessories})<br>`game_id` (query String enum{1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25})<br>`category_id` (query i64)<br>`expansion_id` (query i64)<br>`q` (query String)<br>`limit` (query i64)<br>`offset` (query i64) | `ApiKeyAuth` | `CardmarketCatalogResponse` |  |
| cardmarket | `cardmarket.catalog_categories` | `cardmarket-catalog-categories` | `GET /cardmarket/catalog/categories` | `kind` (query String enum{singles, nonsingles, accessories})<br>`game_id` (query String enum{1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}) | `ApiKeyAuth` | `CardmarketCatalogCategoriesResponse` |  |
| cardmarket | `cardmarket.games` | `cardmarket-games` | `GET /cardmarket/games` | none | `ApiKeyAuth` | `CardmarketGamesResponse` |  |
| cardmarket | `cardmarket.price_guide` | `cardmarket-price-guide` | `GET /cardmarket/price-guide` | `kind` (query String enum{game, accessories})<br>`game_id` (query String enum{1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33})<br>`category_id` (query i64)<br>`product_id` (query i64)<br>`limit` (query i64)<br>`offset` (query i64) | `ApiKeyAuth` | `CardmarketPriceGuideResponse` |  |
| cardmarket | `cardmarket.price_guide_categories` | `cardmarket-price-guide-categories` | `GET /cardmarket/price-guide/categories` | `kind` (query String enum{game, accessories})<br>`game_id` (query String enum{1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33}) | `ApiKeyAuth` | `CardmarketPriceGuideCategoriesResponse` |  |
