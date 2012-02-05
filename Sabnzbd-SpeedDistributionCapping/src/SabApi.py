import datetime
import time
import json
import urllib
from urllib.request import urlopen


def getCurrentDownloadSpeed( sabServer, sabAPIKey ):
    urlString = sabServer + "/?mode=queue&start=START&limit=LIMIT&output=json&apikey=" + sabAPIKey
    page = urlopen(urlString)
    rawURLResponse = page.read().decode('utf-8')
    page.close()
    
    jsonResult = json.loads(rawURLResponse)

    currentDownloadSpeed = jsonResult['queue']['kbpersec']

    return float(currentDownloadSpeed)

def setNewDownloadSpeed( sabServer, sabAPIKey, downloadSpeed ):
    urlString = sabServer + "/?mode=config&name=speedlimit&value=" + str(downloadSpeed) + "&apikey=" + sabAPIKey
    page = urlopen(urlString)
    readValue = page.read()
    page.close()
    return True