CONF = dict(
    cloudwatch = {
        'endpoint': 'https://monitoring.$region.amazonaws.com',
        'version':  '2010-08-10',
    },
    cloudformation = {
        'endpoint': 'https://cloudformation.$region.amazonaws.com',
        'version':  '2010-05-15',
    },
    ec2 = {
        'endpoint': 'http://ec2.$region.amazonaws.com',
        'version':  '2012-03-01',
    },
    emr = {
        'endpoint': 'http://elasticmapreduce.$region.amazonaws.com',
        'version':  '2009-03-31',
    },
    elasticache = {
        'endpoint': 'https://elasticache.$region.amazonaws.com',
        'version':  '2011-07-15',
    },
    rds = {
        'endpoint': 'https://rds.$region.amazonaws.com',
        'version': '2012-01-15',
    },
    sdb = {
        'endpoint': 'https://sdb.$region.amazonaws.com',
        'version':  '2009-04-15',
    },
    sns = {
        'endpoint': 'https://sns.$region.amazonaws.com',
        'version':  '2010-03-31',
    },
    sqs = {
        'endpoint': 'https://sqs.$region.amazonaws.com',
        'version':  '2011-10-01',
    },
    autoscaling = {
        'endpoint': 'https://autoscaling.$region.amazonaws.com',
        'version':  '2011-01-01',
    },
    elasticbeanstalk = {
        'endpoint': 'https://elasticbeanstalk.$region.amazonaws.com',
        'version':  '2010-12-01',
    },
    iam = {
        'endpoint': 'https://iam.amazonaws.com',
        'version':  '2010-05-08',
    },
    importexport = {
        'endpoint': 'https://importexport.amazonaws.com',
        'version':  '2010-06-01',
    },
    sts = {
        'endpoint': 'https://sts.amazonaws.com',
        'version':  '2011-06-15',
    },
    elb = {
        'endpoint': 'https://elasticloadbalancing.$region.amazonaws.com',
        'version':  '2011-11-15',
    },
)
