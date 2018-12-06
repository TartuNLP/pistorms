#!/usr/bin/python

import sys
import ZeroBorg
import time

from flask import request, Flask

zb = ZeroBorg.ZeroBorg()
zb.Init()

def fwd():
    zb.SetMotor1(0.7)
    zb.SetMotor3(-0.7)

def back():
    zb.SetMotor1(-0.7)
    zb.SetMotor3(0.7)

def right():
    zb.SetMotor1(-0.7)
    zb.SetMotor3(-0.7)

def left():
    zb.SetMotor1(0.7)
    zb.SetMotor3(0.7)

def up():
    zb.SetMotor4(0.55)

def down():
    zb.SetMotor4(-0.55)

def stop():
    zb.SetMotor1(0)
    zb.SetMotor3(0)
    zb.SetMotor4(0)

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
    left()
    return "left"

@app.route('/right', methods=["GET", "POST"])
def goRight():
    right()
    return "right"

@app.route('/up', methods=["GET", "POST"])
def doUp():
    up()
    return "up"

@app.route('/down', methods=["GET", "POST"])
def doDown():
    down()
    return "down"

@app.route('/stop', methods=["GET", "POST"])
def doStop():
    stop()
    return "stop"

def wiggle():
    for _ in range(3):
        left()
        time.sleep(0.1)
        right()
        time.sleep(0.1)
    stop()

if __name__ == "__main__":
    try:
        #wiggle()
        app.run(host='raspberrypi.local', port=9990)
    except Exception as e:
        print("Exception " + str(e))
    finally:
        stop()
