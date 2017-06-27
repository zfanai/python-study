#encoding:utf8
#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

#SMTPSVR = 'smtp.python.is.cool'
#POP3SVR = 'pop.python.is.cool'

SMTPSVR = '192.168.10.253'
POP3SVR = '192.168.10.253'

origHdrs = ['From: zhouf@medtrum.net',
    'To: zhouf@medtrum.net',
    'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])
#print origMsg
if True:
    sendSvr = SMTP(SMTPSVR)
    #sendSvr.user('zhouf@medtrum.net')
    #sendSvr.pass_('123456')
    sendSvr.login("zhouf@medtrum.net", "Mailpw169181")
    # sendmail的第一个参数 zhouf, zhouf@medtrum.net, zhouf@192.168.10.253
    # 这三种写法都可以，但是如果写成zhoufs之类的，就会报错了。
    errs = sendSvr.sendmail('zhouf@192.168.10.253',
        ('zhouf', ), origMsg)
    sendSvr.quit()
    assert len(errs) == 0, errs
    sleep(10)    # wait for mail to be delivered

recvSvr = POP3(POP3SVR)
recvSvr.user('zhouf@medtrum.net')
recvSvr.pass_('Mailpw169181')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep+1:]
#print recvBody
#assert origBody == recvBody # assert identical
