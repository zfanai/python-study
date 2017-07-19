#encoding:utf8

import base64

bstr='MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgrWaL6qemBYcow8bKXY5C/xF3bZk1DNwFC1DP/c+Y5BmgCgYIKoZIzj0DAQehRANCAAQ+02pYMofz2mmyY+BIhy+2PMyxFzd/fpdwl0ixsEqNBMdSLHf7uXo1ISuNIEygxsNRROpWqkR5RMlDJa7vS+ZD'
a=base64.b64decode(bstr)
print 'a:', a
