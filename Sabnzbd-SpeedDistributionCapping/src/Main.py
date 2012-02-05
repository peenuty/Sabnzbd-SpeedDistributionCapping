'''
Created on Feb 5, 2012

@author: Rich
'''
import cherrypy
from SabSpeedControllerWeb import SabSpeedControllerWeb


cherrypy.quickstart(SabSpeedControllerWeb())