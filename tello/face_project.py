#!/usr/bin/env python
# coding: utf-8

# ## AFFECTIVE COMPUTING PROJECT
# ### Basic emotion recognition using live drone feed
# ##### Mislav Perić & Filip Furko, 2024.

# ### Problem description and aim of the project
# Artifical intelligence has become a huge party of people's everyday lives in the past years gaining huge popularity because of it's vast application and use cases. Computer vision is the most researched field when talking about live feed object recognition and pose estimation which is the backbone of this project. Tracking a persons body language and movements can provide a lot more information than just a simple movement, thus, focusing on those parameters, we can recognise their incentives. Surveillance is a prime example of the previously defined problem.
# By using live camera feeds, mounted on the most simplest drones, we are able to achieve just that. Connecting drone's open API, the goal is to recognise live emotions from people's faces to be able to act on it accordingly. Use cases that can be interesing to think about are usage of drones in stadiums or concerts to recognise fan satisfaction, overall emotion, or even anger, if there are any disputes, and resolve them quicker than expected.

# ### Objective
# The objective is to use the drone to fly over a person, or a group of people, recognise their facial expressions and classify the emotion they are experiencing with the model. Possible emotions that will be recognised are:
# - angry
# - digust
# - fear
# - happy
# - sad
# - surpise
# - neutral
# 
# The pre-trained Haar cascades classifier from OpenCV, which can identify faces in photos or video streams, will be utilized for this task. To identify faces in the live video feed, the code uses a face cascade classifier (cv2.CascadeClassifier).

# ### Face detection
# In the process of building the whole system, face detection was the first building block.
# To test the face detection accuracy, firstly it was tested using the live feed from the laptop camera provided below.

# In[ ]:


'''
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream or file")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break


    cv2.imshow('Laptop Camera Feed', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''


# After sucessfully testing and opening the camera feed in Python. The actual face detection needed to be implemented. This was done by using the combination of OpenCV CascadeClassifier() and Haar Cascade Classifier. It uses a cascade of classifiers to detect different features in an image or a feed.
# The goal was to create a rectangle shape around the face which indicates the detection of the face itself. Webcam feed was also converted to greyscale for the face detection algorithm which is the first parameter.
# When using detectMultiScale(), it was necessary to focus on the parameters:
# - scaleFactor - specifying how much the image size is reduced at each image scale
# - minNeighbors - specifying how many neighbors each candidate rectangle should have to retain it
# - minSize- Minimum possible object size, where objects smaller than that are ignored

# In[10]:

from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam (value 0 is for default camera, in case you have only 1)

while True:
    # Capture frame-by-frame
    img = tello.get_frame_read().frame
    img = cv.resize(img, (360, 240))


    # Convert to grayscale for the face detection algorithm
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', img)

    # Press 'q' on the keyboard to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop running the cell by clicking q on the keyboard
cap.release()
cv2.destroyAllWindows()


# ### Building the emotion recognition model
# This part was crutial for creaing the project, because the most valuable information came from the actual recognition of the faces captured.
# Training and evaluation of the model will be handled with Fec2013 dataset where each image was stored as 48x48 px.

# ### Training the model
# The model was trained using convolutional neural networks that are known to have high ability to efficiently capture and process spatial features of the faces.

# In[ ]:




