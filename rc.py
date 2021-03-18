#!/usr/bin/python3

import sys
import ZeroBorg
import time

from flask import request, Flask

zb = ZeroBorg.ZeroBorg()
zb.Init()

driveSpeed = 0.7
rotateSpeed = 0.6
diagSpeed = 0.6

def fwd(speed = driveSpeed):
    zb.SetMotor1(speed)
    zb.SetMotor2(-speed)

def back(speed = driveSpeed):
    zb.SetMotor1(-speed)
    zb.SetMotor2(speed)

def straferight(speed = driveSpeed):
    zb.SetMotor3(speed)
    zb.SetMotor4(-speed)

def strafeleft(speed = driveSpeed):
    zb.SetMotor3(-speed)
    zb.SetMotor4(speed)

def rotateleft(speed = rotateSpeed):
    zb.SetMotors(speed)

def rotateright(speed = rotateSpeed):
    zb.SetMotors(-speed)

def stop():
    zb.MotorsOff()

def loadPage(filepath):
    fh = open(filepath, 'r')
    result = fh.read()
    fh.close()
    return result

app = Flask("pistorms")

@app.route('/', methods=["GET", "POST"])
def rcPage():
    stop()
    return loadPage('rc.html')

@app.route('/fwd', methods=["GET", "POST"])
def goFwd():
    fwd()
    return "fwd" 

@app.route('/back', methods=["GET", "POST"])
def goBack():
    back()
    return "back"

@app.route('/left', methods=["GET", "POST"])
def goLeft():
    strafeleft()
    return "left"

@app.route('/right', methods=["GET", "POST"])
def goRight():
    straferight()
    return "right"

@app.route('/fwdleft', methods=["GET", "POST"])
def goFwdL():
    fwd(diagSpeed)
    strafeleft(diagSpeed)
    return "fwdleft"

@app.route('/fwdright', methods=["GET", "POST"])
def goFwdR():
    fwd(diagSpeed)
    straferight(diagSpeed)
    return "fwdright"

@app.route('/backleft', methods=["GET", "POST"])
def gobackL():
    back(diagSpeed)
    strafeleft(diagSpeed)
    return "backleft" 

@app.route('/backright', methods=["GET", "POST"])
def gobackR():
    back(diagSpeed)
    straferight(diagSpeed)
    return "backright" 

@app.route('/rotateleft', methods=["GET", "POST"])
def doUp():
    rotateleft()
    return "rotateleft"

@app.route('/rotateright', methods=["GET", "POST"])
def doDown():
    rotateright()
    return "rotateright"

@app.route('/stop', methods=["GET", "POST"])
def doStop():
    stop()
    return "stop"

def wiggle():
    for _ in range(3):
        rotateleft()
        time.sleep(0.3)
        stop()
        rotateright()
        time.sleep(0.3)
        stop()

if __name__ == "__main__":
    try:
        #wiggle()
        app.run(host='192.168.88.212', port=9990)
    except Exception as e:
        print("Exception " + str(e))
    finally:
        stop()
