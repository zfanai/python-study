#encoding:utf8
import sys
import os

'''
['F_OK', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'UserDict', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_copy_reg', '_execvpe', '_exists', '_exit', '_get_exports_list', '_make_stat_result', '_make_statvfs_result', '_pickle_stat_result', '_pickle_statvfs_result', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'curdir', 'defpath', 'devnull', 'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fstat', 'fsync', 'getcwd', 'getcwdu', 'getenv', 'getpid', 'isatty', 'kill', 'linesep', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'popen2', 'popen3', 'popen4', 'putenv', 'read', 'remove', 'removedirs', 'rename', 'renames', 'rmdir', 'sep', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'startfile', 'stat', 'stat_float_times', 'stat_result', 'statvfs_result', 'strerror', 'sys', 'system', 'tempnam', 'times', 'tmpfile', 'tmpnam', 'umask', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'walk', 'write']
'''

'''
查找某个命令具体在哪个目录。
'''

class Debug(object):
    def trace(self,obj):
        print 'trace:',obj
debug=Debug()

def func1():
    debug.trace(['attr of os:', dir(os)])
def osenviron():
    for k,v in os.environ.items():
        debug.trace(['k,v:', k, v])

def environpath(name):
    path=os.environ['PATH']
    path=path.split(';')
    for p in path:
        #debug.trace(['p:', p])
        for ext in ['.bat', '.exe']:
            fn=os.path.join(p, name+'%s'%ext)
            #debug.trace(['tclsh:', fn])
            if os.path.exists(fn):
                debug.trace(['%s:'%name, fn])

def pathexist():
    tmp=os.path.exists('123.*')
    debug.trace(['tmp:', tmp])
#
if __name__=='__main__':
    if len(sys.argv)<2:
        debug.trace(["args wrong!"])
        sys.exit(1)
    # 
    name=sys.argv[1]
    environpath(name)