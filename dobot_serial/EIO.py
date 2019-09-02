# -*- coding: utf-8 -*-
import numpy as np
import struct
import copy

def GetIOADC_code(address):
    UID0061=np.array([170,170],dtype="uint8")
    UID013B=[0,0]
    Constant_UID0479=""
    UID041A=np.concatenate(([False],[False]))
    UID0263=copy.copy(UID013B)
    UID0263[0]=address
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID0499=UID0263[1]
    UID046B=UID0263[0]
    UID0200=int(UID0229)&0xff
    UID04AA=struct.pack(">B",UID046B)
    UID04A7=struct.pack(">H",UID0499)
    UID0494=UID04A7+UID04AA
    UID04B6=np.fromstring(UID0494,dtype="uint8")
    UID04B3=UID04B6[: :-1]
    UID0110=len(UID04B3)
    UID01CF=np.concatenate(([134],[UID0200],UID04B3))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetIOADC_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID0199=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    UID0195=UID0199[: :-1]
    UID0224=UID0195[0:0+2]
    UID0294=UID0195[2:]
    UID0444=int(np.fromstring((np.array(UID0224,dtype=">u1").tobytes()),dtype=">u2")[0])
    UID043D=int(np.fromstring((np.array(UID0294,dtype=">u1").tobytes()),dtype=">u1")[0])
    UID011D=[UID043D,UID0444]
    ioADC=UID011D
    return ioADC,CheckCorrect

def GetIODI_code(address):
    UID0061=np.array([170,170],dtype="uint8")
    UID00D6=[0,0]
    UID041A=np.concatenate(([False],[False]))
    UID024F=copy.copy(UID00D6)
    UID024F[0]=address
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID024A=np.array(UID024F,dtype="uint8")
    UID0110=len(UID024A)
    UID0200=int(UID0229)&0xff
    UID00DD=UID0110+2
    UID01CF=np.concatenate(([133],[UID0200],UID024A))
    UID003B=np.sum(UID01CF)
    UID0569=int(UID00DD)&0xff
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetIODI_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID01DD=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    UID011BUID01DD.tolist()
    ioDI=UID011B
    return ioDI,CheckCorrect

def GetIODO_code(address):
    UID0061=np.array([170,170],dtype="uint8")
    UID015D=[0,0]
    UID041A=np.concatenate(([False],[False]))
    UID013D=copy.copy(UID015D)
    UID013D[0]=address
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID0139=np.array(UID013D,dtype="uint8")
    UID0110=len(UID0139)
    UID0200=int(UID0229)&0xff
    UID00DD=UID0110+2
    UID01CF=np.concatenate(([131],[UID0200],UID0139))
    UID003B=np.sum(UID01CF)
    UID0569=int(UID00DD)&0xff
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetIODO_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID01DD=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    UID011FUID01DD.tolist()
    ioDO=UID011F
    return ioDO,CheckCorrect

def GetIOMultiplexing_code(address):
    UID0061=np.array([170,170],dtype="uint8")
    UID0152=[0,0]
    UID041A=np.concatenate(([False],[False]))
    UID021A=copy.copy(UID0152)
    UID021A[0]=address
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID02DB=UID021A[0]
    UID02AF=UID021A
    UID0200=int(UID0229)&0xff
    UID02E9=int(UID02AF)&0xff
    UID02D8=np.concatenate(([UID02DB],[UID02E9]))
    UID0110=len(UID02D8)
    UID01CF=np.concatenate(([130],[UID0200],UID02D8))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetIOMultiplexing_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID01DD=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    UID014EUID01DD.tolist()
    ioMultiplexing=UID014E
    return ioMultiplexing,CheckCorrect

def GetIOPWM_code(address):
    UID0061=np.array([170,170],dtype="uint8")
    Constant_UID0153=""
    UID01B0=[0,0.000000,0.000000]
    UID041A=np.concatenate(([False],[False]))
    UID0139=copy.copy(UID01B0)
    UID0139[0]=address
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID0166=UID0139[2]
    UID0148=UID0139[1]
    UID032F=UID0139[0]
    UID0200=int(UID0229)&0xff
    UID0177=struct.pack(">f",UID0148)
    UID0174=struct.pack(">f",UID0166)
    UID03A6=struct.pack(">B",UID032F)
    UID0161=UID0174+UID0177+UID03A6
    UID0180=np.fromstring(UID0161,dtype="uint8")
    UID017D=UID0180[: :-1]
    UID0110=len(UID017D)
    UID01CF=np.concatenate(([132],[UID0200],UID017D))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetIOPWM_uncode(RXD):
    UID021B=[0.000000,0.000000,0]
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID01AA=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    UID0188=UID01AA[: :-1]
    UID0452=np.fromstring((np.array(UID0188,dtype=">u1").tobytes()),dtype="")[0]
    UID04A7=UID0452[0]
    UID046C=UID0452[1]
    UID0469=UID0452[2]
    UID012D=[UID0469,UID046C,UID04A7]
    ioPWM=UID012D
    return ioPWM,CheckCorrect

