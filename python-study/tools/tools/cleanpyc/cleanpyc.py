#!/user/bin/python
# -*- coding: gbk -*-
# Filename: cleanpyc.py
# Date:2011-03-26

import os
import fnmatch
import sys

def clearpyc(root, patterns='*',single_level=False, yield_folders=False):
	"""
	root: ��Ҫ������Ŀ¼
	patterns�� ��Ҫ���ҵ��ļ����ԣ�Ϊ�ָ���ַ���
	single_level: �Ƿ�ֻ��������Ŀ¼��Ĭ��Ϊ��
	yield_folders: �Ƿ����Ŀ¼����Ĭ��Ϊ��
	"""
	patterns = patterns.split(';')
	for path, subdirs, files in os.walk(root):
		if yield_folders:
			files.extend(subdirs)
			files.sort()
		for name in files:
			for pattern in patterns:
				if fnmatch.fnmatch(name, pattern.strip()):# ȥ��pattern���˵Ŀո�
					yield os.path.join(path, name)
		if single_level:
			break


if __name__ == '__main__':
	if 2 == len(sys.argv):
		#print os.path.join(os.getcwd(), sys.argv[1])
		print "���������ȷ"
	else:
		print "����Ŀ¼"
		sys.exit(0)

	directory = sys.argv[1]
	
	for path in clearpyc(directory,'*.pyc'):
		print path
		os.remove(path)			