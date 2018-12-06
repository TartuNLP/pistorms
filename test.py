#!/usr/bin/python

import sys
import time
import ZeroBorg

zb = ZeroBorg.ZeroBorg()
zb.Init()
zb.SetMotor1(1)
zb.SetMotor2(1)
zb.SetMotor3(1)
zb.SetMotor4(1)
time.sleep(0.3)
zb.SetMotor1(-1)
zb.SetMotor2(-1)
zb.SetMotor3(-1)
zb.SetMotor4(-1)
time.sleep(0.3)
zb.SetMotor1(0)
zb.SetMotor2(0)
zb.SetMotor3(0)
zb.SetMotor4(0)
print("Done!")
