#encoding:utf8

from smtplib import SMTP as smtp

def send_email(email, seccode):
    s=smtp('smtp.qiye.163.com')
    s.set_debuglevel(0)
    s.login('no-reply@medtrum.com', 'med#No4781')
    text='''From:no-reply@medtrum.com\r\nTo:%s\r\nSubject:No reply\r\n\r\n%s''' % (email, seccode)
    s.sendmail('no-reply@medtrum.com', [email], text)
    s.quit()
    
#def send_hcp_apply_email()    

if __name__=='__main__':
    send_email('no-reply@medtrum', '123456')