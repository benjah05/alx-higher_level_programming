#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <listobject.h>
/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: object to struct PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size, i;

	if (!PyList_Check(p))
		return;
	size = PyList_Size(p);
	print("[*] Size of the Python List = %zd\n", size);
	print("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		if (item != NULL)
			print("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
