# IRIS-AI


## Overview

IRIS is an advanced AI-powered personal Sports Trainer for players which solves the above problems. With its help, any normal human being can get professional-level guidance to enhance their performance in-game at any place and at any time. We are using Mediapipe for Pose Detection and other Computer Vision-related tasks, and other External Libraries of Python for the application.

## Sample Screenshots

![Alt text](Images/Img1.png?raw=true "Result1")

![Alt text](Images/Img2.png?raw=true "Result2")

![Alt text](Images/Img3.png?raw=true "Result3")

![Alt text](Images/Img4.png?raw=true "Result4")

## Solution

We created a pose detection model using mediapipe and used the respective angles to check for other player's poses. E.g. If we want to learn a badminton smash, we use a smash video as the test video and then upload our own smash video. The result will be the number of steps you are performing right during the whole smash.

## How-To-Run

1) Open cmd in the directory containing the folders. 
2) Run python PoseDetection.py for the respective video. The output will be a txt file which you further put into PoseAnalysis.py.
3) Run python PoseAnalysis.py.
4) Change the path inside the PoseDisplay.py and enter the respective videos as well.
5) Run python PoseDisplay.py.  

Note:

1) It may take time to run as pose detection is a huge task.

## Goal

With the help of this project, any normal human being can get professional-level guidance to enhance their performance in-game at any place and at any time.

## Future Scope

1) Voice assisted Live suggestions and feedbacks.
2) Exciting UI.
3) Support for multiple sports.
