import time
from datetime import datetime, timedelta 

def light():
    global minutos, now, real, temp
    temp = None
    minutos = float((datetime.now().strftime('%M'))[1:])
    now = int(datetime.now().strftime('%S'))
    real = datetime.now()
    if minutos == 0 or minutos == 5:
        temp = real - timedelta(seconds = now) - timedelta(minutes=5) + timedelta(seconds=59)
    if minutos == 1 or minutos == 6:
        temp = real - timedelta(seconds = now) - timedelta(minutes=1) + timedelta(seconds=59)
    if minutos == 2 or minutos == 7:
        temp = real - timedelta(seconds = now) - timedelta(minutes=2) + timedelta(seconds=59)
    if minutos == 3 or minutos == 8:
        temp = real - timedelta(seconds = now) - timedelta(minutes=3) + timedelta(seconds=59)
    if minutos == 4 or minutos == 9:
        temp =  real - timedelta(seconds = now) - timedelta(minutes=4) + timedelta(seconds=59)
    hh = temp.strftime("%d %m %Y %H:%M:%S")
    time_hh = time.strptime(hh,"%d %m %Y %H:%M:%S")
    time_kk = time.mktime(time_hh)
    return time_kk   

while True: print(light()), time.sleep(1)
