#Talking to the drone operating system
from djtellopy import tello
import cv2
#defining me as the varible
me = tello.Tello()
me.connect()
print(me.get_battery())


me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("Image", img)
    cv.waitkey(1)