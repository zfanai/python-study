# coding=gbk

import sys
import os

KEYTOOL_CMD = "keytool";
#WORK_DIR = "C:\Users\zhoufan\Projects\JavaWeb\TrumLink\Output\\"
WORK_DIR = os.getcwd();

print WORK_DIR;

OPTION = "-genkey -alias zhoufan -keypass 888888 "+\
		"-keyalg RSA -keysize 1024 -validity 365 "+\
		"-keystore  "+WORK_DIR+os.path.sep+"zhoufan.keystore "+\
		"-storepass 666666 "+\
		"-dname \"CN=�ܷ�, OU=Medtrum, O=Medtrum, L=�ֶ�, ST=�Ϻ�,C=cn\"";
		
strGenKey = KEYTOOL_CMD + " " + OPTION;
print strGenKey
os.system(strGenKey)
