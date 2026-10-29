require_relative "lib/crawlora/cardmarket/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-cardmarket"
  spec.version = Crawlora::Cardmarket::VERSION
  spec.summary = "Cardmarket API client for Crawlora (5 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Cardmarket API. Covers game and catalogue discovery, product lookup, and price guides across 5 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cardmarket-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-cardmarket", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-cardmarket/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
