#!usr/bin/env python
#encoding:utf-8

from htmllib import HTMLParser;
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO

def main():
    parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
    parser.feed(open("test.html").read())
    parser.close()
    #print parser.anchorlist
    for url in parser.anchorlist:
        print url
if __name__ == '__main__':
    main()
