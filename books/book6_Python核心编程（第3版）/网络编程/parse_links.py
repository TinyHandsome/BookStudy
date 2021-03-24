from html.parser import HTMLParser
from io import StringIO
from urllib import urlopen
from urllib.urlparse import urljoin

from bs4 import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuilders

URLs = (
    'http://python.org',
    'http://google.com',
)

def output(x):
    print('\n'.join(sorted(set(x))))

def simpleBS(url, f):
    # simpleBS() - use BeautifulSoup to parse all tags to get anchors output
    output(urljoin(url, x['href']) for x in BeautifulSoup(f, parse_only=SoupStrainer('a')))

def fasterBS(url, f):
    # fasterBS() - use BeautifulSoup to parse only anchor tags
    output(urljoin(url, x['href']) for x in BeautifulSoup(f, parse_only=SoupStrainer('a')))

def htmlparser(url, f):
    # htmlparser() - user HTMLParser to parse anchor tags
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])

    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)

