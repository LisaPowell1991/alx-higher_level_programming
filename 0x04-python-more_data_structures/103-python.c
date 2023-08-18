#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info
 * about Python lists.
 * @p: A PyObject pointer to Python list.
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t index;
	PyObject *element;

	if (PyList_check(p))
	{
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	
	for (index = 0; index < PyList_Size(p); index++)
	{
		element = PySequence_GetItem(p, index);
		printf("Element %lu: %s\n", index, element->ob_type->tp_name);

		if (strcmp(element->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(element);
	}
	}
}

/**
 * print_python_bytes - Prints basic info
 * about Python bytes objects.
 * @p: A PyObject pointer to the Python bytes object
 *
 * Return: Void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size, index;
	char *bytes_str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
	}
	else
	{
		PyBytes_AsStringAndSize(p, &bytes_str, &bytes_size);
		printf(" size: %lu\n", bytes_size);
		printf(" trying string: %s\n", bytes_str);

	printf(" first %lu bytes: ", bytes_size > 10 ? 10 : bytes_size);

	for (index = 0; index < (bytes_size > 10 ? 10 : bytes_size); index++)
		printf("%02hhx%c", bytes_str[index],
				index < (bytes_size > 10 ? 9 : bytes_size - 1)
						? ' ' : '\n');
	}
}

