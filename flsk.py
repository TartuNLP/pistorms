#!/usr/bin/python

import sys

from flask import request, Flask

def loadPage(filepath):
	fh = open(filepath, 'r')
	result = fh.read()
	fh.close()
	return result

app = Flask("pistorms")

@app.route('/', methods=["GET", "POST"])
def rcPage():
	return loadPage('rc.html')

@app.route('/fwd', methods=["GET", "POST"])
def goFwd():
	return "fwd" 

@app.route('/back', methods=["GET", "POST"])
def goBack():
	return "back"

@app.route('/left', methods=["GET", "POST"])
def goLeft():
	return "left"

@app.route('/right', methods=["GET", "POST"])
def goRight():
	return "right"

@app.route('/up', methods=["GET", "POST"])
def doUp():
	return "up"

@app.route('/down', methods=["GET", "POST"])
def doDown():
	return "down"

@app.route('/stop', methods=["GET", "POST"])
def stop():
	return "HOHOHO"

if __name__ == "__main__":
	app.run(host='localhost', port=9999)
