#encoding:gbk

import Tkinter

tcl=Tkinter.Tcl()

#print dir(a)
print type(tcl)

SCRIPTPATH1= "test1.tcl"
SCRIPTPATH2= "test2.tcl"
SCRIPTPATH3= "test3.tcl"

tcl.eval('source '+ SCRIPTPATH1)