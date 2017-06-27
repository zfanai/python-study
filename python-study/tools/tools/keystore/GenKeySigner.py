# coding=gbk

import sys
import os

if 2 == len(sys.argv):
	#print os.path.join(os.getcwd(), sys.argv[1])  
	#print os.path.join(os.getcwd(), sys.argv[2])  
	strJarFileName=os.path.join(os.getcwd(), sys.argv[1]);
	print "输入的签名文件是：%s" % strJarFileName
else:
	print "输入文件路径"
	sys.exit(0)

KEYTOOL_CMD = "keytool";
WORK_DIR = "C:\Users\zhoufan\Projects\JavaWeb\TrumLink\Output\\"
ksfile = "C:/Users/zhoufan/zhoufan.keystore"

OPTION_SIGNER="-keystore "+ ksfile +" "+strJarFileName+" zhoufan " +\
			"-storepass 666666 -keypass 888888";
strSigner = "jarsigner" + " " + OPTION_SIGNER;
print strSigner
os.system(strSigner)