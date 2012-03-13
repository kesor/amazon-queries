import datetime
import urllib
import urlparse
import hmac
import hashlib
import base64

def b64_hmac_sha256(key, text):
    digest = hmac.new(key, msg=text, digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest)

def iso_utcnow():
    return datetime.datetime.utcnow().isoformat()

def encode_utf8_string(value):
    if not isinstance(value, basestring):
        return str(value)
    if isinstance(value, unicode):
        return value.encode('utf-8')
    return value
