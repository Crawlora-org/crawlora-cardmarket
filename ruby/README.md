# Crawlora Cardmarket API client for Ruby (`crawlora-cardmarket`)

This Ruby gem calls Crawlora's hosted Cardmarket API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering game and catalogue discovery, product lookup, and price guides; it does not call or scrape Cardmarket directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-cardmarket"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/cardmarket"

client = Crawlora::Cardmarket::Client.new
result = client.request("cardmarket-catalog", JSON.parse("{\"q\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 5 API operations.

```ruby
client = Crawlora::Cardmarket::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Cardmarket API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/cardmarket/catalog` | `cardmarket-catalog` | Search Cardmarket product catalogues |
| `GET` | `/cardmarket/catalog/categories` | `cardmarket-catalog-categories` | Discover Cardmarket catalogue categories and expansions |
| `GET` | `/cardmarket/games` | `cardmarket-games` | Discover Cardmarket download game IDs |
| `GET` | `/cardmarket/price-guide` | `cardmarket-price-guide` | Get Cardmarket daily price-guide data |
| `GET` | `/cardmarket/price-guide/categories` | `cardmarket-price-guide-categories` | Discover Cardmarket price-guide categories |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-cardmarket) for account setup, the API operation reference, and release history.
