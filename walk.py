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
    
    #get initial servo positions for left leg
    theta1 = servo1.get_physical_angle()
    
    with open('theta1.txt', 'x') as f:
        f.write(str(theta1) + "\n")
    
    print("angle for upper motor on left leg is", theta1)
    
    theta2 = servo2.get_physical_angle()
    print("angle for lower motor on left leg is", theta2)
    
    with open('theta2.txt', 'x') as f:
        f.write(str(theta2) + "\n")

    #right leg
    servo3 = LX16A(3)
    servo4 = LX16A(2)

    #set limits for the servo angles right leg 
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240) 
    
    #get initial servo positions for right leg
    theta3 = servo3.get_physical_angle()
    
    with open('theta3.txt', 'x') as f:
            f.write(str(theta3) + "\n")
        
    print("angle for upper motor on right leg is", theta3)
    theta4 = servo4.get_physical_angle()
    
    print("angle for lower motor on right leg is", theta4)
    
    with open('theta4.txt', 'x') as f:
        f.write(str(theta4) + "\n")

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0

theta10 = 81
theta20 = 157
theta30 = 54
theta40 = 183

while True:
    #motion for the left leg 
    servo1.move(theta10 - sin(t) * 30 - 15)
    servo2.move(theta20 - sin(t) * 10)
    print("\n at time t", t)
    
    print("angle for upper motor on left leg is", servo1.get_physical_angle())
    print("angle for lower motor on left leg is", servo2.get_physical_angle())
  
    #motion for the right leg
    servo3.move(theta30 + sin(t) * 30 - 15)
    servo4.move(theta40 + sin(t) * 10)
    
    print("angle for upper motor on right leg is", servo3.get_physical_angle())
    print("angle for lower motor on right leg is", servo4.get_physical_angle())
    
    time.sleep(0.002)

    t += 0.01
    
    
    #not much motion but stable gait for following parameters 
    """
    #motion for the left leg 
    servo1.move(theta10 - sin(t) * 30 - 15)
    servo2.move(theta20 - sin(t) * 10 + 40)
    print("\n at time t", t)
    
    print("angle for upper motor on left leg is", servo1.get_physical_angle())
    print("angle for lower motor on left leg is", servo2.get_physical_angle())
  
    #motion for the right leg
    servo3.move(theta30 + sin(t) * 30 - 15)
    #servo3.move(theta30)
    servo4.move(theta40 + sin(t) * 10 - 40)
    
    print("angle for upper motor on right leg is", servo3.get_physical_angle())
    print("angle for lower motor on right leg is", servo4.get_physical_angle())
    
    time.sleep(0.002)

    t += 0.01
    """
