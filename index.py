import RPi.GPIO as GPIO
import sys
import time

Angle = int(sys.argv[1],10) #* 引数[1]で受け取った角度をint(10進数)に変換して格納
Servo_pin = 18      #* GPIO_18番を指定

GPIO.setmode(GPIO.BCM)
GPIO.setup(Servo_pin, GPIO.OUT)

Servo = GPIO.PWM(Servo_pin, 50)
Servo.start(0)


#* 引数で受け取った角度にサーボを回す関数
def servo_angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    Servo.ChangeDutyCycle(duty)
    print("{ angle: " + str(angle) + " , duty: " + str(duty) + " }")
    time.sleep(0.1)

'''
{ angle: 90 , duty: 12.0 }
{ angle: 0 , duty: 7.25 }
{ angle: -90 , duty: 2.5 }
'''

servo_angle(Angle)
Servo.stop()
GPIO.cleanup(Servo_pin)
sys.exit()
