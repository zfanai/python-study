#!usr/bin/env python
#encoding:utf-8

import base64
import zlib
import sys

def convert(s):
    b = base64.b64decode(s.encode('ascii'))
    return zlib.decompress(b).decode('utf-8')
    #return b

##file site.py
SITE_PY = convert("""
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
YAowyJmdag/AGoXg/wBaZusT
""")

print SITE_PY