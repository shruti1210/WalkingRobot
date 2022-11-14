from math import sin, cos
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    #left leg 
    servo1 = LX16A(4)
    servo2 = LX16A(1)

    #set limits for the servo angles left leg
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)

    #right leg
    servo3 = LX16A(3)
    servo4 = LX16A(2)

    #set limits for the servo angles right leg 
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)    

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    #motion for the left leg 
    servo1.move(sin(t) * 10 + 10)
    servo2.move(sin(t) * 10 + 190)

    time.sleep(0.1)
    
    #motion for the right leg
    servo3.move(sin(t) * 10 + 10)
    servo4.move(sin(t) * 10 + 190)
    time.sleep(0.1)

    t += 0.1
