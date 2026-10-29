use crawlora_cardmarket::{CardmarketGamesParams, Client, ModelCardmarketGamesResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client.cardmarket.games(Default::default()).await?;
    let data: ModelCardmarketGamesResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
