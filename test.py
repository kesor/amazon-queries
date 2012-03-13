import unittest

from amazon_query import AmazonQuery
from utils import encode_sort_params

class TestUtils(unittest.TestCase):
    def test_encode_sort_params(self):
        params = { u'Xy': 'a+b-s_c~d', 'A': 'xy% asd $3#', 'a': 'last' }
        expected = 'A=xy%25%20asd%20%243%23&Xy=a%2Bb-s_c~d&a=last'
        self.assertEquals(expected, encode_sort_params(params))

class TestAmazonQuery(unittest.TestCase):
    def test_apicall_parameters(self):
        q = AmazonQuery('https://url.com', 'keyid', 'key', 'act', { 'foo': 'bar' })
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
        q = AmazonQuery('https://url.com', 'keyid', 'key', 'act', { 'foo': 'bar' })
        self.assertEquals(q.secret_access_key, 'key')

if __name__ == '__main__':
    unittest.main()