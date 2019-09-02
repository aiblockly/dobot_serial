# -*- coding: utf-8 -*-
import numpy as np
import copy

def ClearAllAlarmsState_code():
    UID0061=np.array([170,170],dtype="uint8")
    UID061E=np.array([],dtype="uint8")
    UID041A=np.concatenate(([True],[False]))
    UID0110=len(UID061E)
    UID0229=UID0229_i=0
    for i in UID041A:
    	UID0229=UID0229+int(i)*2**UID0229_i
    	UID0229_i=UID0229_i+1
    UID00DD=UID0110+2
    UID0200=int(UID0229)&0xff
    UID0569=int(UID00DD)&0xff
    UID01CF=np.concatenate(([21],[UID0200],UID061E))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2="".join(map(chr,UID0087))
    TXD=UID02C2
    return TXD

def ClearAllAlarmsState_uncode(RXD):
    UID012B=np.array(map(ord,RXD),dtype="uint8")
    UID0128=UID012B[0:0+3]
    UID01E3=np.delete(UID012B,np.s_[0:0+3])
    UID02AE=np.sum(UID01E3)
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    return CheckCorrect

def GetAlarmsState_code():
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
    UID01CF=np.concatenate(([20],[UID0200],UID061E))
    UID003B=np.sum(UID01CF)
    UID045C=256-int(UID003B)
    UID0571=int(UID045C)&0xff
    UID0087=np.concatenate((UID0061,[UID0569],UID01CF,[UID0571]))
    UID02C2="".join(map(chr,UID0087))
    TXD=UID02C2
    return TXD

def GetAlarmsState_uncode(RXD):
    UID0049=np.array(map(ord,RXD),dtype="uint8")
    UID00B6=len(UID0049)
    UID0128=UID0049[0:0+3]
    UID01E3=np.delete(UID0049,np.s_[0:0+3])
    UID005B=UID00B6-6
    UID02AE=np.sum(UID01E3)
    UID0178=UID0049[5:5+UID005B]
    UID02CD=UID02AE==0
    CheckCorrect=UID02CD
    alarmState=UID0178
    return alarmState,CheckCorrect


