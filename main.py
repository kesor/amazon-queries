from amazon_query import AmazonQuery
from amazon_xml import AmazonXML

if __name__ == '__main__':
    endpoint = 'https://ec2.amazonaws.com'
    key_id   = 'AKIAIEXAMPLEEXAMPLE6'
    secret   = 'example+example+example+example+example7'
    action   = 'DescribeRegions'
    query    = AmazonQuery(endpoint, key_id, secret, action)
    response = AmazonXML.parse(query.open())
    print 'Root: %s  RequestID: %s' % (response.root, response.request_id,)
