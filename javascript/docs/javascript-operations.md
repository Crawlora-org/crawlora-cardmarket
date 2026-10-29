# Crawlora Cardmarket JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `5`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cardmarket | `cardmarket.catalog` | `cardmarket-catalog` | `GET /cardmarket/catalog` | `kind` (query "singles" \| "nonsingles" \| "accessories")<br>`game_id` (query "1" \| "2" \| "3" \| "5" \| "6" \| "7" \| "8" \| "9" \| "10" \| "11" \| "12" \| "13" \| "15" \| "16" \| "17" \| "18" \| "19" \| "20" \| "21" \| "22" \| "23" \| "24" \| "25")<br>`category_id` (query number)<br>`expansion_id` (query number)<br>`q` (query string)<br>`limit` (query number)<br>`offset` (query number) | `ApiKeyAuth` | `CardmarketCatalogResponse` |  |
| cardmarket | `cardmarket.catalogCategories` | `cardmarket-catalog-categories` | `GET /cardmarket/catalog/categories` | `kind` (query "singles" \| "nonsingles" \| "accessories")<br>`game_id` (query "1" \| "2" \| "3" \| "5" \| "6" \| "7" \| "8" \| "9" \| "10" \| "11" \| "12" \| "13" \| "15" \| "16" \| "17" \| "18" \| "19" \| "20" \| "21" \| "22" \| "23" \| "24" \| "25") | `ApiKeyAuth` | `CardmarketCatalogCategoriesResponse` |  |
| cardmarket | `cardmarket.games` | `cardmarket-games` | `GET /cardmarket/games` | none | `ApiKeyAuth` | `CardmarketGamesResponse` |  |
| cardmarket | `cardmarket.priceGuide` | `cardmarket-price-guide` | `GET /cardmarket/price-guide` | `kind` (query "game" \| "accessories")<br>`game_id` (query "1" \| "2" \| "3" \| "5" \| "6" \| "7" \| "8" \| "9" \| "10" \| "11" \| "12" \| "13" \| "15" \| "16" \| "17" \| "18" \| "19" \| "20" \| "21" \| "22" \| "23" \| "24" \| "25" \| "26" \| "27" \| "28" \| "29" \| "30" \| "31" \| "32" \| "33")<br>`category_id` (query number)<br>`product_id` (query number)<br>`limit` (query number)<br>`offset` (query number) | `ApiKeyAuth` | `CardmarketPriceGuideResponse` |  |
| cardmarket | `cardmarket.priceGuideCategories` | `cardmarket-price-guide-categories` | `GET /cardmarket/price-guide/categories` | `kind` (query "game" \| "accessories")<br>`game_id` (query "1" \| "2" \| "3" \| "5" \| "6" \| "7" \| "8" \| "9" \| "10" \| "11" \| "12" \| "13" \| "15" \| "16" \| "17" \| "18" \| "19" \| "20" \| "21" \| "22" \| "23" \| "24" \| "25" \| "26" \| "27" \| "28" \| "29" \| "30" \| "31" \| "32" \| "33") | `ApiKeyAuth` | `CardmarketPriceGuideCategoriesResponse` |  |
