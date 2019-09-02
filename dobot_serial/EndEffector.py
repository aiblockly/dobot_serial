# -*- coding: utf-8 -*-
import numpy as np
import copy
import struct



def SetEndEffectorSuctionCup_code(isQueued,suck,enableCtrl):
    UID0061=np.array([170,170],dtype="uint8")
    UID041A=np.concatenate(([True],[isQueued]))
    UID01CE=int(enableCtrl)
    UID01E1=int(suck)
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID01F9=np.concatenate(([UID01CE],[UID01E1]))
    UID0200=int(UID0229)&0xff
    UID01F1=np.array(UID01F9,dtype="uint8")
    UID0110=len(UID01F1)
    UID01CF=np.concatenate(([62],[UID0200],UID01F1))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def SetEndEffectorSuctionCup_uncode(RXD):
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

def SetEndEffectorGripper_code(isQueued,grip,enableCtrl):
    UID0061=np.array([170,170],dtype="uint8")
    UID041A=np.concatenate(([True],[isQueued]))
    UID01CE=int(enableCtrl)
    UID01E1=int(grip)
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID01F9=np.concatenate(([UID01CE],[UID01E1]))
    UID0200=int(UID0229)&0xff
    UID01F1=np.array(UID01F9,dtype="uint8")
    UID0110=len(UID01F1)
    UID01CF=np.concatenate(([63],[UID0200],UID01F1))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def SetEndEffectorGripper_uncode(RXD):
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

def SetEndEffectorLaser_code(isQueued,on,enableCtrl):
    UID0061=np.array([170,170],dtype="uint8")
    UID041A=np.concatenate(([True],[isQueued]))
    UID01CE=int(enableCtrl)
    UID01E1=int(on)
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID01F9=np.concatenate(([UID01CE],[UID01E1]))
    UID0200=int(UID0229)&0xff
    UID01F1=np.array(UID01F9,dtype="uint8")
    UID0110=len(UID01F1)
    UID01CF=np.concatenate(([61],[UID0200],UID01F1))
    UID00DD=UID0110+2
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0569=int(UID00DD)&0xff
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def SetEndEffectorLaser_uncode(RXD):
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

def GetEndEffectorGripper_code():
    UID0061=np.array([170,170],dtype="uint8")
    UID01A7=np.array([0,0],dtype="uint8")
    UID041A=np.concatenate(([False],[False]))
    UID0110=len(UID01A7)
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID00DD=UID0110+2
    UID0200=int(UID0229)&0xff
    UID0569=int(UID00DD)&0xff
    UID01CF=np.concatenate(([63],[UID0200],UID01A7))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetEndEffectorGripper_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID01BE=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    try:
    	UID013B=UID01BE[0]
    except:
    	UID013B=0
    try:
    	UID0144=UID01BE[1]
    except:
    	UID0144=0
    UID0114=UID013B!=0
    UID0130=UID0144!=0
    isCtrlEnabled=UID0114
    isGripped=UID0130
    return isGripped,isCtrlEnabled,CheckCorrect

def GetEndEffectorLaser_code():
    UID0061=np.array([170,170],dtype="uint8")
    UID01A7=np.array([0,0],dtype="uint8")
    UID041A=np.concatenate(([False],[False]))
    UID0110=len(UID01A7)
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID00DD=UID0110+2
    UID0200=int(UID0229)&0xff
    UID0569=int(UID00DD)&0xff
    UID01CF=np.concatenate(([61],[UID0200],UID01A7))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetEndEffectorLaser_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID01BE=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    try:
    	UID0191=UID01BE[0]
    except:
    	UID0191=0
    try:
    	UID019B=UID01BE[1]
    except:
    	UID019B=0
    UID0167=UID0191!=0
    UID0185=UID019B!=0
    isCtrlEnabled=UID0167
    isOn=UID0185
    return isOn,isCtrlEnabled,CheckCorrect

def GetEndEffectorSuctionCup_code():
    UID0061=np.array([170,170],dtype="uint8")
    UID01A7=np.array([0,0],dtype="uint8")
    UID041A=np.concatenate(([False],[False]))
    UID0110=len(UID01A7)
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID00DD=UID0110+2
    UID0200=int(UID0229)&0xff
    UID0569=int(UID00DD)&0xff
    UID01CF=np.concatenate(([62],[UID0200],UID01A7))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetEndEffectorSuctionCup_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID01BE=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    try:
    	UID00FC=UID01BE[0]
    except:
    	UID00FC=0
    try:
    	UID0105=UID01BE[1]
    except:
    	UID0105=0
    UID00DA=UID00FC!=0
    UID00F5=UID0105!=0
    isCtrlEnabled=UID00DA
    isSucked=UID00F5
    return isSucked,isCtrlEnabled,CheckCorrect
