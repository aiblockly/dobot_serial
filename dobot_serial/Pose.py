import numpy as np

def GetPose_code():
    UID0061=np.array([170,170],dtype="uint8")
    UID061E=np.array([],dtype="uint8")
    UID041A=np.concatenate(([False],[False]))
    UID0110=len(UID061E)
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID00DD=UID0110+2
    UID0200=int(UID0229)&0xff
    UID0569=int(UID00DD)&0xff
    UID01CF=np.concatenate(([10],[UID0200],UID061E))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetPose_uncode(RXD):
    UID0076=np.array([],dtype="float32")
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
    UID00A3=np.fromstring((np.array(UID0095,dtype=">u1").tobytes()),dtype=">f4")
    UID00CA=UID00A3[: :-1]
    UID058B=UID00CA.tolist()
    pose=UID058B
    return pose,CheckCorrect
