#encoding:gbk
from markdown import markdown

class Debug(object):
    def t(self, *msg):print 'trace:', msg
d=Debug()

def func1():
    allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em', 'i',
                    'strong', 'p']
    #
    value='#h1'
    s=markdown(value, output_format='html')
    d.t('s:', s)
if __name__=='__main__':
    func1()