#include <Python.h>

void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }
    list = (PyListObject *)p;
    size = PyList_Size(p);
    allocated = list->allocated;
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size, i, max;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);
    str = bytes->ob_sval;
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    max = size + 1 > 10 ? 10 : size + 1;
    printf("  first %ld bytes: ", max);
    for (i = 0; i < max; i++)
        printf("%02hhx%s", str[i], i < max - 1 ? " " : "");
    printf("\n");
}

