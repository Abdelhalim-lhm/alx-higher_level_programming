#include <Python.h>
/**
 * print_python_list_info - function that prints
 * some basic info about Python lists
 * @p: list to take infos from
 * Return: some Cpython infos
 */
void print_python_list_info(PyObject *p)
{
	int i, size = Py_SIZE(p);
	PyObject *Object;

	printf("[*] Size of the Python List = %d", size);
	printf("[*] Allocated = %ld", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		Object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(Object)->tp_name);
	}
}
