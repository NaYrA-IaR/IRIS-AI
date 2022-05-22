import cv2
import mediapipe as mp
import numpy as np

def angle(pointA, pointB, pointC):
    vectorA = []
    vectorA.append(pointA[0] - pointB[0])
    vectorA.append(pointA[1] - pointB[1])
    
    vectorB = []
    vectorB.append(pointC[0]-pointB[0])
    vectorB.append(pointC[1]-pointB[1])

    dot = np.inner(vectorA, vectorB)
    mags = np.linalg.norm(vectorA) * np.linalg.norm(vectorB)
    cos = dot / mags
    
    rad = np.arccos(np.clip(cos, -1.0, 1.0))
    deg = np.rad2deg(rad)

    return int(deg)

def read_file(filename):
    file = open(filename, 'r')
    frame = []
    s = file.read()
    output = s.split(',')
    for i in range(0, len(output) - 1):
        frame.append(int(output[i]))
    return frame

idealDisplay = read_file('idealDisplay.1.txt')
testDisplay = read_file('testDisplay.1.txt')

idealFrameCount = 0
testFrameCount = 0
idealCurrentCount = 0
testCurrentCount = 0
testDisplayCheck = True

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

# Change it to the videos you are using for this.

idealVid = cv2.VideoCapture('1.mp4')
testVid = cv2.VideoCapture('2.mp4')

while idealVid.isOpened() and testVid.isOpened():
    ret, ideal = idealVid.read()
    if ret == False:
        break
    idealFrame = cv2.cvtColor(ideal, cv2.COLOR_BGR2RGB)
    idealDetectedPose = pose.process(idealFrame)
    
    if idealDetectedPose.pose_landmarks:
        if idealCurrentCount == idealDisplay[idealFrameCount]:
            while testDisplayCheck:
                ret, test = testVid.read()
                if ret == False:
                    break
                testFrame = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
                testDetectedPose = pose.process(testFrame)
                
                if testDetectedPose.pose_landmarks:
                    if testCurrentCount == testDisplay[testFrameCount]:
                        mpDraw.draw_landmarks(ideal, idealDetectedPose.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
                        mpDraw.draw_landmarks(test, testDetectedPose.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
                        ideal = cv2.resize(ideal, (750, 500))
                        test = cv2.resize(test, (750, 500))
                        cv2.imshow("Ideal Pose", ideal)
                        cv2.imshow("Test Pose", test)
                        key = cv2.waitKey(500)
                        if key == ord('p'):
                            cv2.waitKey(0)
                        testFrameCount += 1
                        idealFrameCount += 1
                        testDisplayCheck = False
                    testCurrentCount += 1
            testDisplayCheck = True
        idealCurrentCount += 1

idealVid.release()
testVid.release()
cv2.destroyAllWindows()