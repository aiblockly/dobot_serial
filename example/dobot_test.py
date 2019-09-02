import dobot_serial as dbs
usbport="COM3"


mydobot=dbs.dobot(port=usbport)
pose=mydobot.GetPose()[0]
print (pose)

ret=mydobot.SetPTPCmd([0,pose[0],pose[1]-10*10,pose[2],0.0],True)


mydobot.close()
