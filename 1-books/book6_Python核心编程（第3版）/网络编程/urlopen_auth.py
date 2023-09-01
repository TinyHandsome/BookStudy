from base64 import encodestring
from urllib.parse import urlparse
from urllib.request import HTTPBasicAuthHandler, build_opener, install_opener, Request, urlopen

LOGIN = 'wesley'
PASSWD = 'you will never guess'
URL = 'http://localhost/'
REALM = 'Secure Archive'

def handler_version(url):
    hdlr = HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urlparse(url)[1], LOGIN, PASSWD)
    opener = build_opener(hdlr)
    install_opener(opener)
    return url

def request_version(url):
    req = Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[: -1]
    req.add_header("Authorization", "Basic %s" % b64str)
    return req

for funcType in ('handler', 'request'):
    print('*** Using %s: ' % funcType.upper())
    url = eval('%s_version' % funcType)(URL)
    f = urlopen(url)
    print(f.readline())
    f.close()


