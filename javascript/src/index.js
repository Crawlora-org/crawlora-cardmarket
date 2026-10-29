import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class CardmarketClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-cardmarket-js/0.1.0" });
    this["catalog"] = (...args) => this.request("cardmarket-catalog", ...args);
    this["catalogCategories"] = (...args) => this.request("cardmarket-catalog-categories", ...args);
    this["games"] = (...args) => this.request("cardmarket-games", ...args);
    this["priceGuide"] = (...args) => this.request("cardmarket-price-guide", ...args);
    this["priceGuideCategories"] = (...args) => this.request("cardmarket-price-guide-categories", ...args);
  }
}

export { CardmarketClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default CardmarketClient;
