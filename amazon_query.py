import urllib
import urlparse

from utils import iso_utcnow, b64_hmac_sha256

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
                 action, parameters={}, path='/', opener_class=None):
      # http://docs.amazonwebservices.com/AWSEC2/latest/APIReference/Query-Common-Parameters.html
      self.opener_class = opener_class or urllib.FancyURLopener
      self.endpoint = endpoint
      self.path = path
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
        self.parameters['Timestamp'] = iso_utcnow()
        self.sign_request()
        opener = self.opener_class()
        return opener.open(self.endpoint, self.encoded_parameters)

    @property
    def encoded_parameters(self):
        params = dict(self.parameters, **{ 'Signature': self.signature })
        return urllib.urlencode(params)

    def sign_request(self):
        # sorted params -- not strictly per amazon docs, but close
        params = urllib.urlencode( sorted(self.parameters.items()) )
        host = urlparse.urlparse(self.endpoint).hostname
        text = "\n".join(['POST', host, self.path, params])
        self.signature = b64_hmac_sha256(self.secret_access_key, text)
