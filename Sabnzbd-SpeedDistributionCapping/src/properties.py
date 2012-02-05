import datetime
SabSpeedControllerHtmlFile = "SabSpeedController.html"

JAS_SAB="http://192.168.1.7:10001/sabnzbd/api"
JAS_SAB_API_KEY="33a5bebaa229673c2cc90b95b1f79f2f"

RIC_SAB="http://192.168.1.4:20001/sabnzbd/api"
RIC_SAB_API_KEY="47565d1c797e15ca93e507fccf2651aa"

LOG_APP_NAME="SAB Speed Monitor (2.0): "

HIGH_SPEED_LIMIT=1500
LOW_SPEED_LIMIT=768

NIGHT_TIME_START=datetime.time(1, 0, 0)
NIGHT_TIME_STOP=datetime.time(7, 0, 0)

WORK_TIME_START=datetime.time(9, 0, 0)
WORK_TIME_STOP=datetime.time(17, 0, 0)

TIME_BETWEEN_SAB_SPEED_CHECKS=30
TIME_BETWEEN_SAB_SPEED_CHECKS_IF_EXCEPTION=10

WEB_PORT = 20010
WEB_HOST = "192.168.1.4"
