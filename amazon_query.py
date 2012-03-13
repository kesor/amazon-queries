import datetime
import hmac
import hashlib
import base64
import urllib
import urlparse

from utils import encode_sort_params

class AmazonQuery(object):
    """
    Send a signed request to an Amazon AWS endpoint.
    As described in http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-query-api.html

    :type endpoint: string
    :param endpoint: http://docs.amazonwebservices.com/general/latest/gr/rande.html

    :type access_key_id: string
    :param access_key_id: The Access Key ID for the request sender.

    :type secret_access_key: string
    :param secret_access_key: Secret Access Key used for request signature.

    :type action: string
    :param action: Indicates the action to perform.

    :type parameters: dict
    :param parameters: Optional additional request parameters.
    """

    def __init__(self, endpoint, access_key_id, secret_access_key,
                 action, parameters={}, opener_class=None):
      # http://docs.amazonwebservices.com/AWSEC2/latest/APIReference/Query-Common-Parameters.html
      self.opener_class = opener_class or urllib.FancyURLopener
      self.endpoint = endpoint
      self.secret_access_key = secret_access_key
      self.parameters = {
          'Action': action,
          'Version': '2012-03-01',
          'AWSAccessKeyId': access_key_id,
          'SignatureVersion': 2,
          'SignatureMethod': 'HmacSHA256',
      }
      self.parameters.update( parameters )

    def read(self):
        self.sign_request()
        opener = self.opener_class()
        return opener.open(self.endpoint, self.encoded_parameters)

    @property
    def encoded_parameters(self):
        return urllib.urlencode(self.parameters)

    def _text_request_params(self):
        parsed_url = urlparse.urlparse(self.endpoint)
        verb = 'POST'
        host = parsed_url.hostname
        path = parsed_url.path or '/'
        parameters = encode_sort_params(self.parameters)
        return "%s\n%s\n%s\n%s" % (verb, host, path, parameters,)

    def sign_request(self):
        if 'Signature' in self.parameters:
            del self.parameters['Signature']
        self.parameters['Timestamp'] = datetime.datetime.utcnow().isoformat()
        text = self._text_request_params()
        digest = hmac.new(self.secret_access_key, msg=text, digestmod=hashlib.sha256).digest()
        self.parameters['Signature'] = base64.b64encode(digest)
