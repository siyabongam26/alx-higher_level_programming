#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: ", i);
        
        if (PyBytes_Check(item))
        {
            printf("bytes\n");
            // Print bytes information
            print_python_bytes(item);
        }
        else if (PyFloat_Check(item))
        {
            printf("float\n");
            // Print float information
            print_python_float(item);
        }
        else if (PyLong_Check(item))
        {
            printf("int\n");
            // Add code to print integer information if needed
        }
        else
        {
            printf("unknown\n");
            // Add code for other types as needed
        }
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);
    printf("  first 10 bytes: ");
    
    // Print a maximum of 10 bytes
    for (Py_ssize_t i = 0; i < size && i < 10; i++)
    {
        printf("%02x ", (unsigned char)str[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);

    printf("[.] float object info\n");
    printf("  value: %lf\n", value);
}

int main(void)
{
    Py_Initialize();

    // Example usage
    PyObject *list = PyList_New(3);
    PyList_SetItem(list, 0, PyBytes_FromString("Hello"));
    PyList_SetItem(list, 1, PyFloat_FromDouble(3.14));
    PyList_SetItem(list, 2, PyLong_FromLong(42));

    print_python_list(list);

    Py_DECREF(list);

    Py_Finalize();

    return 0;
}
