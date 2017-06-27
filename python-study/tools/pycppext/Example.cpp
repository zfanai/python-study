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
   //��̬����һ���¶���

    Numbers *newnum = new Numbers(arg1, arg2);
   //��ָ��newnum��װ��PyCObject���󲢷��ظ�������

    return PyCObject_FromVoidPtr( newnum, PyDelNumbers);
}
PyObject * Example_Numbers_MemberMult(PyObject *, PyObject* args)
{
    PyObject *pynum = 0;
    int ok = PyArg_ParseTuple( args, "O", &pynum);
    if(!ok) return NULL;
   //��PyCObjectת��Ϊvoidָ��

    void * temp = PyCObject_AsVoidPtr(pynum);
   //��voidָ��ת��Ϊһ��Numbers����ָ��

    Numbers * thisnum = static_cast<Numbers *>(temp);
    //���ú���

    double result = thisnum->NumMemberMult();
    //���ؽ��

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