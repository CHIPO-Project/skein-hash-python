#include <Python.h>

#include "skein.h"

static PyObject *skein_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    skein_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    skein_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef SkeinMethods[] = {
    { "getPoWHash", skein_getpowhash, METH_VARARGS, "Returns the proof of work hash using skein hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef SkeinModule = {
    PyModuleDef_HEAD_INIT,
    "skein_hash",
    "...",
    -1,
    SkeinMethods
};

PyMODINIT_FUNC PyInit_skein_hash(void) {
    return PyModule_Create(&SkeinModule);
}

#else

PyMODINIT_FUNC initskein_hash(void) {
    (void) Py_InitModule("skein_hash", SkeinMethods);
}
#endif
