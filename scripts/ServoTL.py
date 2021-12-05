# Import libraries
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int64


def TL_servo(command):
	global servo1
	if command.data == 2:
		angle = 45
		servo1.ChangeDutyCycle(2+(angle/18))
		time.sleep(0.5)
		servo1.ChangeDutyCycle(0)

if __name__ == '__main__':
	rospy.init_node("ServoTL")
	
	GPIO.setmode(GPIO.BOARD)
	
	global servo1
	GPIO.setup(8,GPIO.OUT)
	servo1 = GPIO.PWM(8,50)
	servo1.start(0)
	
	TL_servo_command = rospy.Subscriber('/command', Int64, TL_servo)
	
	rospy.spin()
