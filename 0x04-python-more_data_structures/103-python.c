#include "Python.h"
#include <object.h>
#include <listobject.h>
/**
 * print_python_bytes - print basic info about Python lists
 * and Python bytes objects
 * @p: bytes object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element: %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
