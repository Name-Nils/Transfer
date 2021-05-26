import RPi.GPIO
import RPiMotorLib
import time

direction = 27
step = 17
enable = 22

motor_run = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
RPi.GPIO.setup(enable,RPi.GPIO.OUT)

def motor(speed, distance):
    RPi.GPIO.output(enable,RPi.GPIO.LOW)
    motor_run.motor_go(True, "1/32", distance, speed, False, .0)

    
    motor_run.motor_go(False, "Half", distance, 0.05, False, .0) #move home again
    RPi.GPIO.output(enable,RPi.GPIO.HIGH)
