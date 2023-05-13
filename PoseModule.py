"""
Pose Module
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""
import cv2
import mediapipe as mp
import numpy as np

class PoseDetector:
    """
    Estimates Pose points of a human body using the mediapipe library.
    """

    def __init__(self, mode=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param upBody: Upper boy only flag
        :param smooth: Smoothness Flag
        :param detectionCon: Minimum Detection Confidence Threshold
        :param trackCon: Minimum Tracking Confidence Threshold
        """

        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode,
                                     smooth_landmarks=self.smooth,
                                     min_detection_confidence=self.detectionCon,
                                     min_tracking_confidence=self.trackCon)

    def findPose(self, img, draw=True):
        """
        Find the pose landmarks in an Image of BGR color space.
        :param img: Image to find the pose in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def nvc(self,lmList):

        left_hip = lmList[23]
        right_hip = lmList[24]

        bottom_torso_x = (lmList[11][1] + lmList[12][1] + lmList[23][1] + lmList[24][1]) / 4.0
        bottom_torso_y = (lmList[11][2] + lmList[12][2] + lmList[23][2] + lmList[24][2]) / 4.0
        bottom_torso_z = (lmList[11][3] + lmList[12][3] + lmList[23][3] + lmList[24][3]) / 4.0

        bottom_torso = bottom_torso_x, bottom_torso_y,bottom_torso_z

        navel_x = (left_hip[1] + right_hip[1] + bottom_torso[0]) / 3.0
        navel_y = (left_hip[2] + right_hip[2] + bottom_torso[1]) / 3.0
        navel_z = (left_hip[3] + right_hip[3] + bottom_torso[2]) / 3.0
        lmList.append([33, int(navel_x),int(navel_y),int(navel_z)])
        return lmList

    def Angle(self,lmlist,First, Second, Third):
        Pa_X = lmlist[First][1]
        Pa_Y= lmlist[First][2]

        Pb_X = lmlist[Second][1]
        Pb_Y= lmlist[Second][2]

        Pc_X = lmlist[Third][1]
        Pc_Y= lmlist[Third][2]

        a = [Pa_X, Pa_Y]
        b = [Pb_X, Pb_Y]
        c = [Pc_X, Pc_Y]
        a = np.array(a) # First
        b = np.array(b) # Mid
        c = np.array(c) # End
        
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
        
        if angle >180:
            angle = 360-angle
            
        return angle
    def findPosition(self, img, draw=True, bboxWithHands=False):
        self.lmList = []
        self.bboxInfo = {}
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                self.lmList.append([id, cx, cy, cz])

            # Bounding Box
            self.lmList=self.nvc(self.lmList)
            ad = abs(self.lmList[12][1] - self.lmList[11][1]) // 2
            if bboxWithHands:
                x1 = self.lmList[16][1] - ad
                x2 = self.lmList[15][1] + ad
            else:
                x1 = self.lmList[12][1] - ad
                x2 = self.lmList[11][1] + ad

            y2 = self.lmList[29][2] + ad
            y1 = self.lmList[1][2] - ad
            bbox = (x1, y1, x2 - x1, y2 - y1)
            cx, cy = bbox[0] + (bbox[2] // 2), \
                     bbox[1] + bbox[3] // 2

            self.bboxInfo = {"bbox": bbox, "center": (cx, cy)}

            if draw:
                cv2.rectangle(img, bbox, (255, 0, 255), 3)
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return self.lmList, self.bboxInfo
