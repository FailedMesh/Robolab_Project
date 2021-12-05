import rospy
import time
import RPi.GPIO as GPIO
from std_msgs.msg import Int64

def TL_motor(command):
	global motor1
	if command.data == 1:
		GPIO.output(In1, GPIO.HIGH)
		GPIO.output(In2, GPIO.LOW)
		motor1.ChangeDutyCycle(50)
	elif command.data == 0:
		motor1.ChangeDutyCycle(0)
	elif command.data == -1:
		GPIO.output(In1, GPIO.LOW)
		GPIO.output(In2, GPIO.HIGH)
		motor1.ChangeDutyCycle(50)
	elif command.data == 2:
		GPIO.output(In1,GPIO.HIGH)
		GPIO.output(In2,GPIO.LOW)
		motor1.ChangeDutyCycle(50)
	elif command.data == 3:
		GPIO.output(In1,GPIO.LOW)
		GPIO.output(In2,GPIO.HIGH)
		motor1.ChangeDutyCycle(50)
if __name__ == '__main__':
	rospy.init_node("Top_left_motor")
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
		
	Enable = 3
	In1 = 5
	In2 = 7

	GPIO.setup(Enable, GPIO.OUT)
	GPIO.setup(In1, GPIO.OUT)
	GPIO.setup(In2, GPIO.OUT)

	global motor1
	motor1 = GPIO.PWM(Enable, 100)
	motor1.start(0)
	
	TL_motor_command = rospy.Subscriber('/command', Int64, TL_motor)
	rospy.spin()

	

	
