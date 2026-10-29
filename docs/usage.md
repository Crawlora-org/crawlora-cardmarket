# Cardmarket API endpoint reference and client usage

This reference lists all 5 public Cardmarket API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/cardmarket`, `crawlora-cardmarket`, and `crawlora-cardmarket` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Cardmarket locally; Crawlora is independent from and not endorsed by Cardmarket or its owners.

The package tracks the public API contract revision `sha256:1626894d49b099a4c2e5f26ffd7437052fb854af8f775db8e5e01271ccc7a705` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `cardmarket`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `catalog` | `catalog` | `cardmarket.catalog` | `GET /cardmarket/catalog` | `kind` (query, optional; values: `singles`, `nonsingles`, `accessories`), `game_id` (query, optional; values: `1`, `2`, `3`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`), `category_id` (query, optional), `expansion_id` (query, optional), `q` (query, optional), `limit` (query, optional), `offset` (query, optional) | Search Cardmarket product catalogues |
| `catalogCategories` | `catalog_categories` | `cardmarket.catalog_categories` | `GET /cardmarket/catalog/categories` | `kind` (query, optional; values: `singles`, `nonsingles`, `accessories`), `game_id` (query, optional; values: `1`, `2`, `3`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`) | Discover Cardmarket catalogue categories and expansions |
| `games` | `games` | `cardmarket.games` | `GET /cardmarket/games` | — | Discover Cardmarket download game IDs |
| `priceGuide` | `price_guide` | `cardmarket.price_guide` | `GET /cardmarket/price-guide` | `kind` (query, optional; values: `game`, `accessories`), `game_id` (query, optional; values: `1`, `2`, `3`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`), `category_id` (query, optional), `product_id` (query, optional), `limit` (query, optional), `offset` (query, optional) | Get Cardmarket daily price-guide data |
| `priceGuideCategories` | `price_guide_categories` | `cardmarket.price_guide_categories` | `GET /cardmarket/price-guide/categories` | `kind` (query, optional; values: `game`, `accessories`), `game_id` (query, optional; values: `1`, `2`, `3`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`) | Discover Cardmarket price-guide categories |

## Client forms

- JavaScript: import `CardmarketClient` (also exported as `Client`) from `@crawlora-org/cardmarket`; use `new CardmarketClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `CardmarketClient` (also exported as `Client`) from `crawlora_cardmarket`; use `with CardmarketClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncCardmarketClient`, used with `async with` and `await`.
- Rust: add `crawlora-cardmarket` with Cargo; import `Client` and the generated operation parameter struct, then call `client.cardmarket.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
