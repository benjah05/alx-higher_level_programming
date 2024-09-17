#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: object to struct PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size = Py_SIZE(p), i;

	if (!PyList_Check(p))
		return;
	print("[*] Size of the Python List = %zd\n", size);
	print("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		item = PyList_GetItem(p, i);
		if (item != NULL)
			print("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}
