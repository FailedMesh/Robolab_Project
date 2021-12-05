import rospy
from std_msgs.msg import Int64

if __name__ == '__main__':
	rospy.init_node("keyboard_teleop")
	command_pub = rospy.Publisher('/command', Int64, queue_size = 10)
	#while command_pub.get_num_connections() == 0:
	    #continue
	move = Int64()
	while True:
		command = input("W for forward, S for stop, X for backward:, D for Right ,A for Left :")
		if command == "W" or command == "w":
			move.data = 1
			command_pub.publish(move)
		elif command == "S" or command == "s":
			move.data = 0
			command_pub.publish(move)
		elif command == "X" or command  == "x":
			move.data = -1
			command_pub.publish(move)
		elif command == "D" or command  == "d":
			move.data = 2
			command_pub.publish(move)
		elif command == "A" or command == "a":
			move.data = 3
			command_pub.publish(move)
		else:
			print("Invalid command. Try again.")


