# coding=gbk

import sys
import os

KEYTOOL_CMD = "keytool";
#WORK_DIR = "C:\Users\zhoufan\Projects\JavaWeb\TrumLink\Output\\"
WORK_DIR = os.getcwd();
OPTION_CER="-export -keystore "+WORK_DIR+os.path.sep+"zhoufan.keystore -alias zhoufan -file zhoufan.cert " +\
			"-storepass 666666 -keypass 888888";
strGenCer = KEYTOOL_CMD + " " + OPTION_CER;
print strGenCer
os.system(strGenCer)