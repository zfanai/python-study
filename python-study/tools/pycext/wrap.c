#include <Python.h>
#include <stdio.h>

int add(int arg1, int arg2)
{
    return arg1 + arg2;
}
//2.add�İ�װ������

static PyObject* wrap_add(PyObject *self, PyObject *args)
{
    //�������Python����ת��ΪC/C++��ʶ�������

    int arg1, arg2;
    //int result;
    
    if(!PyArg_ParseTuple(args, "ii", &arg1, &arg2))
        return NULL;
    
    // ����C/C++�������õ����

    int result = add(arg1,arg2);
    //�ѵõ��Ľ����װ��Python���󣬲�����

    return (PyObject*)Py_BuildValue("i", result);
}
//3.Ϊģ�����PyMethodDef��������

static PyMethodDef wrap_methods[] ={
    {"add", wrap_add, METH_VARARGS},
    {NULL, NULL}
};
//4.����ģ���ʼ������InitModule

PyMODINIT_FUNC initwrap2(void)
{
    Py_InitModule("wrap2", wrap_methods);
}