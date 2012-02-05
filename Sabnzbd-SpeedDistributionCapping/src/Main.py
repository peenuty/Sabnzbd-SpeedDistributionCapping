'''
Created on Feb 5, 2012

@author: Rich
'''
import cherrypy
from Utility import log
from properties import HIGH_SPEED_LIMIT, LOW_SPEED_LIMIT, RIC_SAB, JAS_SAB,\
    NIGHT_TIME_START, NIGHT_TIME_STOP, WORK_TIME_START, WORK_TIME_STOP
from SabSpeedControllerWeb import SabSpeedWebController
from SabSpeedController import SabSpeedController
import threading
from threading import Thread





def main(): 
    printStartupConfiguration();
    
    sabSpeedController = SabSpeedController()
    s= SabSpeedControllerThread(sabSpeedController)
    s.start()
    cherrypy.quickstart(SabSpeedWebController(sabSpeedController))
    
class SabSpeedControllerThread(threading.Thread):
    def __init__(self, sabSpeedController):
        #Required. http://www.daniweb.com/software-development/python/threads/170887
        Thread.__init__(self)
        self.sabSpeedController = sabSpeedController

    def run(self):
        self.sabSpeedController.startControllingSabSpeeds()

def printStartupConfiguration():
    log("--------------------------------")
    log("Initalising SAB Speed Monitor...")
    log("--------------------------------\n")

    log("Jas SAB Server: ", JAS_SAB)
    log("Rich SAB Server: ", RIC_SAB)

    log("High speed limit: ", HIGH_SPEED_LIMIT, "kb/s - Times: ", NIGHT_TIME_START, "->", NIGHT_TIME_STOP, " and ", WORK_TIME_START, "->", WORK_TIME_STOP)
    log("Low speed limit: ", LOW_SPEED_LIMIT, "kb/s at all other times\n\n")

if __name__ == "__main__":
    main()