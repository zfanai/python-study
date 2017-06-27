#!/user/bin/python
# -*- coding: GB2312 -*-
# Filename: cleanpyc.py
# Date:2011-03-26

import os
import fnmatch
import sys
import shutil

def trace(obj):
	print "trace:", obj

def clean_files(root, bnamelist=[], patterns='', single_level=False, yield_folders=False):
	"""
	root: 需要遍历的目录
	patterns： 需要查找的文件，以；为分割的字符串
	single_level: 是否只遍历单层目录，默认为否
	yield_folders: 是否包含目录本身，默认为否
	"""
	patterns = patterns.split(';')
	for path, subdirs, files in os.walk(root):
		if yield_folders:
			files.extend(subdirs)
			files.sort()
			
		#trace(["=================================================="])
		#trace(["path,basename:", path, os.path.basename(path)])
		bname = os.path.basename(path)
		#if bname=="Debug" or bname=="Release" or bname=="ipch":
		if bname in bnamelist:
			#yield os.path.join(path, name)
			yield "d", path
			continue
		# 		
		for name in files:
			for pattern in patterns:
				if fnmatch.fnmatch(name, pattern.strip()):# 去除pattern两端的空格
					yield "f", os.path.join(path, name)
		if single_level:
			break


if __name__ == '__main__':
	if 4 == len(sys.argv):
		#print os.path.join(os.getcwd(), sys.argv[1])
		print "参数检查正确"
	else:
		print "输入目录"
		sys.exit(0)

	directory = sys.argv[1]
	bnamelist= sys.argv[2].split(";")
	patterns=sys.argv[3]
	trace(["bnamelist", bnamelist])
	trace(["patterns", patterns])
	
	for t,p in clean_files(directory, bnamelist, patterns):
		print t,p
		if t=="f":
			os.remove(p)
		elif t=="d":
			shutil.rmtree(p, ignore_errors=True)
		trace(["delete path:", p])
	