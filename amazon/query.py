import datetime
import urllib, urlparse
import hmac, hashlib, base64

class AmazonQuery(object):
    """
    Send a signed request to an Amazon AWS endpoint.

    :type endpoint: string
    :param endpoint: from http://docs.amazonwebservices.com/general/latest/gr/rande.html

    :type key_id: string
    :param key_id: The Access Key ID for the request sender.

    :type secret_key: string
    :param secret_key: Secret Access Key used for request signature.

    :type parameters: dict
    :param parameters: Optional additional request parameters.
    """

    def __init__(self, endpoint, key_id, secret_key, parameters=dict()):
        parsed = urlparse.urlparse(endpoint)
        self.host = parsed.hostname
        self.path = parsed.path or '/'
        self.endpoint = endpoint
        self.secret_key = secret_key
        self.parameters = dict({
            'AWSAccessKeyId': key_id,
            'SignatureVersion': 2,
            'SignatureMethod': 'HmacSHA256',
        }, **parameters)

    def signed_parameters(self):
        self.parameters['Timestamp'] = datetime.datetime.utcnow().isoformat()
        params = dict(self.parameters, **{ 'Signature': self.signature })
        return urllib.urlencode(params)
    signed_parameters = property(signed_parameters)

    def signature(self):
        params = urllib.urlencode( sorted(self.parameters.items()) )
        text = "\n".join(['POST', self.host, self.path, params])
        auth = hmac.new(self.secret_key, msg=text, digestmod=hashlib.sha256)
        return base64.b64encode(auth.digest())
    signature = property(signature)
