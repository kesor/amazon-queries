import datetime
import urllib
import urlparse
import hmac
import hashlib
import base64

def b64_hmac_sha256(key, text):
    digest = hmac.new(key, msg=text, digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest)

def parse_host_path(url):
    parsed = urlparse.urlparse(url)
    host = parsed.hostname
    path = parsed.path or '/'
    return (host, path)

def iso_utcnow():
    return datetime.datetime.utcnow().isoformat()

def encode_utf8_string(value):
    if not isinstance(value, basestring):
        return str(value)
    if isinstance(value, unicode):
        return value.encode('utf-8')
    return value

def safe_quote_param(key, value):
    val = encode_utf8_string(value)
    return urllib.quote(key, safe='') + '=' + urllib.quote(val, safe='-_~')

def encode_sort_params(parameters):
    keys = parameters.keys()
    keys.sort()
    quoted = [ safe_quote_param(key, parameters[key]) for key in keys ]
    return '&'.join(quoted)