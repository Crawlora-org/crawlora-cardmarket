import os

from crawlora_cardmarket import CardmarketClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with CardmarketClient(api_key=api_key) as client:
    games = client.games()
    print('games', games)
    catalog = client.catalog(q='blue eyes')
    print('catalog', catalog)
