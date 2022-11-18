
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime, timedelta 
import sys
import os 
import time
import threading
import logging

while True:
    os.system("cls")
    break
logging.disable(level=(logging.DEBUG))
API = IQ_Option('ed.mi.goveia@gmail.com', '24030907*Ed*')
API.connect()

if API.check_connect():
	print(' Conectado com sucesso!')
else:
	print(' Erro ao conectar')
	input('\n\n Aperte enter para sair')
	sys.exit()

vat = 5 * 12
vel = 5 * 6
va = 5 * 3
vt = 5 * 2
vv = 5 * 1

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

try:
    while True:
        input('6\nPresssione\033[35mENTER\033[0m para análisar...\n')
        os.system("cls")
        while True: 
                hero = light()
                
                def bad(): 
                    you = API.get_all_open_time()
                    return you 
                binary = threading.Thread(target = bad)
                binary.start()
                you = bad()
                binary.join()

                for paridade in you['turbo']:
                    if you['turbo'][paridade]['open'] == True:
                        
                        win_one = 0
                        loss_one = 0
                        doji_one = 0
                        
                        while True:
                            candles = API.get_candles(paridade, 60, 60, hero)
                            break
                        
                        for index, vela in enumerate(candles):
                            
                            min = int(datetime.fromtimestamp(int(vela['from'])).strftime('%M')[1:])
                    
                            if min == 5 or min == 0 :
                                
                                cor_operacao = 'g' if vela['open'] < vela['close'] else 'r' if vela['open'] > vela['close'] else 'd'
                                
                                entrada_analise = ['g' if candles[index - i]['open'] < candles[index - i]['close'] else 'r' if candles[index - i]['open'] > candles[index - i]['close'] else 'd' for i in range(1,6)]
                                entrada_analise = False if entrada_analise.count('d') > 0 else 'g' if entrada_analise.count('r') > entrada_analise.count('g') else 'r' if entrada_analise.count('g') > entrada_analise.count('r') else False
                                
                                if entrada_analise != False:
                                
                                    if entrada_analise == cor_operacao:
                                        win_one += 1
                                        
                                    elif entrada_analise != cor_operacao:						
                                        loss_one += 1
                                            
                                else:
                                    doji_one += 1						

                        win_two = 0
                        loss_two = 0
                        doji_two = 0


                        candles = API.get_candles(paridade, 60, 30, hero)

                        for index, vela in enumerate(candles):
                            
                            min = int(datetime.fromtimestamp(int(vela['from'])).strftime('%M')[1:])
                            
                            if min == 5 or min == 0 :
                                
                                cor_operacao = 'g' if vela['open'] < vela['close'] else 'r' if vela['open'] > vela['close'] else 'd'
                                
                                entrada_analise = ['g' if candles[index - i]['open'] < candles[index - i]['close'] else 'r' if candles[index - i]['open'] > candles[index - i]['close'] else 'd' for i in range(1,6)]
                                entrada_analise = False if entrada_analise.count('d') > 0 else 'g' if entrada_analise.count('r') > entrada_analise.count('g') else 'r' if entrada_analise.count('g') > entrada_analise.count('r') else False
                                
                                if entrada_analise != False:
                                
                                    if entrada_analise == cor_operacao:
                                        win_two += 1
                                    elif entrada_analise != cor_operacao:						
                                        loss_two += 1
                                else:
                                    doji_two += 1						

                        win_three = 0
                        loss_three = 0
                        doji_three = 0

                        candles = API.get_candles(paridade, 60, 15, hero)

                        for index, vela in enumerate(candles):
                            
                            min = int(datetime.fromtimestamp(int(vela['from'])).strftime('%M')[1:])
                            
                            if min == 5 or min == 0 :
                                
                                cor_operacao = 'g' if vela['open'] < vela['close'] else 'r' if vela['open'] > vela['close'] else 'd'
                                
                                entrada_analise = ['g' if candles[index - i]['open'] < candles[index - i]['close'] else 'r' if candles[index - i]['open'] > candles[index - i]['close'] else 'd' for i in range(1,6)]
                                entrada_analise = False if entrada_analise.count('d') > 0 else 'g' if entrada_analise.count('r') > entrada_analise.count('g') else 'r' if entrada_analise.count('g') > entrada_analise.count('r') else False
                                
                                if entrada_analise != False:
                                
                                    if entrada_analise == cor_operacao:
                                        win_three += 1
                                        
                                    elif entrada_analise != cor_operacao:						
                                        loss_three += 1
                                                    
                                else:
                                    doji_three += 1						

                        win_k = 0
                        loss_k = 0
                        doji_k = 0

                        candles = API.get_candles(paridade, 60, 10, hero)

                        for index, vela in enumerate(candles):
                            
                            min = int(datetime.fromtimestamp(int(vela['from'])).strftime('%M')[1:])
                            
                            if min == 5 or min == 0 :
                                
                                cor_operacao = 'g' if vela['open'] < vela['close'] else 'r' if vela['open'] > vela['close'] else 'd'
                                
                                entrada_analise = ['g' if candles[index - i]['open'] < candles[index - i]['close'] else 'r' if candles[index - i]['open'] > candles[index - i]['close'] else 'd' for i in range(1,6)]
                                entrada_analise = False if entrada_analise.count('d') > 0 else 'g' if entrada_analise.count('r') > entrada_analise.count('g') else 'r' if entrada_analise.count('g') > entrada_analise.count('r') else False
                                
                                if entrada_analise != False:
                                
                                    if entrada_analise == cor_operacao:
                                        win_k += 1
                                        
                                    elif entrada_analise != cor_operacao:						
                                        loss_k += 1		
                                else:
                                    doji_k += 1	
                        
                        
                        win_l = 0
                        loss_l = 0
                        doji_l = 0

                        candles = API.get_candles(paridade, 60, 5, hero)

                        for index, vela in enumerate(candles):
                            
                            min = int(datetime.fromtimestamp(int(vela['from'])).strftime('%M')[1:])
                            
                            if min == 5 or min == 0 :
                                
                                cor_operacao = 'g' if vela['open'] < vela['close'] else 'r' if vela['open'] > vela['close'] else 'd'
                                
                                entrada_analise = ['g' if candles[index - i]['open'] < candles[index - i]['close'] else 'r' if candles[index - i]['open'] > candles[index - i]['close'] else 'd' for i in range(1,6)]
                                entrada_analise = False if entrada_analise.count('d') > 0 else 'g' if entrada_analise.count('r') > entrada_analise.count('g') else 'r' if entrada_analise.count('g') > entrada_analise.count('r') else False
                                
                                if entrada_analise != False:
                                
                                    if entrada_analise == cor_operacao:
                                        win_l += 1
                                    elif entrada_analise != cor_operacao:						
                                        loss_l += 1		
                                else:
                                    doji_l += 1	

                        print(f'\n\n Análise de {paridade}, finalizada:', temp )
                        print(' -----------------------------------------------------------------')
                        print(' TWELVE  \033[35m:\033[0m WIN:', win_one, ', LOSS:', loss_one,', DOJI:', doji_one,', WINRATE:','\033[35m',round(100 * ((win_one) / (win_one + loss_one))), '%','\033[0m',', TOTAL DE OPERAÇÕES:', win_one + loss_one, '')
                        print(' SIX     \033[35m:\033[0m WIN:', win_two, ', LOSS:', loss_two,', DOJI:', doji_two,', WINRATE:','\033[35m', round(100 * ((win_two) / (win_two + loss_two))), '%','\033[0m',', TOTAL DE OPERAÇÕES:', win_two + loss_two, '')
                        print(' Three   \033[35m:\033[0m WIN:', win_three, ', LOSS:', loss_three,', DOJI:', doji_three,', WINRATE:','\033[35m', round(100 * ((win_three) / (win_three + loss_three))), '%','\033[0m',', TOTAL DE OPERAÇÕES:', win_three + loss_three, '')
                        
                        if win_l == 1:
                            print(' A útima operação realizada teve como resultado uma \033[35mvitória!\033[0m \n')
                        if loss_l == 1:
                            print(' A útima operação realizada teve como resultado uma \033[35mderrota!\033[0m \n')
                        if doji_l == 1:
                            print(' A útima operação \033[35mnão pode ser realizada\033[0m! \n')
                break
        time.sleep(0.5)
except KeyboardInterrupt:
    print('Prando o robô!')
            
            