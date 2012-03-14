from amazon_query import AmazonQuery

if __name__ == '__main__':
    key_id   = 'AKIAIEXAMPLEEXAMPLE6'
    secret   = 'example+example+example+example+example7'

    endpoint = 'https://cloudformation.us-west-1.amazonaws.com'
    question = { 'Version': '2010-05-15', 'Action': 'ListStacks' }

    endpoint = 'http://monitoring.us-west-1.amazonaws.com'
    question = { 'Version': '2010-08-01', 'Action': 'ListMetrics' }

    endpoint = 'http://ec2.us-west-1.amazonaws.com'
    question = { 'Version': '2012-03-01', 'Action': 'DescribeInstances' }

    endpoint = 'http://elasticmapreduce.us-west-1.amazonaws.com'
    question = { 'Version': '2009-03-31', 'Action': 'DescribeJobFlows' }

    endpoint = 'https://elasticache.us-west-1.amazonaws.com'
    question = { 'Version': '2011-07-15', 'Action': 'DescribeCacheClusters' }

    endpoint = 'https://rds.us-west-1.amazonaws.com'
    question = { 'Version': '2012-01-15', 'Action': 'DescribeDBEngineVersions' }

    endpoint = 'http://sdb.us-west-1.amazonaws.com'
    question = { 'Version': '2009-04-15', 'Action': 'ListDomains' }

    endpoint = 'http://sns.us-west-1.amazonaws.com'
    question = { 'Version': '2010-03-31', 'Action': 'ListTopics' }

    endpoint = 'http://sqs.us-west-1.amazonaws.com'
    question = { 'Version': '2011-10-01', 'Action': 'ListQueues' }

    endpoint = 'http://s3-us-west-1.amazonaws.com'
    question = { 'Version': '2006-03-01', 'Action': 'ListAllMyBuckets' }

    endpoint = 'http://autoscaling.us-west-1.amazonaws.com'
    question = { 'Version': '2011-01-01', 'Action': 'DescribeTags' }

    endpoint = 'https://elasticbeanstalk.us-east-1.amazonaws.com'
    question = { 'Version': '2010-12-01', 'Action': 'ListAvailableSolutionStacks' }

    endpoint = 'https://iam.amazonaws.com'
    question = { 'Version': '2010-05-08', 'Action': 'ListUsers' }

    endpoint = 'https://importexport.amazonaws.com'
    question = { 'Version': '2010-06-01', 'Action': 'ListJobs' }

    endpoint = 'https://sts.amazonaws.com'
    question = { 'Version': '2011-06-15', 'Action': 'GetSessionToken' }

    endpoint = 'http://elasticloadbalancing.us-west-1.amazonaws.com'
    question = { 'Action': 'DescribeLoadBalancers', 'Version': '2011-11-15' }

    query    = AmazonQuery(endpoint, key_id, secret, question)
    print query.open().read()
