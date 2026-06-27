#!/usr/bin/python3

from gpiozero import MotionSensor
from time import sleep

pir = MotionSensor(18) #(GPIO)

try:
#    print("Warming up sensor...")
#    sleep(45)
    print("Warm-up complete. Monitoring for motion...")

    while True:
        if pir.motion_detected:
            print("Motion detected!")
        else:
            print("No motion")
        sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting...")
