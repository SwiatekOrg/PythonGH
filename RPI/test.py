from datetime import timedelta
from datetime import datetime
import time


czas = time.localtime()
print(type(czas))

czas2 = datetime.strptime("2018-03-30 1:00:00", '%Y-%m-%d %H:%M:%S')
print(type(czas2))

dt_obj = datetime.strptime("2018-03-29 20:00:00", '%Y-%m-%d %H:%M:%S')
czas = datetime.strptime((str(czas[0]) + "-" + str(czas[1]) + "-" + str(czas[2]) + " " + str(czas[3]) + ":" + str(czas[4]) + ":" + str(czas[5])), '%Y-%m-%d %H:%M:%S')
xd =czas2 - dt_obj
print(xd)
print(type(xd))