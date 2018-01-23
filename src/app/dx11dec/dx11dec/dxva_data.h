#pragma  once

#include <stdio.h>
#include <windows.h>
#include <D3D11.h>
#include <dxva.h>

#define PIC_WIDHT_HEVC 320
#define PIC_HEIGHT_HEVC 240

typedef struct _DXVADecBuf
{
    D3D11_VIDEO_DECODER_BUFFER_TYPE bufType;
    char* pBufData;
    UINT bufSize;
} DXVADecBuf;

typedef struct _DXVAData
{
    GUID guidDecoder;
    UINT picWidth;
    UINT picHeight;
    UINT isShortFormat;
    UINT dxvaBufNum;
    DXVADecBuf dxvaDecBuffers[10];
} DXVAData;

extern DXVAData g_dxvaDataHEVC_Short;
