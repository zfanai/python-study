// Example.cpp
#include <Python.h>

class Numbers
{
public:
    Numbers(int first, double second)
        : m_first( first), m_second(second){}
    double NumMemberMult(void){ return m_first*m_second;}
private:
    int m_first;
    double m_second;
};

static void PyDelNumbers(void *ptr)
{
    Numbers * oldnum = static_cast<Numbers *>(ptr);
    delete oldnum;
    return;
}

PyObject *Example_new_Numbers(PyObject *, PyObject* args)
{
    int arg1;
    double arg2;
    int ok = PyArg_ParseTuple(args,"id",&arg1,&arg2);
    if(!ok) return NULL;
   //动态创建一个新对象

    Numbers *newnum = new Numbers(arg1, arg2);
   //把指针newnum包装成PyCObject对象并返回给解释器

    return PyCObject_FromVoidPtr( newnum, PyDelNumbers);
}
PyObject * Example_Numbers_MemberMult(PyObject *, PyObject* args)
{
    PyObject *pynum = 0;
    int ok = PyArg_ParseTuple( args, "O", &pynum);
    if(!ok) return NULL;
   //把PyCObject转换为void指针

    void * temp = PyCObject_AsVoidPtr(pynum);
   //把void指针转换为一个Numbers对象指针

    Numbers * thisnum = static_cast<Numbers *>(temp);
    //调用函数

    double result = thisnum->NumMemberMult();
    //返回结果

    return Py_BuildValue("d",result);
}

static PyMethodDef Example_methods[] = {
    {"Numbers", Example_new_Numbers, METH_VARARGS},
    {"NumMemberMult", Example_Numbers_MemberMult, METH_VARARGS},
    {NULL, NULL}
};
PyMODINIT_FUNC initExample (void)
{
    Py_InitModule("Example", Example_methods);
}