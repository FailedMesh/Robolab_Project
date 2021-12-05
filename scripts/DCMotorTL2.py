import rospy
import time
import RPi.GPIO as GPIO
from std_msgs.msg import Int64

def TL_motor(command):
    global motor2
    if command.data == 1:
        GPIO.output(In3, GPIO.HIGH)
        GPIO.output(In4, GPIO.LOW)
        motor2.ChangeDutyCycle(50)
    elif command.data == 0:
        motor2.ChangeDutyCycle(0)
    elif command.data == -1:
        GPIO.output(In3, GPIO.LOW)
        GPIO.output(In4, GPIO.HIGH)
        motor2.ChangeDutyCycle(50)
    elif command.data == 2:
        GPIO.output(In3,GPIO.LOW)
        GPIO.output(In4,GPIO.HIGH)
        motor2.ChangeDutyCycle(50)
    elif command.data == 3:
        GPIO.output(In3,GPIO.HIGH)
        GPIO.output(In4,GPIO.LOW)
        motor2.ChangeDutyCycle(50)

if __name__ == '__main__':
    rospy.init_node("Top_right_motor")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    Enable2 = 11
    In3 = 13
    In4 = 15

    GPIO.setup(Enable2, GPIO.OUT)
    GPIO.setup(In3, GPIO.OUT)
    GPIO.setup(In4, GPIO.OUT)

    global motor2
    motor2 = GPIO.PWM(Enable2, 100)
    motor2.start(0)
    TL_motor_command = rospy.Subscriber('/command',Int64,TL_motor)
    rospy.spin()
    
