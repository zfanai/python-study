#include <Python.h>
#include <stdio.h>
 
static PyObject* xor_crypt(PyObject* self, PyObject* args)
{
    char* s;
    unsigned int key = 0;
    unsigned int M1 = 0;
    unsigned int IA1 = 0;
    unsigned int IC1 = 0;
    unsigned int size;
     
    PyObject* v;
    char *p;
    unsigned int i = 0;
    unsigned char c;
     
    // �������� s#��ʾ�ַ��������ĳ���, |��ı�ʾ��ѡ����, I��ʾunsigned int
    if(!PyArg_ParseTuple(args, "s#|IIII", &s, &size, &key, &M1, &IA1, &IC1))
        return NULL;
     
    if(key == 0)
        key = 1;
    if(M1 == 0)
        M1 = 1 << 19;
    if(IA1 == 0)
        IA1 = 2 << 20;
    if(IC1 == 0)
        IC1 = 3<< 21;
     
    // v��python�Ŀ��ַ���, ����Ϊsize
    v = PyString_FromStringAndSize((char*)NULL, size);
    if(v == NULL)
        return NULL;
     
    // p�ǰ�python���ַ���vת��Ϊc���ַ���, ��p���в���Ҳ��Ӱ��v
    p = PyString_AS_STRING(v);
    for (i = 0; i < size; i++) {
        c = (unsigned char)s[i];
        key = IA1 * (key % M1) + IC1;
        *p = c ^ (unsigned char)((key >> 20)&0xff);
            p++;
    }
    return v;
}
 
// �����б�, Ҫ������ʼ��������
static PyMethodDef xorcrypt2_methods[] = {
    // ��Ӧpython��ģ����.������ | ��Ӧ��c���� | METH_VARARGS��������python, crypt����cʵ�ֵ� | ����˵��
    {"crypt", (PyCFunction)xor_crypt,  METH_VARARGS, PyDoc_STR("encrypt/decrypt(string) -> generate the string.")},
 
    {NULL, NULL}  // sentinel
};
 
PyDoc_STRVAR(module_doc, "XOR encrypt/decrypt module.");
 
/* ����ʼ��ģ��ʱ, ��������Զ�������, ������Ҫ�̶�Ϊ <init+ģ����> */
PyMODINIT_FUNC initxorcrypt2(void)
{
    PyObject *m;
 
    m = Py_InitModule3("xorcrypt2", xorcrypt2_methods, module_doc);
 
    if (m == NULL)
        return;
 
    PyModule_AddStringConstant(m, "__version__", "0.2");
}