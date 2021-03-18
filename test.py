#!/usr/bin/env python3

import time
from pwmzb import ZB

speed = 0.2

def move(z, angle):
	z.start(0, speed)
	z.start(1, -speed)
	z.start(2, speed)
	z.start(3, -speed)
	
	time.sleep(2)
	
	z.stop(0)
	z.stop(1)
	z.stop(2)
	z.stop(3)

if __name__ == "__main__":
	z = ZB()
	print("let's go")
	try:
		move(z, 0)
	except Exception as e:
		print("AAA", e)
		z.killall()
		raise(e)
