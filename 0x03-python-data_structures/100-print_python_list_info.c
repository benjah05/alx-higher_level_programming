#include <Python.h>
#include </usr/include/python3.8/Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: object to struct PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;

	if (p == NULL)
		return;
	print("[*] Size of the Python List = %d\n", Py_SIZE(p));
	print("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		if (item != NULL)
			print("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
