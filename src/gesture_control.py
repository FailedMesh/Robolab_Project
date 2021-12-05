import rospy
import cv2
import os
import numpy as np
import tensorflow as tf
import mediapipe as mp
from IPython.display import clear_output
from std_msgs.msg import Int64

rospy.init_node("gesture_teleop")
gesture_pub = rospy.Publisher('/command', Int64, queue_size=10)
move = Int64()

gesture_model = tf.keras.models.load_model('iteration_1_weights.h5')

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence = 0.8, max_num_hands = 1)

webcam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('gesture_controlled_car.avi', fourcc, 20.0, (640, 480))

video = []

while webcam.isOpened():
    ret, frame = webcam.read()
    flipped_image = cv2.flip(frame, 1)
    processed_image = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
    processed_image.flags.writeable = False
    results = hands.process(processed_image)
    
    if results.multi_hand_landmarks:
        frame_coords = []
        for hand_landmarks in results.multi_hand_landmarks:
            for i, lm in enumerate(hand_landmarks.landmark): 
                frame_coords.append(lm.x)
                frame_coords.append(lm.y)
            clear_output(wait = True)
            mp_draw.draw_landmarks(flipped_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            input_coords = np.array([frame_coords])
            prediction = np.argmax(gesture_model.predict(input_coords))
            
            if prediction == 0:
                text = "DRIVE FORWARD"
                move.data = 1
                gesture_pub.publish(move)
            if prediction == 1:
                text = "REVERSE"
                move.data = -1
                gesture_pub.publish(move)
            if prediction == 2:
                text = "STOP"
                move.data = 0
                gesture_pub.publish(move)
            if prediction == 3:
                text = "TURN RIGHT"
                move.data = 2
                gesture_pub.publish(move)
            if prediction == 4:
                text = "TURN LEFT"
                move.data = 3
                gesture_pub.publish(move)
                
            cv2.putText(flipped_image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
            out.write(flipped_image)
    
    video.append(flipped_image)
    cv2.imshow('webcam', flipped_image)
    cv2.waitKey(1)

out.release()
video = np.array(video)