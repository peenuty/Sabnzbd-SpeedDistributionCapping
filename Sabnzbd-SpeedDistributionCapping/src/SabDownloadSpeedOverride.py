import datetime
from datetime import timedelta
class SabDownloadSpeedOverride(object):
    
    def __init__(self, newSpeed, timeForNewSpeedToBeEffectiveInMins):
        self.newSpeed = int(newSpeed)
        self.timeForNewSpeedToBeEffectiveUntil = datetime.datetime.now() + timedelta(minutes=int(timeForNewSpeedToBeEffectiveInMins))

    def getOverriddenDownloadSpeed(self):
        overriddenDownloadSpeed = -1
        if(self.timeForNewSpeedToBeEffectiveUntil > datetime.datetime.now()):
            overriddenDownloadSpeed = self.newSpeed
        return overriddenDownloadSpeed
    
    def isSpeedOverridden(self):
        return self.getOverriddenDownloadSpeed() > -1