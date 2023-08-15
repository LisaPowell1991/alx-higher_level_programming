#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info
 * about Python lists.
 * @p: a pointer
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); i++)
    {
	    PyObject*item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
