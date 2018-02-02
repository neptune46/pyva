#include <stdio.h>
#include <stdint.h>
#include <map>
#include <string>

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

struct GuidMap
{
    GuidMap()
    {
        codecToGuid["h264"] = { 0x1b81be68, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00, 0xc0, 0x4f, 0x2e, 0x73, 0xc5 };
    }

    GUID getGuid(std::string codecName) 
    {
        GUID guid = {};
        std::map<std::string, GUID>::iterator it;

        it = codecToGuid.find(codecName);
        if (it != codecToGuid.end())
            guid = codecToGuid[codecName];

        return guid;
    }

    std::map<std::string, GUID> codecToGuid;

} guidMap;


class VideoDecoder
{
public:
    VideoDecoder() {};
    ~VideoDecoder() {};

    HRESULT init();
    void free();

    uint32_t getVideoDecoderProfileCount();
    HRESULT getVideoDecoderProfile(uint32_t index, GUID* guid);

    HRESULT createVideoDecoder(GUID profile, uint32_t width, uint32_t height, DXGI_FORMAT format = DXGI_FORMAT_NV12);

private:
    ID3D11Device* d3d11Device_ = nullptr;
    ID3D11DeviceContext* d3d11DeviceCtx_ = nullptr;
    ID3D11VideoDevice* d3d11VideoDevice_ = nullptr;
    ID3D11VideoContext *d3d11VideoContext_ = nullptr;

    ID3D11VideoDecoder *videoDecoder_ = nullptr;
};

HRESULT VideoDecoder::init()
{
    HRESULT hr = S_OK;

    D3D_FEATURE_LEVEL fl;
    hr = D3D11CreateDevice(nullptr, D3D_DRIVER_TYPE_HARDWARE, nullptr, 0, nullptr, 0,
        D3D11_SDK_VERSION, &d3d11Device_, &fl, &d3d11DeviceCtx_);

    if (SUCCEEDED(hr))
    {
        hr = d3d11Device_->QueryInterface(&d3d11VideoDevice_);
    }

    if (SUCCEEDED(hr))
    {
        hr = d3d11DeviceCtx_->QueryInterface(&d3d11VideoContext_);
    }

    return hr;
}

void VideoDecoder::free()
{
    FREE_RESOURCE(d3d11Device_);
    FREE_RESOURCE(d3d11DeviceCtx_);
    FREE_RESOURCE(d3d11VideoDevice_);
    FREE_RESOURCE(d3d11VideoContext_);
}

uint32_t VideoDecoder::getVideoDecoderProfileCount()
{
    uint32_t profileCount = 0;

    if (d3d11VideoDevice_)
    {
        profileCount = d3d11VideoDevice_->GetVideoDecoderProfileCount();
    }

    return profileCount;
}

HRESULT VideoDecoder::getVideoDecoderProfile(uint32_t index, GUID* guid)
{
    return d3d11VideoDevice_->GetVideoDecoderProfile(index, guid);
}

HRESULT VideoDecoder::createVideoDecoder(GUID profile, uint32_t width, uint32_t height, DXGI_FORMAT format)
{
    D3D11_VIDEO_DECODER_DESC desc = { 0 };
    desc.Guid = profile;
    desc.SampleWidth = width;
    desc.SampleHeight = height;
    desc.OutputFormat = format;
    D3D11_VIDEO_DECODER_CONFIG config = { 0 };
    config.ConfigBitstreamRaw = 1; // 0: long format; 1: short format

    return d3d11VideoDevice_->CreateVideoDecoder(&desc, &config, &videoDecoder_);
}

VideoDecoder decoderObj;

PyObject *init(PyObject *)
{
    HRESULT hr = decoderObj.init();
    int32_t ret = (hr == S_OK) ? 0 : 1;

    return PyLong_FromLong(ret);
}

PyObject *deinit(PyObject *)
{
    decoderObj.free();
    return PyLong_FromLong(0);
}

PyObject *decoderProfileCount(PyObject *)
{
    uint32_t count = decoderObj.getVideoDecoderProfileCount();
    return PyLong_FromLong(count);
}

PyObject *decoderProfile(PyObject *, PyObject* o)
{
    GUID guid = {};
    uint32_t index = PyLong_AsLong(o);
    HRESULT hr = decoderObj.getVideoDecoderProfile(index, &guid);

    return PyUnicode_FromFormat("%08x%04x%04x%02x%02x%02x%02x%02x%02x%02x%02x", guid.Data1, guid.Data2, guid.Data3,
        guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3], guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);
}

PyObject *createVideoDecoder(PyObject *self, PyObject *args)
{
    uint32_t ret = -1;
    const char* strCodec = nullptr;
    uint32_t width = 0;
    uint32_t height = 0;

    // METH_O: Method 1
    //const char* p2 = PyUnicode_AsUTF8(codec);

    // METH_O: Method 2
    //PyObject* bytes = PyUnicode_AsUTF8String(codec);
    //std::string file_name = PyBytes_AsString(bytes);
    //if (PyErr_Occurred()) 
    //    return NULL;

    // METH_VARARGS: Method 3
    if (!PyArg_ParseTuple(args, "sII", &strCodec, &width, &height))
        return PyLong_FromLong(ret);

    GUID profile = guidMap.getGuid(strCodec);
    HRESULT hr = decoderObj.createVideoDecoder(profile, width, height);
    ret = SUCCEEDED(hr) ? 0 : -1;

    return PyLong_FromLong(ret);
}

static PyMethodDef pyva_methods[] = {
    // The first property is the name exposed to Python, the second is the C++
    // function name that contains the implementation.
    { "init", (PyCFunction)init, METH_NOARGS, nullptr },
    { "free", (PyCFunction)deinit, METH_NOARGS, nullptr },
    { "getDecoderProfileCount", (PyCFunction)decoderProfileCount, METH_NOARGS, nullptr },
    { "getDecoderProfile", (PyCFunction)decoderProfile, METH_O, nullptr },
    { "createDecoder", (PyCFunction)createVideoDecoder, METH_VARARGS, nullptr },

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


