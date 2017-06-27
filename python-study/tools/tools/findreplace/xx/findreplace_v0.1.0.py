#encoding=gbk

import sys
import os
import fnmatch
import traceback

def trace(obj):
	print "trace:", obj


def _find_replace(filename, find, replace):
	pass
	trace(["_find_replace"])
	try:
		fo=open(filename, "r+")
		buf=fo.read(-1)
		trace(["buf size:", len(buf)])
		#
		#trace(["find,replace:", ord(find), ord(replace)])
		buf2=buf.replace(find, replace)
		fo.truncate(0)
		fo.seek(0,os.SEEK_SET)
		fo.write(buf2)
		#
		fo.close()
	except:
		pass
		excstr=traceback.format_exc()
		print excstr
		#fo.close()

def find_replace(target_dir, find, replace, patterns="*", single_level=False):
	trace(["target_dir:", target_dir])
	patterns = patterns.split(';')
	
	# Ŀ¼����
	#print "dirname:",os.path.dirname(target_dir)
	#print "basename:",os.path.basename(target_dir)
	dirname = os.path.dirname(target_dir)
	pos=len(dirname)
	
	#print os.path.exists(target_dir)
	if not os.path.exists(target_dir):
		print "dir dose not exist"
		raise Exception
	
	
	for path, subdirs, files in os.walk(target_dir):
		#if yield_folders:
		#	files.extend(subdirs)
		#	files.sort()
		#print subdirs
		for name in files:
			#trace(["name:", name])
			for pattern in patterns:
				#trace(["pattern:", pattern])
				if fnmatch.fnmatch(name, pattern.strip()):# ȥ��pattern���˵Ŀո�
					#print os.path.join(path, name)
					#print "123"
					#
					abspath = os.path.join(path, name)
					#abspath.replace("\\", "/")
					#yield abspath[pos:]
					trace(["abspath:", abspath])
					#
					_find_replace(abspath, find, replace)
			#
			#break
		
		if single_level:
			break	
	

if __name__ == "__main__":
	arg_size = len(sys.argv)
	if arg_size<3:
		print "[Usage]:get_filename target_dir output_file"
		#sys.exit()
		#target_dir = "C:/Users/zhoufan/Projects/Java/ChartServer/lib"
		#output_file = "C:/Users/zhoufan/Projects/Java/ChartServer/lib/filename_list.txt"	
		#target_dir = "C:/Users/zhoufan/Desktop/RGraph/demos"
		target_dir = "C:/Users/zhoufan/Desktop/aw"
		
	else:
		pass
		target_dir = sys.argv[1]
		output_file = sys.argv[2]
		
	#print "sdf"
	#target_dir = "C:/Users/zhoufan/Projects/Java/ChartServer/lib"
	#output_file = "C:/Users/zhoufan/Projects/Java/ChartServer/lib/filename_list.txt"
	
	# ע��yield���÷���ֱ�ӵ��ú�����û��Ч����
	#try:
	#	fileobj = open(output_file, "w")
	#	for path in get_filename2(target_dir, output_file, patterns="*.jar"):
	#		path=path.replace("\\", "/")
	#		print path
	#		fileobj.write(path+" ")
	#	fileobj.close()
	#except Exception,e:
	#	print "error"
	#print "dfe"
	#find_replace(target_dir, "http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js", 
	#			"../jquery-1.10.2.min.js","*.html")
	#find_replace(target_dir, "��", " ", "*.txt")
	find_replace(target_dir, "\t", "    ", "*.py")

