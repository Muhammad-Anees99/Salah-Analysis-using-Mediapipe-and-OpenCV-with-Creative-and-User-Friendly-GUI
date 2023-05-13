# Salah-Analysis-using-Mediapipe-and-OpenCV-with-Creative-and-User-Friendly-GUI
This project is a Python-based solution for real-time detection and tracking of different poses of Salah using the Mediapipe library and Graphical User Interface (GUI). It uses the pose estimation model provided by Mediapipe to detect the 33 keypoints of the human body, including the head, neck, shoulders, elbows, wrists, hips, knees, and ankles.
# Automated-Salah-Pose-Tracker-using-Mediapipe-and-User-Friendly-Interface
This project is a Python-based solution for real-time detection and tracking of different poses of Salah using the Mediapipe library and Graphical User Interface (GUI). It uses the pose estimation model provided by Mediapipe to detect the 33 keypoints of the human body, including the head, neck, shoulders, elbows, wrists, hips, knees, and ankles.
This project is a Python-based solution for real-time detection and tracking of different poses of Salah using the Mediapipe library and Graphical User Interface (GUI). It uses the pose estimation model provided by Mediapipe to detect the 33 keypoints of the human body, including the head, neck, shoulders, elbows, wrists, hips, knees, and ankles. The detected pose is then classified using a custom algorithm that matches the keypoints with the expected pose positions for Salah. The system is designed to be user-friendly, with an intuitive GUI that displays the detected pose in real-time and provides feedback to the user on the accuracy of the pose.

The project includes the following features:

Real-time detection and tracking of different poses of Salah
Mediapipe-based pose estimation model for detecting 33 keypoints of the human body
Custom algorithm for classifying the detected pose as one of the expected Salah poses
User-friendly GUI for displaying the detected pose in real-time and providing feedback to the user on the accuracy of the pose
Open-source code available on GitHub for anyone to use and modify
This project is intended to help people improve their Salah poses by providing real-time feedback on their performance. It can be used by individuals practicing Salah on their own or by instructors teaching a group of students. The system is also flexible and can be customized to accommodate different body sizes and types.
*******************************************************************************************************************************************************************************************
                          						-----Instructions-----

>> Always keep the "PoseModule.py" in the same folder as the main program.

>> Always take a png file named "bg11" inside the working folder.

>> Make sure to connect the device with the internet for text-to-speech conversion.
*******************************************************************************************************************************************************************************************
>> Install all Libraries
from tkinter import filedialog
*******************************************************************************************************************************************************************************************
from PoseModule import PoseDetector
*******************************************************************************************************************************************************************************************
import cv2
*******************************************************************************************************************************************************************************************
import numpy as np
*******************************************************************************************************************************************************************************************
from tkinter import*
*******************************************************************************************************************************************************************************************
from PIL import Image, ImageTk
*******************************************************************************************************************************************************************************************
import mediapipe as mp
*******************************************************************************************************************************************************************************************
import pyttsx3
*******************************************************************************************************************************************************************************************
import webbrowser
*******************************************************************************************************************************************************************************************
import time
*******************************************************************************************************************************************************************************************
import threading
