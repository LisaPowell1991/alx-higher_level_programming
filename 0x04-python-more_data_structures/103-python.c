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

	if (PyList_Check(p))
	{
		Py_ssize_t list_size = PyObject_Length(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		for (index = 0; index < list_size; index++)
		{
			element = PySequence_GetItem(p, index);
			printf("Element %ld: %s\n", index, element->ob_type->tp_name);

			if (element->ob_type == &PyBytes_Type)
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
		bytes_size = PyObject_Length(p);
		bytes_str = ((PyBytesObject *)p)->ob_sval;

		printf(" size: %ld\n", bytes_size);
		printf(" trying string: %s\n", bytes_str);
		printf(" first %ld bytes: ", bytes_size > 10 ? 10 : bytes_size);

		for (index = 0; index < (bytes_size > 10 ? 10 : bytes_size); index++)
			printf("%02hhx%c", bytes_str[index],
					index < (bytes_size > 10 ? 9 : bytes_size - 1) ? ' ' : '\n');
	}
}
