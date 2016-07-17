require 'uri'
require 'time'
require 'base64'
require 'net/http'
require 'digest/hmac'

class AmazonQuery

  def initialize(endpoint, key_id, secret_key, parameters = {})
    @uri         = URI.parse(endpoint)
    @host        = @uri.host
    @port        = @uri.port or 443
    @path        = @uri.path.empty? ? '/' : @uri.path
    @secret_key  = secret_key
    @parameters  = parameters.merge({
      'AWSAccessKeyId'   => key_id,
      'SignatureVersion' => 2,
      'SignatureMethod'  => 'HmacSHA256',
      'Timestamp'        => Time.now.utc.iso8601 # '2016-07-17T10:48:48Z'
    })
  end

  def signed_parameters
    sorted_params = @parameters.sort_by { |k,v| k.to_s }
    params = URI.encode_www_form(sorted_params)
    text = ['POST', @host, @path, params].join("\n")
    auth = Digest::HMAC.digest(text, @secret_key, Digest::SHA256)
    signature = Base64.strict_encode64(auth)
    @parameters.merge!({ 'Signature' => signature })
  end

  def request
    http = Net::HTTP.new(@host, @uri.port)
    http.set_debug_output($stderr) if $DEBUG
    http.use_ssl = (@port == 443)
    http.post(@path, URI.encode_www_form(signed_parameters)).body
  end

end
