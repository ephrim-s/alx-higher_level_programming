#include <Python.h>

/**
 * print_python_list_info - displays basic info about python
 * @p: pyoject list
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, x;
	PyObject *objct;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (x = 0; x < size; x++)
	{
		printf("Element %d: ", x);

		objct = PyList_GetItem(p, x);
		printf("%s\n", PyTYPE(objct)->tp_name);
	}
}
