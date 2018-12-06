#!/usr/bin/python

import sys
import ZeroBorg
import time
import cv2 as cv
import math
import sched, time

from picamera.array import PiRGBArray
from picamera import PiCamera

(imw, imh) = (160, 120)

def debug(msg):
    print("{0}: {1}".format(time.time(), msg))

debug("imports done")

def sigm(x):
    res = math.tanh(float(x)*4)
    if (res > 0.05 and res < 0.5):
        res = 0.5
    if (res < -0.05 and res > -0.5):
        res = -0.5
    if (res < 0.05 and res > -0.05):
        res = 0
    return res

def adjustMotors(frame, detector, zb):
    gray1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 
    gray2 = cv.equalizeHist(gray1)
    faces = detector.detectMultiScale(gray2)
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        
        l = float(x) / imw
        r = float(imw - x - w) / imw
        
        speed = sigm(l - r)
        
        debug(str((l, r, speed)))
        
        zb.SetMotor1(-speed)
        zb.SetMotor3(-speed)
    else:
        debug("no faces")
        zb.SetMotor1(0)
        zb.SetMotor3(0)

def init():
    camera = PiCamera()
    camera.resolution = (imw, imh)
    camera.framerate = 8
    rawCapture = PiRGBArray(camera, size=camera.resolution)
    
    cap = (camera, rawCapture)

    zb = ZeroBorg.ZeroBorg()
    zb.Init()
    debug("zb initialized")

    detector = cv.CascadeClassifier()
    detector.load('face_frontal.xml')
    debug("face detector initialized")

    return zb, detector, cap

if __name__ == "__main__":
    zb, detector, (camera, rawCapture) = init()

    try:
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            adjustMotors(image, detector, zb)
            rawCapture.truncate(0)
    except Exception as e:
        print(e)
        debug("Stopping all motors")
        zb.SetMotor1(0)
        zb.SetMotor2(0)
        zb.SetMotor3(0)
        zb.SetMotor4(0)
