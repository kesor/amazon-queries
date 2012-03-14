import datetime
import urllib, urlparse
import hmac, hashlib, base64

class AmazonQuery(object):
    """
    Send a signed request to an Amazon AWS endpoint.
    As described in http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-query-api.html

    :type endpoint: string
    :param endpoint: http://docs.amazonwebservices.com/general/latest/gr/rande.html

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

    def open(self, opener_class=urllib.FancyURLopener):
        self.parameters['Timestamp'] = datetime.datetime.utcnow().isoformat()
        return opener_class().open(self.endpoint, self.encoded_parameters)

    @property
    def encoded_parameters(self):
        params = dict(self.parameters, **{ 'Signature': self.signature })
        return urllib.urlencode(params)

    @property
    def signature(self):
        params = urllib.urlencode( sorted(self.parameters.items()) )
        text = "\n".join(['POST', self.host, self.path, params])
        auth = hmac.new(self.secret_key, msg=text, digestmod=hashlib.sha256)
        return base64.b64encode(auth.digest())
