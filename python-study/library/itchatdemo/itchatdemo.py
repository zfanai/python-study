#encoding:utf8

import itchat, time
def lc():
    print("Finash Login!")
def ec():
    print("exit")

itchat.auto_login(loginCallback=lc, exitCallback=ec, hotReload=True)
time.sleep(1)
itchat.send_msg("hello world.")
itchat.logout()    #强制退出登录    