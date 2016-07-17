import urllib
# import httplib
# import socket
import ssl
from amazon.query import AmazonQuery

if __name__ == '__main__':
    # key_id   = 'AKIAIEXAMPLEEXAMPLE6'
    # secret   = 'example+example+example+example+example7'

    # endpoint = 'http://ec2.us-west-1.amazonaws.com'
    # question = { 'Version': '2014-02-01', 'Action': 'DescribeInstances' }

    # query = AmazonQuery(endpoint, key_id, secret, question)
    # httplib.debuglevel = 1
    # httplib.HTTPConnection.debuglevel = 1
    # print urllib.FancyURLopener().open(endpoint, query.signed_parameters).read()

    endpoint = 'https://cloudformation.us-east-1.amazonaws.com'
    question = { 'Version': '2010-05-15', 'Action': 'ListStacks' }
    query = AmazonQuery(endpoint, key_id, secret, question)

#    httplib.debuglevel = 1
#    httplib.HTTPConnection.debuglevel = 1
#    socket.ssl.cert_reqs='CERT_NONE'

    ssl_content = ssl.create_default_context()
    ssl_context.verify_mode = ssl.CERT_NONE
    print urllib.urlopen(endpoint, query.signed_parameters, None, ssl_context).read()

#
# other questions to try ...
#

#   endpoint = 'https://cloudformation.us-west-1.amazonaws.com'
#   question = { 'Version': '2010-05-15', 'Action': 'ListStacks' }

#   endpoint = 'http://monitoring.us-west-1.amazonaws.com'
#   question = { 'Version': '2010-08-01', 'Action': 'ListMetrics' }

#   endpoint = 'http://ec2.us-west-1.amazonaws.com'
#   question = { 'Version': '2012-03-01', 'Action': 'DescribeInstances' }
#   question = { 'Version': '2012-03-01', 'Action': 'DescribeReservedInstancesOfferings' }
#   question = { 'Version': '2012-03-01', 'Action': 'DescribeAvailabilityZones' }

#   endpoint = 'http://elasticmapreduce.us-west-1.amazonaws.com'
#   question = { 'Version': '2009-03-31', 'Action': 'DescribeJobFlows' }

#   endpoint = 'http://ec2.us-east-1.amazonaws.com'
#   question = { 'Version': '2012-10-01', 'Action': 'DescribeSpotPriceHistory' }

#   endpoint = 'https://elasticache.us-west-1.amazonaws.com'
#   question = { 'Version': '2011-07-15', 'Action': 'DescribeCacheClusters' }

#   endpoint = 'https://rds.us-west-1.amazonaws.com'
#   question = { 'Version': '2012-01-15', 'Action': 'DescribeDBEngineVersions' }

#   endpoint = 'http://sns.us-west-1.amazonaws.com'
#   question = { 'Version': '2010-03-31', 'Action': 'ListTopics' }

#   endpoint = 'http://sqs.us-west-1.amazonaws.com'
#   question = { 'Version': '2011-10-01', 'Action': 'ListQueues' }

#   endpoint = 'http://sdb.us-west-1.amazonaws.com'
#   question = { 'Version': '2009-04-15', 'Action': 'ListDomains' }

#   endpoint = 'http://s3-us-west-1.amazonaws.com'
#   question = { 'Version': '2006-03-01', 'Action': 'ListAllMyBuckets' }

#   endpoint = 'https://elasticbeanstalk.us-east-1.amazonaws.com'
#   question = { 'Version': '2010-12-01', 'Action': 'ListAvailableSolutionStacks' }

#   endpoint = 'https://iam.amazonaws.com'
#   question = { 'Version': '2010-05-08', 'Action': 'ListUsers' }

#   endpoint = 'http://autoscaling.us-west-1.amazonaws.com'
#   question = { 'Version': '2011-01-01', 'Action': 'DescribeTags' }

#   endpoint = 'https://importexport.amazonaws.com'
#   question = { 'Version': '2010-06-01', 'Action': 'ListJobs' }

#   endpoint = 'https://sts.amazonaws.com'
#   question = { 'Version': '2011-06-15', 'Action': 'GetSessionToken' }

#   endpoint = 'https://iam.amazonaws.com'
#   question = { 'Version': '2010-05-08', 'Action': 'GetUser' }
#   question = { 'Version': '2010-05-08', 'Action': 'ListUserPolicies', 'UserName': 'test_iam' }
#   question = { 'Version': '2010-05-08', 'Action': 'GetUserPolicy', 'UserName': 'test_iam', 'PolicyName': 'ReadOnlyAccess-test_iam-201203291722' }

#   endpoint = 'http://elasticloadbalancing.us-west-1.amazonaws.com'
#   question = { 'Version': '2011-11-15', 'Action': 'DescribeLoadBalancers' }
