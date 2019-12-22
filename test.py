#!/usr/bin/python

import sys
import time
import ZeroBorg

class Zbg:
	def __init__(self):
		self.zb = ZeroBorg.ZeroBorg()
		self.zb.Init()
	
	def stop(self):
		self.zb.SetMotor1(0)
		self.zb.SetMotor2(0)
		self.zb.SetMotor3(0)
		self.zb.SetMotor4(0)
	
	def movet(self, d1, d2, d3, t = 1):
		zb.SetMotor1(d1)
		zb.SetMotor3(d2)
		zb.SetMotor4(d3)
		
		time.sleep(t)
		
		self.stop()
