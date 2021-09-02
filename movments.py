#Talking to the drone operating system
from djtellopy import tello
from time import sleep
#defining me as the varible
me = tello.Tello()
me.connect()
print(me.get_battery())
#drone directions
#takeoff
me.takeoff()
#move forward in flight
me.send_rc_control(0,50,0,0)
#stop midair
sleep(2)
#move left
me.send_rc_control(-30,0,0,0)
#landing instructions
me.send_rc_control(0,0,0,0)
me.land()