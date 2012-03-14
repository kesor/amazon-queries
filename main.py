from amazon_query import AmazonQuery

if __name__ == '__main__':
    key_id   = 'AKIAIEXAMPLEEXAMPLE6'
    secret   = 'example+example+example+example+example7'

    endpoint = 'http://ec2.amazonaws.com'
    question = { 'Action': 'DescribeRegions', 'Version': '2012-03-01' }

    endpoint = 'http://elasticloadbalancing.us-east-1.amazonaws.com'
    question = { 'Action': 'DescribeLoadBalancers', 'Version': '2011-11-15' }

    query    = AmazonQuery(endpoint, key_id, secret, question)
    print query.open().read()
