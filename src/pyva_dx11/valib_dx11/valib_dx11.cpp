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

int createDeviceD3d11()
{
    HRESULT hr = S_OK;
    ID3D11Device *pD3D11Device = NULL;
    ID3D11DeviceContext *pDeviceContext = NULL;
    D3D_FEATURE_LEVEL fl;

    hr = D3D11CreateDevice(nullptr, D3D_DRIVER_TYPE_HARDWARE, nullptr, 0, nullptr, 0,
                           D3D11_SDK_VERSION, &pD3D11Device, &fl, &pDeviceContext);

    FREE_RESOURCE(pD3D11Device);
    FREE_RESOURCE(pDeviceContext);

    return 0;
}
