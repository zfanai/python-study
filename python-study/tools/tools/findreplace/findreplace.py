#encoding=gbk

import sys
import os
import fnmatch
import traceback

debug_flag=False

def trace(obj):
    print "trace:", obj

def _find_replace(filename, findReplace):
    pass
    #trace(["_find_replace"])
    try:
        fo=open(filename, "r+")
        buf=fo.read(-1)
        size=len(buf)
        #trace(["buf size:", len(buf)])
        #
        #trace(["find,replace:", ord(find), ord(replace)])
        for item in findReplace:
            find,replace=item[0:2]
            buf2=buf.replace(find, replace)
            buf=buf2
            
        #
        if size == len(buf2):return False
        
        if not debug_flag:
            fo.truncate(0)
            fo.seek(0,os.SEEK_SET)
            fo.write(buf2)
        else:
            print buf2
        #
        fo.close()
        return True
    except:
        pass
        excstr=traceback.format_exc()
        print excstr
        #fo.close()
        return False

def find_replace(target_dir, findReplace, patterns="*", single_level=False):
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
    
    proc_count=0
    for path, subdirs, files in os.walk(target_dir):
        #if yield_folders:
        #    files.extend(subdirs)
        #    files.sort()
        #print subdirs
        end_flag=None
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
                    #trace(["abspath:", abspath])
                    #
                    rv=_find_replace(abspath, findReplace)
                    if rv:proc_count+=1
                    if debug_flag and proc_count>=2:end_flag=True
            #
            if end_flag:break
        
        if single_level:break   
        if end_flag:break 
        
# ==========================================================
def replaceTcld(target_dir):
    from GKEYS import GKEYS
    #trace(['dir:', dir(GKEYS)])
    clsAttr=[]
    for k in dir(GKEYS):
        if not k.startswith('_'):
            print k
            clsAttr.append(k)
    # 
    pyFindReplace=[]
    jsFindReplace=[]
    for k in clsAttr:
        find='GKEYS.%s' % k
        replace='\'%s\'' % getattr(GKEYS, k)
        trace(['find,replace:', find, replace])
        pyFindReplace.append([find, replace])
        find='{{appctx.GKEYS.%s}}' % k
        replace='%s' % getattr(GKEYS, k)
        trace(['find,replace:', find, replace])
        jsFindReplace.append([find, replace])
    #
    pyFindReplace.sort(reverse=True)
    #find_replace(target_dir, pyFindReplace, '*.py')
    find_replace(target_dir, jsFindReplace, '*.html')

# ==============================================================
def do_flask_master(target_dir):
    #find_replace(target_dir, [['flktrace', 'flkdebug'], ['flask_trace(', 'trace(\'flask\',']], '*.py') 
    #find_replace(target_dir, [['flkdebug', 'debug']], '*.py')  
    #find_replace(target_dir, [['flktrace', 'debug']], '*.py')
    #find_replace(target_dir, [['debug.sqlalchemy_trace(', 'debug.trace(\'sqlalchemy\', '],
    #                          ['debug.satrace(', 'debug.trace(\'sqlalchemy\', '], 
    #                          ['debug.werkzeug_trace(', 'debug.trace(\'werkzeug_trace\', '] 
    #                          ], '*.py')
    find_replace(target_dir, [['werkzeug_trace', 'werkzeug']], '*.py')

def do_py27(target_dir):
    desc=[['from zftrace import zfdebug', 'from zftrace import debug'],
          ['zfdebug.trace(', 'debug.trace(\'dump\', ']]
    find_replace(target_dir, desc, '*.py')
    
def do_urlfor(target_dir):
    pass
    '''["url_for('help')", "url_for('main.help'"],
      ["url_for('datamanage'", "url_for('main.datamanage'"],
      ["url_for('monitor_other'", "url_for('main.monitor_other'"],
      ["url_for('chart_other'", "url_for('main.chart_other'"],
      ["url_for('report_other'", "url_for('main.report_other'"],
      ["url_for('journal_other'", "url_for('main.journal_other'"],
      ["url_for('record_other'", "url_for('main.record_other'"],
      ["url_for('dataupload'", "url_for('main.dataupload'"],
      ["url_for('export'", "url_for('main.export'"],
      ["url_for('search'", "url_for('main.search'"],
      ["url_for('mibao'", "url_for('main.mibao'"],
      ["url_for('profile'", "url_for('main.profile'"],
      ["url_for('changepwd'", "url_for('main.changepwd'"],
      ["url_for('transfer'", "url_for('main.transfer'"], 
      ['url_for("message"', "url_for('main.message'"],
      ["url_for('patient_profile'", "url_for('main.patient_profile'"], '''
    
    desc=[

    #['url_for("chart_other"', "url_for('main.chart_other'"],
    #["url_for('export_other'", "url_for('main.export_other'"],
    ["url_for('portrait'", "url_for('ajax.portrait'"],
          ]
    find_replace(target_dir, desc, '*.html')    

def do_replace_journaltype(target_dir):
    desc=[
      ["JournalType.BG", "'BG'"],
      ["JournalType.CARB", "'CARB'"],
      ["JournalType.INS", "'INS'"],
      ["JournalType.EXR", "'EXR'"],
      ["JournalType.HEL", "'HEL'"],
      ["JournalType.HBA1C", "'HBA1C'"],
      ["JournalType.DOSE", "'DOSE'"],
      ["JournalType.URINEK", "'URINEK'"],
      ["JournalType.OTR", "'OTR'"],    
          ]
    find_replace(target_dir, desc, '*.py')   
    
def do_replace_user_type(target_dir):
    desc=[
      ["USER_TYPE.DOCTOR", "'D'"],
      ["USER_TYPE.PATIENT", "'P'"],
      ["USER_TYPE.MONITOR", "'M'"],
      ["USER_TYPE.CREATE", "'C'"],
      
          ]
    find_replace(target_dir, desc, '*.py')  
    
# @note zhoufan
# 命令行参数 target_dir pattern find replace 
# pattern用分号隔开。
if __name__ == "__main__":
    arg_size = len(sys.argv)
    if arg_size<2:
        print "[Usage]:target_dir pattern find replace "
        sys.exit(0)
    #
    target_dir = sys.argv[1]
    #replaceTcld(target_dir)
    #do_flask_master(target_dir)
    #do_py27(target_dir)
    #do_urlfor(target_dir)
    #do_replace_journaltype(target_dir)
    do_replace_user_type(target_dir)

