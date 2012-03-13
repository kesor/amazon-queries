from amazon_query import AmazonQuery

if __name__ == '__main__':
    endpoint = 'https://ec2.amazonaws.com'
    key_id   = 'AKIAIEXAMPLEEXAMPLE6'
    secret   = 'example+example+example+example+example7'
    action   = 'DescribeRegions'
    query    = AmazonQuery(endpoint, key_id, secret, action)
    print ''.join( query.read() )
