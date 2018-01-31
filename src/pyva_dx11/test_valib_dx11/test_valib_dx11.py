
import uuid
import pyva

guidmap = [
    ("D3D11_DECODER_PROFILE_WMV9_POSTPROC",                                    uuid.UUID(fields=(0x1b81be90, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00c04f2e73c5))),
    ("D3D11_DECODER_PROFILE_WMV9_MOCOMP",                                      uuid.UUID(fields=(0x1b81be91, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00c04f2e73c5))),
    ("D3D11_DECODER_PROFILE_WMV9_IDCT",                                        uuid.UUID(fields=(0x1b81be94, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00c04f2e73c5))),
    ("D3D11_DECODER_PROFILE_VC1_POSTPROC",                                     uuid.UUID(fields=(0x1b81beA0, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00c04f2e73c5))),
    ("D3D11_DECODER_PROFILE_VC1_MOCOMP",                                       uuid.UUID(fields=(0x1b81beA1, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00c04f2e73c5))),
    ("D3D11_DECODER_PROFILE_VC1_IDCT",                                         uuid.UUID(fields=(0x1b81beA2, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00c04f2e73c5))),
    ("D3D11_DECODER_PROFILE_VC1_VLD",                                          uuid.UUID(fields=(0x1b81beA3, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00c04f2e73c5))),
    ("D3D11_DECODER_PROFILE_VC1_D2010",                                        uuid.UUID(fields=(0x1b81beA4, 0xa0c7, 0x11d3, 0xb9, 0x84, 0x00c04f2e73c5))),
    ("D3D11_DECODER_PROFILE_MPEG4PT2_VLD_SIMPLE",                              uuid.UUID(fields=(0xefd64d74, 0xc9e8, 0x41d7, 0xa5, 0xe9, 0xe9b0e39fa319))),
    ("D3D11_DECODER_PROFILE_MPEG4PT2_VLD_ADVSIMPLE_NOGMC",                     uuid.UUID(fields=(0xed418a9f, 0x010d, 0x4eda, 0x9a, 0xe3, 0x9a65358d8d2e))),
    ("D3D11_DECODER_PROFILE_MPEG4PT2_VLD_ADVSIMPLE_GMC",                       uuid.UUID(fields=(0xab998b5b, 0x4258, 0x44a9, 0x9f, 0xeb, 0x94e597a6baae))),
    ("D3D11_DECODER_PROFILE_HEVC_VLD_MAIN",                                    uuid.UUID(fields=(0x5b11d51b, 0x2f4c, 0x4452, 0xbc, 0xc3, 0x09f2a1160cc0))),
    ("D3D11_DECODER_PROFILE_HEVC_VLD_MAIN10",                                  uuid.UUID(fields=(0x107af0e0, 0xef1a, 0x4d19, 0xab, 0xa8, 0x67a163073d13))),
    ("D3D11_DECODER_PROFILE_VP9_VLD_PROFILE0",                                 uuid.UUID(fields=(0x463707f8, 0xa1d0, 0x4585, 0x87, 0x6d, 0x83aa6d60b89e))),
    ("D3D11_DECODER_PROFILE_VP9_VLD_10BIT_PROFILE2",                           uuid.UUID(fields=(0xa4c749ef, 0x6ecf, 0x48aa, 0x84, 0x48, 0x50a7a1165ff7))),
    ("D3D11_DECODER_PROFILE_VP8_VLD",                                          uuid.UUID(fields=(0x90b899ea, 0x3a62, 0x4705, 0x88, 0xb3, 0x8df04b2744e7))),
    ("D3D11_CRYPTO_TYPE_AES128_CTR",                                           uuid.UUID(fields=(0x9b6bd711, 0x4f74, 0x41c9, 0x9e, 0x7b, 0x0be2d7d93b4f))),
    ("D3D11_DECODER_ENCRYPTION_HW_CENC",                                       uuid.UUID(fields=(0x89d6ac4f, 0x09f2, 0x4229, 0xb2, 0xcd, 0x37740a6dfd81))),
    ("D3D11_KEY_EXCHANGE_HW_PROTECTION",                                       uuid.UUID(fields=(0xb1170d8a, 0x628d, 0x4da3, 0xad, 0x3b, 0x82ddb08b4970))),
    ("D3D11_AUTHENTICATED_QUERY_PROTECTION",                                   uuid.UUID(fields=(0xa84eb584, 0xc495, 0x48aa, 0xb9, 0x4d, 0x8bd2d6fbce05))),
    ("D3D11_AUTHENTICATED_QUERY_CHANNEL_TYPE",                                 uuid.UUID(fields=(0xbc1b18a5, 0xb1fb, 0x42ab, 0xbd, 0x94, 0xb5828b4bf7be))),
    ("D3D11_AUTHENTICATED_QUERY_DEVICE_HANDLE",                                uuid.UUID(fields=(0xec1c539d, 0x8cff, 0x4e2a, 0xbc, 0xc4, 0xf5692f99f480))),
    ("D3D11_AUTHENTICATED_QUERY_CRYPTO_SESSION",                               uuid.UUID(fields=(0x2634499e, 0xd018, 0x4d74, 0xac, 0x17, 0x7f724059528d))),
    ("D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_COUNT",     uuid.UUID(fields=(0x0db207b3, 0x9450, 0x46a6, 0x82, 0xde, 0x1b96d44f9cf2))),
    ("D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS",           uuid.UUID(fields=(0x649bbadb, 0xf0f4, 0x4639, 0xa1, 0x5b, 0x24393fc3abac))),
    ("D3D11_AUTHENTICATED_QUERY_UNRESTRICTED_PROTECTED_SHARED_RESOURCE_COUNT", uuid.UUID(fields=(0x012f0bd6, 0xe662, 0x4474, 0xbe, 0xfd, 0xaa53e5143c6d))),
    ("D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT",                              uuid.UUID(fields=(0x2c042b5e, 0x8c07, 0x46d5, 0xaa, 0xbe, 0x8f75cbad4c31))),
    ("D3D11_AUTHENTICATED_QUERY_OUTPUT_ID",                                    uuid.UUID(fields=(0x839ddca3, 0x9b4e, 0x41e4, 0xb0, 0x53, 0x892bd2a11ee7))),
    ("D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_ATTRIBUTES",                     uuid.UUID(fields=(0x6214d9d2, 0x432c, 0x4abb, 0x9f, 0xce, 0x216eea269e3b))),
    ("D3D11_AUTHENTICATED_QUERY_ENCRYPTION_WHEN_ACCESSIBLE_GUID_COUNT",        uuid.UUID(fields=(0xb30f7066, 0x203c, 0x4b07, 0x93, 0xfc, 0xceaafd61241e))),
    ("D3D11_AUTHENTICATED_QUERY_ENCRYPTION_WHEN_ACCESSIBLE_GUID",              uuid.UUID(fields=(0xf83a5958, 0xe986, 0x4bda, 0xbe, 0xb0, 0x411f6a7a01b7))),
    ("D3D11_AUTHENTICATED_QUERY_CURRENT_ENCRYPTION_WHEN_ACCESSIBLE",           uuid.UUID(fields=(0xec1791c7, 0xdad3, 0x4f15, 0x9e, 0xc3, 0xfaa93d60d4f0))),
    ("D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE",                               uuid.UUID(fields=(0x06114bdb, 0x3523, 0x470a, 0x8d, 0xca, 0xfbc2845154f0))),
    ("D3D11_AUTHENTICATED_CONFIGURE_PROTECTION",                               uuid.UUID(fields=(0x50455658, 0x3f47, 0x4362, 0xbf, 0x99, 0xbfdfcde9ed29))),
    ("D3D11_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION",                           uuid.UUID(fields=(0x6346cc54, 0x2cfc, 0x4ad4, 0x82, 0x24, 0xd15837de7700))),
    ("D3D11_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE",                          uuid.UUID(fields=(0x0772d047, 0x1b40, 0x48e8, 0x9c, 0xa6, 0xb5f510de9f01))),
    ("D3D11_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE",               uuid.UUID(fields=(0x41fff286, 0x6ae0, 0x4d43, 0x9d, 0x55, 0xa46e9efd158a))),
    ("D3D11_KEY_EXCHANGE_RSAES_OAEP",                                          uuid.UUID(fields=(0xc1949895, 0xd72a, 0x4a1d, 0x8e, 0x5d, 0xed857d171520))),
]

def getGuidName(x):
    name = ""
    for g in guidmap:
        if (x.int == g[1].int):
            name = guidmap[i][0]
    if name == "":
        name = str(x)
    return name

guids = []
ret = pyva.init()
if ret == 0:
    num = pyva.getDecoderProfileCount()
    for i in range(num):
        guids.append(uuid.UUID(pyva.getDecoderProfile(i)))
    pyva.free()

for guid in guids:
    print(getGuidName(guid))

print("finish")
