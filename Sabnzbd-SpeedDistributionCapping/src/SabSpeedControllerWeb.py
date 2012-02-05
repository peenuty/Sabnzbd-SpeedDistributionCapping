import properties

class SabSpeedWebController(object):

    def __init__(self, sabSpeedController):
        self.sabSpeedController = sabSpeedController
        
    def index(self):
        return self.getWebHtmlContent();
    index.exposed = True
    
    def setSabSpeed(self, newSpeed=None, minutesToHaveNewSpeed=None):
        print('Speed override received from web UI:')
        print('newSpeed: ' + newSpeed)
        print('minutesToHaveNewSpeed: ' + minutesToHaveNewSpeed)
        self.sabSpeedController.createSabSpeedOverride(newSpeed, minutesToHaveNewSpeed)
        return 'Your speed override has been set (Player!)'
    setSabSpeed.exposed = True
    
    def getWebHtmlContent(self):
        webHtmlContentResult = 'There was a problem getting page html from file :('
        with open(properties.SabSpeedControllerHtmlFile, 'r') as file:
            readData = file.read()
            webHtmlContentResult = readData;
        return webHtmlContentResult
    
    
        
        
