#encoding:utf8

from apnsclient import *
import OpenSSL

OpenSSL.SSL.SSLv3_METHOD = OpenSSL.SSL.TLSv1_METHOD

# 可以使用Session对象来维持连接池
session = Session()
con = session.get_connection("push_sandbox", cert_file="apns_development.pem")

# 发送推送和得到反馈
message = Message(["cdddd063ef3ae28b833aa0321876b412dad9f30ee867964d316b74425edb5570"], alert="My message", badge=10)

# Send the message.
srv = APNs(con)
res = srv.send(message)

# Check failures. Check codes in APNs reference docs.
for token, reason in res.failed.items():
    code, errmsg = reason
    print "Device faled: {0}, reason: {1}".format(token, errmsg)

# Check failures not related to devices.
for code, errmsg in res.errors:
    print "Error: ", errmsg