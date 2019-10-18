from .PTP import *
from .Alarm import *
from .Pose import *
from .CP import *
from .ARC import *
from .EndEffector import *
from .Jog import *
from .Device import *
from .Home import *
from .Wait import *
from .EIO import *
from .QueueCmd import *
import serial
import time


def readbuffer(ser):
    while 1:
        if ser.inWaiting()>=3:
            break
        else:
            time.sleep(0.001)
    mybuffer=ser.read(3)
    length=int(np.fromstring(mybuffer,dtype="uint8")[2])+1
    while 1:
        if ser.inWaiting()>=length:
            break
        else:
            time.sleep(0.001)
    mybuffer=mybuffer+ser.read(length)
    #print len(mybuffer)
    return mybuffer


class dobot:
    def __init__(self,port):
        self.port=serial.Serial(port,115200,timeout=60)

    def SetPTPCmd(self,tagPTPCmd=[0,200.0,30.0,50.0,0.0],isQueued=True):
        mybuffer=SetPTPCmd_code(isQueued,tagPTPCmd)
        self.port.write(mybuffer)
        return SetPTPCmd_uncode(readbuffer(self.port))

    def close(self):
        self.port.close()

    def GetPose(self,):
        mybuffer=GetPose_code()
        self.port.write(mybuffer)
        return GetPose_uncode(readbuffer(self.port))

    def SetCPCmd(self,cpCmd,isQueued=True):
        mybuffer=SetCPCmd_code(isQueued,cpCmd)
        self.port.write(mybuffer)
        return SetCPCmd_uncode(readbuffer(self.port))

    def SetARCCmd(self,ARCCmd,isQueued=True):
        mybuffer=SetARCCmd_code(isQueued,ARCCmd)
        self.port.write(mybuffer)
        return SetARCCmd_uncode(readbuffer(self.port))

    def SetEndEffectorSuctionCup(self,enableCtrl,suck,isQueued):
        mybuffer=SetEndEffectorSuctionCup_code(isQueued,suck,enableCtrl)
        self.port.write(mybuffer)
        return SetEndEffectorSuctionCup_uncode(readbuffer(self.port))

    def SetEndEffectorGripper(self,enableCtrl,grip,isQueued):
        mybuffer=SetEndEffectorGripper_code(isQueued,grip,enableCtrl)
        self.port.write(mybuffer)
        return SetEndEffectorGripper_uncode(readbuffer(self.port))

    def SetEndEffectorLaser(self,enableCtrl,on,isQueued):
        mybuffer=SetEndEffectorLaser_code(isQueued,on,enableCtrl)
        self.port.write(mybuffer)
        return SetEndEffectorLaser_uncode(readbuffer(self.port))

    def GetEndEffectorGripper(self):
        mybuffer=GetEndEffectorGripper_code()
        self.port.write(mybuffer)
        return GetEndEffectorGripper_uncode(readbuffer(self.port))

    def GetEndEffectorLaser(self):
        mybuffer=GetEndEffectorLaser_code()
        self.port.write(mybuffer)
        return GetEndEffectorLaser_uncode(readbuffer(self.port))

    def GetEndEffectorSuctionCup(self):
        mybuffer=GetEndEffectorSuctionCup_code()
        self.port.write(mybuffer)
        return GetEndEffectorSuctionCup_uncode(readbuffer(self.port))

    def SetJOGCmd(self,tagJOGCmd,isQueued):
        mybuffer=SetJOGCmd_code(isQueued,tagJOGCmd)
        self.port.write(mybuffer)
        return SetJOGCmd_uncode(readbuffer(self.port))

    def GetDeviceName(self):
        mybuffer=GetDeviceName_code()
        self.port.write(mybuffer)
        return GetDeviceName_uncode(readbuffer(self.port))

    def GetDeviceSN(self):
        mybuffer=GetDeviceSN_code()
        self.port.write(mybuffer)
        return GetDeviceSN_uncode(readbuffer(self.port))

    def GetDeviceVersion(self):
        mybuffer=GetDeviceVersion_code()
        self.port.write(mybuffer)
        return GetDeviceVersion_uncode(readbuffer(self.port))

    def SetHomeCmd(self,isQueued=True):
        mybuffer=SetHomeCmd_code(isQueued)
        self.port.write(mybuffer)
        return SetHomeCmd_uncode(readbuffer(self.port))

    def SetWAITCmd(self,tagWAITCmd,isQueued=True):
        mybuffer=SetWAITCmd_code(isQueued,tagWAITCmd)
        self.port.write(mybuffer)
        return SetWAITCmd_uncode(readbuffer(self.port))

    def GetIOADC(self,address):
        mybuffer=GetIOADC_code(address)
        self.port.write(mybuffer)
        return GetIOADC_uncode(readbuffer(self.port))

    def GetIODI(self,address):
        mybuffer=GetIODI_code(address)
        self.port.write(mybuffer)
        return GetIODI_uncode(readbuffer(self.port))

    def GetIODO(self,address):
        mybuffer=GetIODI_code(address)
        self.port.write(mybuffer)
        return GetIODO_uncode(readbuffer(self.port))

    def GetIOMultiplexing(self,address):
        mybuffer=GetIOMultiplexing_code(address)
        self.port.write(mybuffer)
        return GetIOMultiplexing_uncode(readbuffer(self.port))

    def GetIOPWM(self,address):
        mybuffer=GetIOPWM_code(address)
        self.port.write(mybuffer)
        return GetIOPWM_uncode(readbuffer(self.port))

    def SetEMotor(self,eMotor,isQueued=True):
        mybuffer=SetEMotor_code(isQueued,eMotor)
        self.port.write(mybuffer)
        return SetEMotor_uncode(readbuffer(self.port))

    def SetIODO(self,ioDO,isQueued=True):
        mybuffer=SetIODO_code(isQueued,ioDO)
        self.port.write(mybuffer)
        return SetIODO_uncode(readbuffer(self.port))

    def SetIOMultiplexing(self,ioMultiplexing,isQueued=True):
        mybuffer=SetIOMultiplexing_code(isQueued,ioMultiplexing)
        self.port.write(mybuffer)
        return SetIOMultiplexing_uncode(readbuffer(self.port))

    def SetIOPWM(self,ioPWM,isQueued=True):
        mybuffer=SetIOPWM_code(isQueued,ioPWM)
        self.port.write(mybuffer)
        return SetIOPWM_uncode(readbuffer(self.port))

    def GetQueuedCmdCurrentIndex(self):
        mybuffer=GetQueuedCmdCurrentIndex_code()
        self.port.write(mybuffer)
        return GetQueuedCmdCurrentIndex_uncode(readbuffer(self.port))
