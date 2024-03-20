import RPi.GPIO as GPIO
import time

IN1 = 31
IN2 = 33
IN3 = 35
IN4 = 37

SEQ = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def step(direction, delay, steps):
    for _ in range(steps):
        for step in SEQ[::direction]:
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(delay)

try:
    # Rotate the stepper motor clockwise with a delay of 0.01 seconds for 512 steps
    step(1, 0.01, 512)
    
    # Rotate the stepper motor counterclockwise with a delay of 0.01 seconds for 512 steps
    step(-1, 0.01, 512)

except KeyboardInterrupt:
    GPIO.cleanup()
