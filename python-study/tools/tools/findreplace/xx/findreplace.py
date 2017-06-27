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
    
    # 目录名称
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
        #    files.extend(subdirs)
        #    files.sort()
        #print subdirs
        for name in files:
            #trace(["name:", name])
            for pattern in patterns:
                #trace(["pattern:", pattern])
                if fnmatch.fnmatch(name, pattern.strip()):# 去除pattern两端的空格
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
    
# @note zhoufan
# 命令行参数 target_dir pattern find replace 
# pattern用分号隔开。
if __name__ == "__main__":
    arg_size = len(sys.argv)
    if arg_size<5:
        print "[Usage]:target_dir pattern find replace "
        sys.exit(0)
    else:
        pass
        target_dir = sys.argv[1]
        pattern = sys.argv[2]
        find = sys.argv[3]
        replace = sys.argv[4]
        if find=="tab":
            find = "\t"
        #
        trace(["find:", find])
        trace(["replace:", replace])
        trace(["pattern:", pattern])
        
    #
    find_replace(target_dir, find, replace, pattern)

