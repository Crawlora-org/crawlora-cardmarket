# Cardmarket clients for Crawlora

Official Crawlora client packages for the hosted Cardmarket API. Access 5 API endpoints covering game and catalogue discovery, product lookup, and price guides from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Cardmarket locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Cardmarket or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/cardmarket`](javascript/README.md)
- Python: [`crawlora-cardmarket`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-cardmarket`](go.mod)
- Ruby: [`crawlora-cardmarket`](ruby/README.md)
- Java: [`net.crawlora:crawlora-cardmarket:0.1.0`](java/README.md)
- PHP: [`crawlora/cardmarket`](php/README.md)
- Rust: [`crawlora-cardmarket`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 5 selected public Cardmarket API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/cardmarket/catalog` | `cardmarket-catalog` | Search Cardmarket product catalogues |
| `GET` | `/cardmarket/catalog/categories` | `cardmarket-catalog-categories` | Discover Cardmarket catalogue categories and expansions |
| `GET` | `/cardmarket/games` | `cardmarket-games` | Discover Cardmarket download game IDs |
| `GET` | `/cardmarket/price-guide` | `cardmarket-price-guide` | Get Cardmarket daily price-guide data |
| `GET` | `/cardmarket/price-guide/categories` | `cardmarket-price-guide-categories` | Discover Cardmarket price-guide categories |

## License

MIT. See [LICENSE](LICENSE).
