# Crawlora Cardmarket API client for Java

The official Java client for Crawlora's hosted Cardmarket API. It exposes 5 endpoints covering game and catalogue discovery, product lookup, and price guides. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-cardmarket</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-java-console) to get an API key.

```java
import net.crawlora.cardmarket.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.games(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Cardmarket API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/docs/usage.md) also lists parameters and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/cardmarket/catalog` | `cardmarket-catalog` | Search Cardmarket product catalogues |
| `GET` | `/cardmarket/catalog/categories` | `cardmarket-catalog-categories` | Discover Cardmarket catalogue categories and expansions |
| `GET` | `/cardmarket/games` | `cardmarket-games` | Discover Cardmarket download game IDs |
| `GET` | `/cardmarket/price-guide` | `cardmarket-price-guide` | Get Cardmarket daily price-guide data |
| `GET` | `/cardmarket/price-guide/categories` | `cardmarket-price-guide-categories` | Discover Cardmarket price-guide categories |

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-cardmarket)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-java-api-docs)
