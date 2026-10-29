require "json"
require "net/http"
require "uri"

module Crawlora
  module Cardmarket
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"cardmarket-catalog": {"bodyParam": null, "bodyRequired": false, "id": "cardmarket-catalog", "method": "GET", "params": [{"description": "Catalogue file type; defaults to singles", "enum": ["singles", "nonsingles", "accessories"], "in": "query", "name": "kind", "type": "string", "x-example": "singles"}, {"description": "Required for singles/nonsingles; omit for global accessories", "enum": [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "in": "query", "name": "game_id", "type": "integer", "x-example": 6}, {"description": "Optional current category ID; discover the full set with /cardmarket/catalog/categories", "in": "query", "name": "category_id", "type": "integer", "x-example": 51}, {"description": "Optional current expansion ID; discover the full set with /cardmarket/catalog/categories", "in": "query", "name": "expansion_id", "type": "integer", "x-example": 1585}, {"description": "Optional case-insensitive local product-name substring, up to 200 characters", "in": "query", "name": "q", "type": "string", "x-example": "pikachu"}, {"description": "Rows per page, 1-500; defaults to 100", "in": "query", "name": "limit", "type": "integer", "x-example": 100}, {"description": "Zero-based offset; defaults to 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/cardmarket/catalog", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["singles", "nonsingles", "accessories"], "in": "query", "name": "kind", "type": "string"}, {"enum": ["1", "2", "3", "5", "6", "7", "8", "9", "10", "11", "12", "13", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"], "in": "query", "name": "game_id", "type": "integer"}, {"in": "query", "name": "category_id", "type": "integer"}, {"in": "query", "name": "expansion_id", "type": "integer"}, {"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "cardmarket-catalog-categories": {"bodyParam": null, "bodyRequired": false, "id": "cardmarket-catalog-categories", "method": "GET", "params": [{"description": "Catalogue file type; defaults to singles", "enum": ["singles", "nonsingles", "accessories"], "in": "query", "name": "kind", "type": "string", "x-example": "singles"}, {"description": "Required for singles/nonsingles; omit for global accessories", "enum": [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "in": "query", "name": "game_id", "type": "integer", "x-example": 6}], "path": "/cardmarket/catalog/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["singles", "nonsingles", "accessories"], "in": "query", "name": "kind", "type": "string"}, {"enum": ["1", "2", "3", "5", "6", "7", "8", "9", "10", "11", "12", "13", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"], "in": "query", "name": "game_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "cardmarket-games": {"bodyParam": null, "bodyRequired": false, "id": "cardmarket-games", "method": "GET", "params": [], "path": "/cardmarket/games", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cardmarket-price-guide": {"bodyParam": null, "bodyRequired": false, "id": "cardmarket-price-guide", "method": "GET", "params": [{"description": "Price-guide dataset; defaults to game", "enum": ["game", "accessories"], "in": "query", "name": "kind", "type": "string", "x-example": "game"}, {"description": "Required when kind=game; omit for global accessories", "enum": [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], "in": "query", "name": "game_id", "type": "integer", "x-example": 6}, {"description": "Optional category ID; discover the full set with /cardmarket/price-guide/categories", "in": "query", "name": "category_id", "type": "integer", "x-example": 52}, {"description": "Optional exact product ID filter", "in": "query", "name": "product_id", "type": "integer", "x-example": 271439}, {"description": "Rows per page, 1-500; defaults to 100", "in": "query", "name": "limit", "type": "integer", "x-example": 100}, {"description": "Zero-based offset; defaults to 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/cardmarket/price-guide", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["game", "accessories"], "in": "query", "name": "kind", "type": "string"}, {"enum": ["1", "2", "3", "5", "6", "7", "8", "9", "10", "11", "12", "13", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"], "in": "query", "name": "game_id", "type": "integer"}, {"in": "query", "name": "category_id", "type": "integer"}, {"in": "query", "name": "product_id", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "cardmarket-price-guide-categories": {"bodyParam": null, "bodyRequired": false, "id": "cardmarket-price-guide-categories", "method": "GET", "params": [{"description": "Price-guide dataset; defaults to game", "enum": ["game", "accessories"], "in": "query", "name": "kind", "type": "string", "x-example": "game"}, {"description": "Required when kind=game; omit for global accessories", "enum": [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], "in": "query", "name": "game_id", "type": "integer", "x-example": 6}], "path": "/cardmarket/price-guide/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["game", "accessories"], "in": "query", "name": "kind", "type": "string"}, {"enum": ["1", "2", "3", "5", "6", "7", "8", "9", "10", "11", "12", "13", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"], "in": "query", "name": "game_id", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["cardmarket-catalog", "cardmarket-catalog-categories", "cardmarket-games", "cardmarket-price-guide", "cardmarket-price-guide-categories"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-cardmarket-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('catalog') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cardmarket-catalog', params, response_type: response_type)
      end
      define_method('catalog_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cardmarket-catalog-categories', params, response_type: response_type)
      end
      define_method('games') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cardmarket-games', params, response_type: response_type)
      end
      define_method('price_guide') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cardmarket-price-guide', params, response_type: response_type)
      end
      define_method('price_guide_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cardmarket-price-guide-categories', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
