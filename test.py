import unittest

from amazon_query import AmazonQuery

class TestAmazonQuery(unittest.TestCase):
    def test_apicall_parameters(self):
        q = AmazonQuery('https://url.com', 'keyid', 'key',
                { 'Action': 'act', 'Version': '2012-03-01', 'foo': 'bar' })
        expected = {
            'Action': 'act',
            'Version': '2012-03-01',
            'AWSAccessKeyId': 'keyid',
            'SignatureVersion': 2,
            'SignatureMethod': 'HmacSHA256',
            'foo': 'bar',
        }
        self.assertDictContainsSubset(expected, q.parameters)
        self.assertDictContainsSubset(q.parameters, expected)

    def test_apicall_secret_key(self):
        q = AmazonQuery('https://url.com', 'keyid', 'key')
        self.assertEquals(q.secret_key, 'key')

if __name__ == '__main__':
    unittest.main()
