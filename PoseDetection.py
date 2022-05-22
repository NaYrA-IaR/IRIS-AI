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

# Enter the video you want to process for detection.
vid = cv2.VideoCapture('6.mp4')
allAngles = []

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while vid.isOpened():
    ret, frame = vid.read()
    
    if ret == False:
        break
    
    newFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detectedPose = pose.process(newFrame)
    key = cv2.waitKey(1)
    if key == ord('p'):
        cv2.waitKey(0)

    if detectedPose.pose_landmarks:
        
        left_ankle = detectedPose.pose_landmarks.landmark[27]
        left_knee = detectedPose.pose_landmarks.landmark[25]
        left_hip = detectedPose.pose_landmarks.landmark[23]
        left_shoulder = detectedPose.pose_landmarks.landmark[11]
        left_elbow = detectedPose.pose_landmarks.landmark[13]
        left_wrist = detectedPose.pose_landmarks.landmark[15]
        right_ankle = detectedPose.pose_landmarks.landmark[28]
        right_knee = detectedPose.pose_landmarks.landmark[26]
        right_hip = detectedPose.pose_landmarks.landmark[24]
        right_shoulder = detectedPose.pose_landmarks.landmark[12]
        right_elbow = detectedPose.pose_landmarks.landmark[14]
        right_wrist = detectedPose.pose_landmarks.landmark[16]
        
        left_knee_angle = angle([left_hip.x, left_hip.y, left_hip.z], [left_knee.x, left_knee.y, left_knee.z], [left_ankle.x, left_ankle.y, left_ankle.z])
        right_knee_angle = angle([right_hip.x, right_hip.y, right_hip.z], [right_knee.x, right_knee.y, right_knee.z], [right_ankle.x, right_ankle.y, right_ankle.z])
        left_elbow_angle = angle([left_shoulder.x, left_shoulder.y, left_shoulder.z], [left_elbow.x, left_elbow.y, left_elbow.z], [left_wrist.x, left_wrist.y, left_wrist.z])
        right_elbow_angle = angle([right_shoulder.x, right_shoulder.y, right_shoulder.z], [right_elbow.x, right_elbow.y, right_elbow.z], [right_wrist.x, right_wrist.y, right_wrist.z])
        left_shoulder_angle = angle([left_elbow.x, left_elbow.y, left_elbow.z], [left_shoulder.x, left_shoulder.y, left_shoulder.z], [left_hip.x, left_hip.y, left_hip.z])
        right_shoulder_angle = angle([right_elbow.x, right_elbow.y, right_elbow.z], [right_shoulder.x, right_shoulder.y, right_shoulder.z], [right_hip.x, right_hip.y, right_hip.z])
        left_hip_angle = angle([left_shoulder.x, left_shoulder.y, left_shoulder.z], [left_hip.x, left_hip.y, left_hip.z], [left_knee.x, left_knee.y, left_knee.z])
        right_hip_angle = angle([right_shoulder.x, right_shoulder.y, right_shoulder.z], [right_hip.x, right_hip.y, right_hip.z], [right_knee.x, right_knee.y, right_knee.z])
        
        allAngles.append([left_knee_angle, right_knee_angle, left_elbow_angle, right_elbow_angle, left_shoulder_angle, right_shoulder_angle, left_hip_angle, right_hip_angle])
        mpDraw.draw_landmarks(frame, detectedPose.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
    
    cv2.imshow("Pose Detection", frame)

print(allAngles)     
file = open("6.txt", 'w')
for frame in allAngles:
    for angle in frame:
        file.write(str(angle) + ',')
file.close()

vid.release()
cv2.destroyAllWindows()