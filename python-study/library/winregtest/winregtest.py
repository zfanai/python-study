#encoding:gbk

import _winreg

HKEYS = (_winreg.HKEY_USERS,
         _winreg.HKEY_CURRENT_USER,
         _winreg.HKEY_LOCAL_MACHINE,
         _winreg.HKEY_CLASSES_ROOT)
RegError = _winreg.error
RegOpenKeyEx = _winreg.OpenKeyEx
RegEnumKey = _winreg.EnumKey
RegEnumValue = _winreg.EnumValue

class Debug(object):
    def trace(self, obj):
        print 'trace:', obj
debug=Debug()

class Reg:
    """Helper class to read values from the registry
    """
    # @zfn ��cls��Ϊ��һ�������ͱ�ʾ���ຯ���𣨲��ǵģ���
    # r"%s\Setup\VC" % vsbase, "productdir"
    def get_value(cls, path, key):
        for base in HKEYS:
            d = cls.read_values(base, path)
            debug.trace(['d:', d])
            if d and key in d:
                return d[key]
        raise KeyError(key)
    # @zfn ���ڽ�ȫ�ֺ���
    get_value = classmethod(get_value)
    
    # @note ��ȡ�ؼ������ơ�
    def read_keys(cls, base, key):
        """Return list of registry keys."""
        try:
            handle = RegOpenKeyEx(base, key)
        except RegError:
            return None
        L = []
        i = 0
        while True:
            try:
                k = RegEnumKey(handle, i)
            except RegError:
                break
            L.append(k)
            i += 1
        return L
    read_keys = classmethod(read_keys)
    
    # @zfn cls.read_values(base, path)
    # ����Ĳ���key��ʵ��path
    def read_values(cls, base, key):
        """Return dict of registry keys and values.

        All names are converted to lowercase.
        """
        try:
            handle = RegOpenKeyEx(base, key)
        except RegError:
            return None
        d = {}
        i = 0
        while True:
            try:
                # @note ö�����ע������������м�-ֵ�ԡ�
                # 
                name, value, type = RegEnumValue(handle, i)
            except RegError:
                break
            name = name.lower()
            d[cls.convert_mbcs(name)] = cls.convert_mbcs(value)
            i += 1
        return d
    read_values = classmethod(read_values)

    def convert_mbcs(s):
        dec = getattr(s, "decode", None)
        if dec is not None:
            try:
                s = dec("mbcs")
            except UnicodeError:
                pass
        return s
    convert_mbcs = staticmethod(convert_mbcs)    

def func1():
    
    vsbase=r"Software\Microsoft\VisualStudio\10.0"
    productdir = Reg.get_value(r"%s\Setup\VC" % vsbase, "productdir")
    debug.trace(['productdir:', productdir])
   
if __name__=='__main__':
    func1()