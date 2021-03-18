import sys
sys.path.append('/home/pi/zeroborg')
#import ZeroBorg3 as ZeroBorg
import ZeroBorg

import time
from multiprocessing import Process, Value, Lock

maxPower = 0.9
defaultGranularity = 0.005

motorLock = Lock()

class ZB:
	procDB = [None, None, None, None]
	
	def __init__(self):
		self.z = ZeroBorg.ZeroBorg()
		self.z.Init()

	def _setpwr(z, motorId, pwr, motorLockVal):
		motorLockVal.acquire()
		zz = z.z
		(zz.SetMotor1, zz.SetMotor2, zz.SetMotor3, zz.SetMotor4)[motorId](pwr)
		sys.stderr.write(f"{motorId} set to {pwr}\n")
		time.sleep(defaultGranularity / 2)
		motorLockVal.release()

	def _motor(self, motorId, contValue, power, granularity, motorLockVal):
		direction = maxPower if power > 0 else -maxPower
		strength = abs(power)
		
		onDur = strength * granularity
		offDur = (1 - strength) * granularity
		
		while contValue.value:
			self._setpwr(motorId, direction, motorLockVal)
			time.sleep(onDur)
			
			self._setpwr(motorId, 0, motorLockVal)
			time.sleep(offDur)
	
	def start(self, motorId, power, granularity = defaultGranularity):
		if self.procDB[motorId]:
			self.stop(motorId)
		
		contValue = Value('b', True)
		
		procHandle = Process(target = self._motor, args = (motorId, contValue, power, granularity, motorLock))
		procHandle.start()
		
		#return (procHandle, contValue)
		self.procDB[motorId] = (procHandle, contValue)
	
	def stop(self, motorId):
		try:
			procHandle, contValue = self.procDB[motorId]
			
			contValue.value = False
			procHandle.join()
		except:
			pass
		
		self.procDB[motorId] = None
	
	def killall(self):
		self.z.MotorsOff()
