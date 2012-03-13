import datetime
import urllib

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