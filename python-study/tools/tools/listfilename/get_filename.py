#encoding=gbk

import sys
import os
import fnmatch

def get_filename2(target_dir, output, patterns="*", single_level=False):
	#pass
	#print "filename" 
	print target_dir
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
			for pattern in patterns:
				if fnmatch.fnmatch(name, pattern.strip()):# ȥ��pattern���˵Ŀո�
					#print os.path.join(path, name)
					#print "123"
					#
					abspath = os.path.join(path, name)
					#abspath.replace("\\", "/")
					yield abspath[pos:]
		if single_level:
			break	
	

if __name__ == "__main__":
	arg_size = len(sys.argv)
	if arg_size<3:
		print "[Usage]:get_filename target_dir output_file"
		sys.exit()
		target_dir = "C:/Users/zhoufan/Projects/Java/ChartServer/lib"
		output_file = "C:/Users/zhoufan/Projects/Java/ChartServer/lib/filename_list.txt"		
	else:
		pass
		target_dir = sys.argv[1]
		output_file = sys.argv[2]
		
	#print "sdf"
	#target_dir = "C:/Users/zhoufan/Projects/Java/ChartServer/lib"
	#output_file = "C:/Users/zhoufan/Projects/Java/ChartServer/lib/filename_list.txt"
	
	# ע��yield���÷���ֱ�ӵ��ú�����û��Ч����
	try:
		fileobj = open(output_file, "w")
		for path in get_filename2(target_dir, output_file, patterns="*.jar"):
			path=path.replace("\\", "/")
			print path
			fileobj.write(path+" ")
		fileobj.close()
	except Exception,e:
		print "error"
	#print "dfe"


