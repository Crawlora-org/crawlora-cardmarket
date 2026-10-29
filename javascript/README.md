# @crawlora-org/cardmarket — Cardmarket API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Cardmarket API.
It exposes 5 API endpoints for game and catalogue discovery, product lookup, and price guides through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-javascript-homepage). It does not run a browser or scrape Cardmarket locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Cardmarket or its owners.

## Install

```sh
npm install @crawlora-org/cardmarket
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { CardmarketClient } from "@crawlora-org/cardmarket";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new CardmarketClient({ apiKey });
const result1 = await client.games({});
console.log(result1);
const result2 = await client.catalog({ q: "blue eyes" });
console.log(result2);
```

The client also exports `Client` as an alias for `CardmarketClient`. Operation
methods are available directly in camelCase and through the `cardmarket`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Cardmarket API endpoints

This package exposes each route below as a direct method and through the `cardmarket` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/cardmarket/catalog` | `cardmarket-catalog` | Search Cardmarket product catalogues |
| `GET` | `/cardmarket/catalog/categories` | `cardmarket-catalog-categories` | Discover Cardmarket catalogue categories and expansions |
| `GET` | `/cardmarket/games` | `cardmarket-games` | Discover Cardmarket download game IDs |
| `GET` | `/cardmarket/price-guide` | `cardmarket-price-guide` | Get Cardmarket daily price-guide data |
| `GET` | `/cardmarket/price-guide/categories` | `cardmarket-price-guide-categories` | Discover Cardmarket price-guide categories |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
