#! /usr/bin/env python

# SAB Multiple Server Monitor and Speed Abitration Script
# (c) Jaskirat Rajasansir 2010

import datetime
import time
import urllib
from SabApi import getCurrentDownloadSpeed, setNewDownloadSpeed
import SabApi
from properties import RIC_SAB, RIC_SAB_API_KEY, JAS_SAB, JAS_SAB_API_KEY,\
    LOG_APP_NAME, EXCEPTION_TIMEOUT, NIGHT_TIME_START, NIGHT_TIME_STOP,\
    LOW_SPEED_LIMIT, HIGH_SPEED_LIMIT, WORK_TIME_START, WORK_TIME_STOP,\
    SAB_CHECK_TIMEOUT
import properties
from Utility import log

class SabSpeedController(object):
    

    def getMaxDownloadMethod(self, currentTime, currentDay):
        maxDownloadSpeed = 0
        if (currentTime > NIGHT_TIME_START and currentTime < NIGHT_TIME_STOP):
            log(currentTime, " - It's night time.")
            maxDownloadSpeed = HIGH_SPEED_LIMIT
        elif (currentTime > WORK_TIME_START and currentTime < WORK_TIME_STOP):
            log(currentTime, " - It's work time.")
            maxDownloadSpeed = HIGH_SPEED_LIMIT
        else:
            log(currentTime, " - We're awake and at home.")
            maxDownloadSpeed = LOW_SPEED_LIMIT
    # 5 and 6 = Saturday and Sunday
        if ((currentDay == 5 or currentDay == 6) and not (currentTime > NIGHT_TIME_START and currentTime < NIGHT_TIME_STOP)):
            log("It's the weekend (", currentDay, ") and during the day.")
            maxDownloadSpeed = LOW_SPEED_LIMIT
        else:
            log("It's a weekday (", currentDay, ").")
        return maxDownloadSpeed


    def isSabActive(self, sabSpeed):
        return sabSpeed < 1

    def startControllingSabSpeeds(self):
        while True :
            currentTime=datetime.datetime.now().time()
            currentDay=datetime.datetime.now().weekday()
        
            try:
                jasSABSpeed = getCurrentDownloadSpeed( JAS_SAB, JAS_SAB_API_KEY )
            except IOError:
                log("**Exception**", currentTime, "I/O error trying to access Jas's SAB.")
                time.sleep(EXCEPTION_TIMEOUT)
                continue
        
            try:
                richSABSpeed = getCurrentDownloadSpeed( RIC_SAB, RIC_SAB_API_KEY )
            except IOError:
                log("**Exception**", currentTime, "I/O error trying to access Rich's SAB.")
                time.sleep(EXCEPTION_TIMEOUT)
                continue
        
            log("Jas SAB current speed:", jasSABSpeed, "kb/s\t\tRich SAB current speed:", richSABSpeed, "kb/s")
        
            maxDownloadSpeed = self.getMaxDownloadMethod(currentTime, currentDay)
        
        
            if (self.isSabActive(jasSABSpeed) and self.isSabActive(richSABSpeed)):
                log("Both servers idle. Standby.")
            elif (self.isSabActive(jasSABSpeed)):
                log("Set Jas's server to", maxDownloadSpeed, "kb/s")
                setNewDownloadSpeed( RIC_SAB, RIC_SAB_API_KEY, maxDownloadSpeed )
            elif (self.isSabActive(richSABSpeed)):
                log("Set Rich's server to", maxDownloadSpeed, "kb/s")
                setNewDownloadSpeed( JAS_SAB, JAS_SAB_API_KEY, maxDownloadSpeed )        
            else:
                log("Aggregate", maxDownloadSpeed, "kb/s evenly across both servers")
                
                aggregatedSpeed = maxDownloadSpeed / 2
        
                setNewDownloadSpeed( RIC_SAB, RIC_SAB_API_KEY, aggregatedSpeed )
                setNewDownloadSpeed( JAS_SAB, JAS_SAB_API_KEY, aggregatedSpeed )
        
            print("\n")
        
            time.sleep(SAB_CHECK_TIMEOUT)
    

