#! /usr/bin/env python
import sys, urllib, re, os

import requests

from html2text import html2text

html2txtUrl = 'https://www.w3.org/services/html2txt?url='

def url2text(url):
    url = html2txtUrl + urllib.quote_plus(url)

    r = requests.get(url)

    return remove_refs(r.content)

def url2md(url):
    #dumb that this works better, but hey
    os.system('html2text/html2text.py --ignore-links --ignore-images ' + url + ' > tmp')
    f = open('tmp', 'r')
    return f.read()

def remove_refs(text):

    inline_refs = re.compile('\[\d+\]\shttp.+\n')
    no_inlines = re.sub(inline_refs, '', text)
    refs = re.compile('\[\d+\]')
    no_refs = re.sub(refs, '', no_inlines)
    return no_refs

def main():
    print url2text(sys.argv[1])
    print url2md(sys.argv[1])
    return 
 
if __name__ == '__main__':
    main()
