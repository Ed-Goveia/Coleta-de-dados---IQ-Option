import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("ed.mi.goveia@gmail.com","24030907*Ed*")
Iq.connect()#connect to iqoption
goal="EURUSD"
print("get candles")
print(Iq.get_candles(goal,60,111,time.time()))