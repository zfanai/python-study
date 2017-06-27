#encoding:utf8

from jinja2 import Environment, PackageLoader

# jinja2test必须是一个模块的名称
env=Environment(loader=PackageLoader('jinja2test','templates'))

class Debug(object):
    def __init__(self):
        pass
    def trace(self,msg):
        print "trace:", msg
    def rprint(self,msg):
        print msg
debug=Debug()

def func1():
    template=env.get_template('tpl1.txt')
    #print template.render(the='variables', go='here')
    template.render(the='variables', go='here')

    template=env.get_template('tpl2.txt')
    #print template.render(the='variables', go='here')
    res=template.render(the='variables', go='here')
    debug.trace(["res:",res]) 
    debug.trace([ "finish"])

def func2():
    template=env.get_template('tpl3.txt')
    res=template.render(title='asdf')
    debug.trace(["res:",res])
    debug.trace([ "finish"])

def func3():
    template=env.get_template('tpl4.txt')
    res=template.render(title='asdf')
    debug.rprint(res)
    debug.trace([ "finish"])

def func4():
    template=env.get_template('tpl5.txt')
    res=template.render(gender=u'男')
    debug.rprint(res)
    debug.trace(["finish"]) 
    
if __name__ == '__main__':
    #func1()
    func4()