def SetEMotor_code(isQueued,eMotor):
    UID0061=np.array([170,170],dtype="uint8")
    Constant_UID023B=""
    UID041A=np.concatenate(([True],[isQueued]))
    UID027C=eMotor[2]
    UID022C=eMotor[1]
    UID024C=eMotor
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID0290=struct.pack(">B",UID022C)
    UID0294=struct.pack(">B",UID024C)
    UID028C=struct.pack(">f",UID027C)
    UID0200=int(UID0229)&0xff
    UID0277=UID028C+UID0290+UID0294
    UID02A3=np.fromstring(UID0277,dtype="uint8")
    UID02A0=UID02A3[: :-1]
    UID0110=len(UID02A0)
    UID01CF=np.concatenate(([135],[UID0200],UID02A0))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def SetEMotor_uncode(RXD):
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
    UID01C1=int(np.fromstring((np.array(UID0095,dtype=">u1").tobytes()),dtype=">u8")[0])
    queuedCmdIndex=UID01C1
    return queuedCmdIndex,CheckCorrect

def SetIODO_code(isQueued,ioDO):
    UID0061=np.array([170,170],dtype="uint8")
    UID041A=np.concatenate(([True],[isQueued]))
    UID0252=np.array(ioDO,dtype="uint8")
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID0110=len(UID0252)
    UID00DD=UID0110+2
    UID0200=int(UID0229)&0xff
    UID01CF=np.concatenate(([131],[UID0200],UID0252))
    UID0569=int(UID00DD)&0xff
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def SetIODO_uncode(RXD):
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
    UID01C1=int(np.fromstring((np.array(UID0095,dtype=">u1").tobytes()),dtype=">u8")[0])
    queuedCmdIndex=UID01C1
    return queuedCmdIndex,CheckCorrect

def SetIOMultiplexing_code(isQueued,ioMultiplexing):
    UID0061=np.array([170,170],dtype="uint8")
    UID041A=np.concatenate(([True],[isQueued]))
    UID0328=ioMultiplexing[0]
    UID038B=ioMultiplexing
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID0336=int(UID038B)&0xff
    UID0200=int(UID0229)&0xff
    UID0325=np.concatenate(([UID0328],[UID0336]))
    UID0110=len(UID0325)
    UID01CF=np.concatenate(([130],[UID0200],UID0325))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def SetIOMultiplexing_uncode(RXD):
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
    UID01C1=int(np.fromstring((np.array(UID0095,dtype=">u1").tobytes()),dtype=">u8")[0])
    queuedCmdIndex=UID01C1
    return queuedCmdIndex,CheckCorrect

def SetIOPWM_code(isQueued,ioPWM):
    UID0061=np.array([170,170],dtype="uint8")
    Constant_UID023B=""
    UID041A=np.concatenate(([True],[isQueued]))
    UID027C=ioPWM[2]
    UID022C=ioPWM[1]
    UID024C=ioPWM[0]
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID0290=struct.pack(">f",UID022C)
    UID0294=struct.pack(">B",UID024C)
    UID028C=struct.pack(">f",UID027C)
    UID0200=int(UID0229)&0xff
    UID0277=UID028C+UID0290+UID0294
    UID02A3=np.fromstring(UID0277,dtype="uint8")
    UID02A0=UID02A3[: :-1]
    UID0110=len(UID02A0)
    UID01CF=np.concatenate(([132],[UID0200],UID02A0))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def SetIOPWM_uncode(RXD):
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
    UID01C1=int(np.fromstring((np.array(UID0095,dtype=">u1").tobytes()),dtype=">u8")[0])
    queuedCmdIndex=UID01C1
    return queuedCmdIndex,CheckCorrect
