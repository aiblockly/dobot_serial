# -*- coding: utf-8 -*-
import numpy as np
import copy

def GetDeviceName_code():
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
    UID01CF=np.concatenate(([1],[UID0200],UID061E))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD


def GetDeviceName_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID013D=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    UID013A=np.array(UID013D,dtype="uint8").tobytes()
    UID00D0=len(UID013A)
    UID00AA=UID00D0-1
    UID016D=UID013A[0:0+UID00AA]
    DeviceName=UID016D
    return DeviceName,CheckCorrect

def GetDeviceSN_code():
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
    UID01CF=np.concatenate(([0],[UID0200],UID061E))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetDeviceSN_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID013D=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    UID013A=np.array(UID013D,dtype="uint8").tobytes()
    UID00D5=len(UID013A)
    UID00AA=UID00D5-1
    UID016D=UID013A[0:0+UID00AA]
    DeviceSN=UID016D
    return DeviceSN,CheckCorrect

def GetDeviceVersion_code():
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
    UID01CF=np.concatenate(([2],[UID0200],UID061E))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2=np.array(UID0087,dtype="uint8").tobytes()
    TXD=UID02C2
    return TXD

def GetDeviceVersion_uncode(RXD):
    UID0049=np.fromstring(RXD,dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID01B3=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    UID00F8UID01B3.tolist()
    DeviceVersion=UID00F8
    return DeviceVersion,CheckCorrect
