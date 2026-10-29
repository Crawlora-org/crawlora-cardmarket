import { CardmarketClient } from "../src/index.js";

const client = new CardmarketClient({ apiKey: "test-key" });
void client.catalog({});
void client.request("cardmarket-catalog", {});
const streamResponse: Promise<Response> = client.request("cardmarket-catalog", {}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("cardmarket-catalog", {}, { responseType: "stream" });
const directStream: Promise<Response> = client.catalog({}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("cardmarket-catalog", {"kind": "singles", "game_id": 1, "category_id": 1, "expansion_id": 1, "q": "sample", "limit": 1, "offset": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("cardmarket-catalog", {}, { responseType: "text" });
void rawText;


void client.catalog();
void client.request("cardmarket-catalog");
// @ts-expect-error The selected operation requires its documented params.
void client.catalog();
