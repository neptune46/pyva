#pragma  once

#include <stdio.h>
#include <stdint.h>

#include <windows.h>
#include <D3D11.h>
#include <dxva.h>

#include <vector>

#define PIC_WIDHT_HEVC 320
#define PIC_HEIGHT_HEVC 240

struct DXVADecBuf
{
    D3D11_VIDEO_DECODER_BUFFER_TYPE bufType;
    uint8_t* pBufData;
    UINT bufSize;
};

struct HevcDxvaBufs
{
    HevcDxvaBufs();
    std::vector<uint8_t> pic;
    std::vector<uint8_t> slc;
    std::vector<uint8_t> qm;
    std::vector<uint8_t> bs;
};

struct DXVAData
{
    GUID guidDecoder;
    UINT picWidth;
    UINT picHeight;
    UINT isShortFormat;
    UINT dxvaBufNum;
    DXVADecBuf dxvaDecBuffers[10];
} ;

extern DXVAData decDataHevc;
