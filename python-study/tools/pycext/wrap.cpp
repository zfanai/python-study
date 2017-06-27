#include <Python.h>
#include <stdio.h>

int add(int arg1, int arg2)
{
    return arg1 + arg2;
}
//2.add的包装函数：

static PyObject* wrap_add(PyObject *self, PyObject *args)
{
    //把输入的Python对象转换为C/C++能识别的数据

    int arg1, arg2;
    //int result;
    
    if(!PyArg_ParseTuple(args, "ii", &arg1, &arg2))
        return NULL;
    
    // 调用C/C++函数，得到结果

    int result = add(arg1,arg2);
    //把得到的结果包装成Python对象，并返回

    return (PyObject*)Py_BuildValue("i", result);
}

static PyObject* Windy_dict(PyObject *self, PyObject *args)
{
    //创建列表
    PyObject *newlist = PyList_New(0);
    PyList_Append(newlist, PyString_FromString("first"));
    PyList_Append(newlist, PyString_FromString("second"));
    PyList_Append(newlist, PyString_FromString("third"));
    //返回给解释器
    return newlist;
}

//3.为模块添加PyMethodDef方法数组

static PyMethodDef wrap_methods[] ={
    {"add", wrap_add, METH_VARARGS},
    {"dict", Windy_dict, METH_VARARGS},
    {NULL, NULL}
};
//4.增加模块初始化函数InitModule

PyMODINIT_FUNC initwrap2(void)
{
    Py_InitModule("wrap2", wrap_methods);
}