from amazon.conf import CONF
from amazon.query import AmazonQuery

class AmazonRequest(object):
    def __init__(self, key_id, secret_key, api_name, action):
        assert api_name in CONF, 'Unknown Amazon API: %s' % api_name
        assert 'version' in CONF[api_name], 'Missing API Version: %s' % api_name
        assert 'endpoint' in CONF[api_name], 'Missing API Endpoint: %s' % api_name
        self.key_id = key_id
        self.secret_key = secret_key
        self.endpoint = CONF[api_name]['endpoint']
        self.question = { 'Version': CONF[api_name]['version'], 'Action': action }

    def signed_request(self):
        """ Returns a tuple of (url, body) to fetch API response via HTTP """
        query = AmazonQuery(self.endpoint, self.key_id, self.secret_key, self.question)
        return query.signed_params()
    signed_request = property(signed_request)
