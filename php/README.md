# Crawlora Cardmarket API client for PHP (`crawlora/cardmarket`)

This PHP package calls Crawlora's hosted Cardmarket API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering game and catalogue discovery, product lookup, and price guides. It does not call or scrape Cardmarket directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/cardmarket
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Cardmarket\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("cardmarket-catalog", ['q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 5 API operations.

## Supported Cardmarket API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/cardmarket/catalog` | `cardmarket-catalog` | Search Cardmarket product catalogues |
| `GET` | `/cardmarket/catalog/categories` | `cardmarket-catalog-categories` | Discover Cardmarket catalogue categories and expansions |
| `GET` | `/cardmarket/games` | `cardmarket-games` | Discover Cardmarket download game IDs |
| `GET` | `/cardmarket/price-guide` | `cardmarket-price-guide` | Get Cardmarket daily price-guide data |
| `GET` | `/cardmarket/price-guide/categories` | `cardmarket-price-guide-categories` | Discover Cardmarket price-guide categories |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-cardmarket). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/docs/usage.md).
