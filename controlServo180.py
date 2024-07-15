from servo import Servo
import time
from time import sleep

sg90_servo = Servo(pin=2)  # Varies according to the GPIO pin used

while True:
    angle = input("Enter rotation angle (0-180), or -1 to exit: ")

    try:
        angle = int(angle)
    except ValueError:
        print("Invalid rotation angle. Please re-enter.")
        continue

    if angle == -1:
        break

    if angle < 0 or angle > 180:
        print("Invalid rotation angle. Please re-enter.")
        continue

    sg90_servo.move(angle)

    time.sleep(1) 
