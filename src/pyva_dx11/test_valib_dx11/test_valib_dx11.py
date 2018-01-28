
import pyva

guids = []
ret = pyva.init()
if ret == 0:
    num = pyva.getDecoderProfileCount()
    for i in range(num):
        guids.append (pyva.getDecoderProfile(i))
    pyva.free()

for guid in guids:
    print(guid)
