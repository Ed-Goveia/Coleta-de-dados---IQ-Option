from datetime import datetime

def timer():
    minuts = float(((datetime.now()).strftime('%M.%S'))[1:])
    minmin = float(0)
    if minuts < 4.59 and minuts > 0.00: minmin = abs(minuts - 4.59)
    if minuts > 4.59 and minuts < 9.59: minmin = abs(minuts - 9.59)
    mk = '{:.2f}'.format(minmin)
    mmm = mk.replace(".", ":")
    return mmm
