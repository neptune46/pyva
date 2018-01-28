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
        res = nullptr;     \
    }

class VideoDecoder
{
public:
    VideoDecoder() {};
    ~VideoDecoder() {};

    HRESULT createDevcice();
    void destroyDevice();

private:
    ID3D11Device* d3d11Device_ = nullptr;
    ID3D11DeviceContext* d3d11DeviceCtx_ = nullptr;
};

HRESULT VideoDecoder::createDevcice()
{
    D3D_FEATURE_LEVEL fl;
    HRESULT hr = D3D11CreateDevice(nullptr, D3D_DRIVER_TYPE_HARDWARE, nullptr, 0, nullptr, 0,
        D3D11_SDK_VERSION, &d3d11Device_, &fl, &d3d11DeviceCtx_);
    return hr;
}

void VideoDecoder::destroyDevice()
{
    FREE_RESOURCE(d3d11Device_);
    FREE_RESOURCE(d3d11DeviceCtx_);
}

VideoDecoder decoderObj;

PyObject *createDeviceD3d11(PyObject *)
{
    HRESULT hr = decoderObj.createDevcice();
    int32_t ret = (hr == S_OK) ? 0 : 1;

    return PyLong_FromLong(ret);
}

PyObject *destroyDeviceD3d11(PyObject *)
{
    decoderObj.destroyDevice();
    return PyLong_FromLong(0);
}

static PyMethodDef pyva_methods[] = {
    // The first property is the name exposed to Python, the second is the C++
    // function name that contains the implementation.
    { "createdevice", (PyCFunction)createDeviceD3d11, METH_NOARGS, nullptr },
    { "destroydevice", (PyCFunction)destroyDeviceD3d11, METH_NOARGS, nullptr },

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


