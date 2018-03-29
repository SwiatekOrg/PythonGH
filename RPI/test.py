
from datetime import datetime
import time

czas = time.localtime()
dt_str = '9-24-2010 5:03:29'
dt_obj = datetime.strptime(dt_str, '%m-%d-%Y %H:%M:%S')
czas = (str(str(czas[0])+"-"+str(czas[1])+"-"+str(czas[2])+" "+str(czas[3])+":"+str(czas[4])+":"+str(czas[5])))
czas = datetime.strptime(czas,'%Y-%m-%d %H:%M:%S')
godzina1 = [dt_obj.hour,dt_obj.minute]
godzina2 = [czas.hour,czas.minute]
minuta = int( (godzina2[0]-godzina1[0])*60 + (godzina2[1]-godzina1[1]))
print(minuta)