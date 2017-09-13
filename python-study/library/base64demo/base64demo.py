#encoding:utf8

import base64

#bstr='MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgrWaL6qemBYcow8bKXY5C/xF3bZk1DNwFC1DP/c+Y5BmgCgYIKoZIzj0DAQehRANCAAQ+02pYMofz2mmyY+BIhy+2PMyxFzd/fpdwl0ixsEqNBMdSLHf7uXo1ISuNIEygxsNRROpWqkR5RMlDJa7vS+ZD'
#bstr='eyJzdCI6IjE1MDA4MjU2MDAiLCJldCI6IjE1MDA5MTIwMDAiLCJ0eiI6OH0='
bstr='eyJzdCI6MTUwMDgyNTYwMCwiZXQiOjE1MDA5MTIwMDAsInR6Ijo4fQ=='
a=base64.b64decode(bstr)
print 'a:', a

