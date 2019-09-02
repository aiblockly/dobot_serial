import numpy as np
import struct

relative=0
absolute=1

def SetCPCmd_code(isQueued,cpCmd):
    UID0061=np.array([170,170],dtype="uint8")
    Constant_UID07FF=""
    UID041A=np.concatenate(([True],[isQueued]))
    UID0A18=cpCmd[4]
    UID07D7=cpCmd[3]
    UID0843=cpCmd[2]
    UID0855=cpCmd[1]
    UID0867=cpCmd[0]
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID0A51=struct.pack(">f",UID07D7)
    UID0A64=struct.pack(">f",UID0843)
    UID0A69=struct.pack(">f",UID0855)
    UID0A6C=struct.pack(">B",UID0867)
    UID0A4E=struct.pack(">f",UID0A18)
    UID0200=int(UID0229)&0xff
    UID0A00=UID0A4E+UID0A51+UID0A64+UID0A69+UID0A6C
    UID031E=np.fromstring(UID0A00,dtype="uint8")
    UID031B=UID031E[: :-1]
    UID0110=len(UID031B)
    UID01CF=np.concatenate(([91],[UID0200],UID031B))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def SetCPCmd_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID0071=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    UID0095=UID0071[: :-1]
    CheckCorrect=UID02CD
    try:
        UID01C1=int(np.fromstring((np.array(UID0095,dtype=">u1").tobytes()),dtype=">u8")[0])
    except:
        UID01C1=0
    queuedCmdIndex=UID01C1
    return queuedCmdIndex,CheckCorrect
