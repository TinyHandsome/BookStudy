from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen


REGEX = compile(br'#([\d,]+) in Books ')
AMZN = 'http://amazon.cn/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}


def getRanking(isbn):
    page = urlopen('%s%s' % (AMZN, isbn))
    data = page.read()
    page.close()
    return str(REGEX.findall(data)[0], 'utf-8')


def _showRanking(isbn):
    print('- %r ranked %s' % (ISBNs[isbn], getRanking(isbn)))


def main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        _showRanking(isbn)


@register
def _atexit():
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
