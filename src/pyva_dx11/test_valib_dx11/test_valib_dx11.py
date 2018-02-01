
import uuid
import pyva

guidList = [
    ("DXVA2_ModeMPEG2_MoComp",  uuid.UUID('{e6a9f44b-61b0-4563-9ea4-63d2a3c6fe66}')),
    ("DXVA2_ModeMPEG2_IDCT",  uuid.UUID('{bf22ad00-03ea-4690-8077-473346209b7e}')),
    ("DXVA2_ModeMPEG2_VLD",  uuid.UUID('{ee27417f-5e28-4e65-beea-1d26b508adc9}')),
    ("DXVA2_ModeMPEG1_VLD",  uuid.UUID('{6f3ec719-3735-42cc-8063-65cc3cb36616}')),
    ("DXVA2_ModeMPEG2and1_VLD",  uuid.UUID('{86695f12-340e-4f04-9fd3-9253dd327460}')),
    ("DXVA2_ModeH264_A",  uuid.UUID('{1b81be64-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_MoComp_NoFGT",  uuid.UUID('{1b81be64-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_B",  uuid.UUID('{1b81be65-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_MoComp_FGT",  uuid.UUID('{1b81be65-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_C",  uuid.UUID('{1b81be66-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_IDCT_NoFGT",  uuid.UUID('{1b81be66-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_D",  uuid.UUID('{1b81be67-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_IDCT_FGT",  uuid.UUID('{1b81be67-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_E",  uuid.UUID('{1b81be68-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_VLD_NoFGT",  uuid.UUID('{1b81be68-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_F",  uuid.UUID('{1b81be69-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_VLD_FGT",  uuid.UUID('{1b81be69-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeH264_VLD_WithFMOASO_NoFGT",  uuid.UUID('{d5f04ff9-3418-45d8-9561-32a76aae2ddd}')),
    ("DXVA2_ModeH264_VLD_Stereo_Progressive_NoFGT",  uuid.UUID('{d79be8da-0cf1-4c81-b82a-69a4e236f43d}')),
    ("DXVA2_ModeH264_VLD_Stereo_NoFGT",  uuid.UUID('{f9aaccbb-c2b6-4cfc-8779-5707b1760552}')),
    ("DXVA2_ModeH264_VLD_Multiview_NoFGT",  uuid.UUID('{705b9d82-76cf-49d6-b7e6-ac8872db013c}')),
    ("DXVA2_ModeWMV8_A",  uuid.UUID('{1b81be80-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV8_PostProc",  uuid.UUID('{1b81be80-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV8_B",  uuid.UUID('{1b81be81-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV8_MoComp",  uuid.UUID('{1b81be81-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV9_A",  uuid.UUID('{1b81be90-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV9_PostProc",  uuid.UUID('{1b81be90-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV9_B",  uuid.UUID('{1b81be91-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV9_MoComp",  uuid.UUID('{1b81be91-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV9_C",  uuid.UUID('{1b81be94-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeWMV9_IDCT",  uuid.UUID('{1b81be94-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_A",  uuid.UUID('{1b81beA0-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_PostProc",  uuid.UUID('{1b81beA0-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_B",  uuid.UUID('{1b81beA1-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_MoComp",  uuid.UUID('{1b81beA1-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_C",  uuid.UUID('{1b81beA2-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_IDCT",  uuid.UUID('{1b81beA2-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_D",  uuid.UUID('{1b81beA3-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_VLD",  uuid.UUID('{1b81beA3-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_ModeVC1_D2010",  uuid.UUID('{1b81beA4-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_NoEncrypt",  uuid.UUID('{1b81beD0-a0c7-11d3-b984-00c04f2e73c5}')),
    ("DXVA2_VideoProcProgressiveDevice",  uuid.UUID('{5a54a0c9-c7ec-4bd9-8ede-f3c75dc4393b}')),
    ("DXVA2_VideoProcBobDevice",  uuid.UUID('{335aa36e-7884-43a4-9c91-7f87faf3e37e}')),
    ("DXVA2_VideoProcSoftwareDevice",  uuid.UUID('{4553d47f-ee7e-4e3f-9475-dbf1376c4810}')),
    ("DXVA2_ModeMPEG4pt2_VLD_Simple",  uuid.UUID('{efd64d74-c9e8-41d7-a5e9-e9b0e39fa319}')),
    ("DXVA2_ModeMPEG4pt2_VLD_AdvSimple_NoGMC",  uuid.UUID('{ed418a9f-010d-4eda-9ae3-9a65358d8d2e}')),
    ("DXVA2_ModeMPEG4pt2_VLD_AdvSimple_GMC",  uuid.UUID('{ab998b5b-4258-44a9-9feb-94e597a6baae}')),
    ("DXVA2_ModeHEVC_VLD_Main",  uuid.UUID('{5b11d51b-2f4c-4452-bcc3-09f2a1160cc0}')),
    ("DXVA2_ModeHEVC_VLD_Main10",  uuid.UUID('{107af0e0-ef1a-4d19-aba8-67a163073d13}')),
]

def getGuidName(x):
    name = ""
    for g in guidList:
        if (x.int == g[1].int):
            name = g[0]
    if name == "":
        name = str(x)
    return name

def getProfile(profiles):
    guids = []
    ret = pyva.init()
    if ret == 0:
        num = pyva.getDecoderProfileCount()
        for i in range(num):
            guids.append(uuid.UUID(pyva.getDecoderProfile(i)))
        pyva.free()
    
    for guid in guids:
        profiles.append(getGuidName(guid))

if __name__ == "__main__":
    profiles = []
    getProfile(profiles)
    print(profiles)

print("finish")
