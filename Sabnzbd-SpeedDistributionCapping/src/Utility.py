from properties import LOG_APP_NAME
def log(*objectsToLog):
    print(LOG_APP_NAME + ': ' + ' '.join(str(objectToLog) for objectToLog in objectsToLog))