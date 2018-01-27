#include <stdio.h>
#include <stdint.h>

#include <windows.h>
#include <D3D11.h>
#include <dxva.h>

#include <Python.h>

#define FREE_RESOURCE(res) \
    if (res)               \
    {                      \
        res->Release();    \
        res = NULL;        \
    }

PyObject *createDeviceD3d11(PyObject *)
{
    HRESULT hr = S_OK;
    int32_t ret = 0;
    ID3D11Device *pD3D11Device = NULL;
    ID3D11DeviceContext *pDeviceContext = NULL;
    D3D_FEATURE_LEVEL fl;

    hr = D3D11CreateDevice(nullptr, D3D_DRIVER_TYPE_HARDWARE, nullptr, 0, nullptr, 0,
                           D3D11_SDK_VERSION, &pD3D11Device, &fl, &pDeviceContext);

    ret = (hr == S_OK) ? 0 : 1;

    return PyLong_FromLong(ret);
}

static PyMethodDef pyva_methods[] = {
    // The first property is the name exposed to Python, the second is the C++
    // function name that contains the implementation.
    { "createdevice", (PyCFunction)createDeviceD3d11, METH_NOARGS, nullptr },

    // Terminate the array with an object containing nulls.
    { nullptr, nullptr, 0, nullptr }
};

static PyModuleDef pyva_module = {
    PyModuleDef_HEAD_INIT,
    "pyva",                   // Module name to use with Python import statements
    "Provides video acceleration through d3d11/dxva2 API",  // Module description
    0,
    pyva_methods              // Structure that defines the methods of the module
};

PyMODINIT_FUNC PyInit_pyva() {
    return PyModule_Create(&pyva_module);
}


