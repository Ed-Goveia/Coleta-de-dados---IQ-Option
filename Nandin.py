from signal import SIGABRT, signal
from iqoptionapi.stable_api import IQ_Option
import logging
import time
from datetime import datetime,timedelta
import pandas as pd
import json
import sys
from candlestick import candlestick
import os
import threading



# OTC em M1
# limpar terminal


os.system("clear")
 
# Modo de conta
logging.disable(level=(logging.DEBUG))

def slide(frase,velocidade):
    for i in list(frase):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(velocidade)

try:
    ap_ini = "..."
    for i in range(2): 
        slide(ap_ini,0.5)
        os.system("clear")
    
    os.system("clear")
    ola = "Olá, tudo bem?"
    slide(ola, 0.2)
    time.sleep(1)
    os.system("clear")
    lets_go = "Vamos começar?"
    slide(lets_go,0.12)
    time.sleep(1)
    os.system("clear")
    ap_user = "Por favor, digite seu Email e senha usados na sua conta da Iq Option \n"
    slide(ap_user,0.08)
    time.sleep(1)
    try_login = 0
    Iq = {}
    status = False
    while status == False and try_login < 3:
        username =  input (' \nUsarname: ')   #input("  \nUsuário: ")
        passaword = input (' \nPassaword: ' )   #input("Senha: ")
        
        os.system("clear")
        connec = "Conectando"
        slide(connec,0.1),slide(ap_ini,0.3)

        Iq = IQ_Option(username, passaword)
        try_login += 1
        status, reason = Iq.connect()
        if status == False:
            ress = json.loads(reason)
            if "code" in ress and ress["code"] == "invalid_credentials":
                
                while True:
                    os.system("clear")
                    break
                print (f' Tentativa {try_login + 1}')
                print("\n\nErro ao conectar: Usuário ou senha incorreta\n\n")
            else:
                print("\n\nErro ao tentar se conectar:" +
                    res["message"] + "\n\n")

        else:
            break

    if status == False:
        print("Você Excedeu 3 tentativas. Tente novamente mais tarde \n\n")
        input('\n\n\nPressione ENTER para sair!')
        sys.exit()

    
    while True:
        os.system("clear")
        break
    os.system("clear")
    print(' Conectado com sucesso!')
    time.sleep(2)
    while True:
        try:
            mode= int(input('\n\033[35m+\033[0m Deseja operar na conta PRACTICE ou REAL? \n 1 - PRACTICE\n 2 - REAL\n [\033[35m...\033[0m]: ')) 
            if mode > 0 and mode < 3 : 
                os.system("clear")
                break
        except:
            os.system("clear")
            print('\n Opção invalida')
  
    def m():
        mu = None
        if mode == 1:
            mu = "PRACTICE" 
        if mode == 2:
            mu = "REAL"
        return mu
    
    
    while True:
        os.system("clear")
        break
    mo = m()
    
    MODE = mo  # /"REAL"
    Iq.change_balance(MODE)

    

except ValueError as ve:
    print(ve)
    print('Parando bot')
except KeyboardInterrupt:
    print('Parando bot')

while True:
    try:
        print(' Pressione para 0 para pular a introdução ou 1 para uma breve introdução...')
        duc = int(input(' [\033[35m...\033[0m]: '))
        if duc >= 0 and duc <= 1:
            break
    except:
        print('Opção inválida!')
    
# tipo de conta

def perfil():
    perfil = json.loads(json.dumps(Iq.get_profile_ansyc()))
    return perfil

x = perfil()
banca = round(int(Iq.get_balance()))
name = x['name']

frame = 1
timeframe = frame * 60 # para pegar os candles
expirations_mode = frame
total = 0

os.system("clear")
while True:
    
    
    # Valor de entrada
    print(f' [ VALOR DE ENTRADA ]')
    time.sleep(0.5)
    
    while True:
        if duc == 0: break
        print('\n')
        ap_entrada = " Valor usado para executar suas operações."
        dica_entrada = " Dica : Uma recomedação válida pode ser fazer entradas com um valor aproximado ou menor que 3% da sua banca."
        slide(ap_entrada,0.05), print('\n'), slide(dica_entrada,0.01),print('\n'), time.sleep(0.5)
        break
    time.sleep(0.5)
   
    while True:
        try:

            ini_buy_amount = float(input('\n\033[35m+\033[0m Defina o valor que deseja usar para as entradas: '))
            break
        except:
            os.system("clear")
            print('Opcão Inválida!')
    
    os.system("clear")
    
    # Configuração Stop WIN
    
    print(f' [ STOP WIN ]')
    time.sleep(0.5)
    while True:
        if duc == 0: break
        print('\n')
        ap_stop_win = " Stop win é uma função estratégica que usa um valor de ganho definido por você, para parar a execução do robô quando esse valor é alcançado."
        dica = " Dica: Definir um Stop win razoável faz com que você tenha possíveis resultados consistentes."
        slide(ap_stop_win,0.03), print('\n'), time.sleep(0.5), slide(dica,0.005),print('\n')
        break
    time.sleep(0.5)
    
    while True:
        try:
            stop_gain = int(input(f'\n\033[35m + \033[0mDefina o valor de Stop Win: '))
            break
        except:
            os.system("clear")
            print('Opcão Inválida!')
    
    os.system("clear")
    
    # Configuração de stop loss
    print(f' [ STOP LOSS ]')
    time.sleep(0.5)
    
    while True:
        if duc == 0: break
        print('\n')
        ap_stop_loss = " O Stop loss é uma função estratégica que usa um valor de perda definido por você, para parar a execução do robô quando esse valor é alcançado."
        ap_stop_loss_frase = "'' Melhor que saber operar, é saber a hora de não operar.'' "  
        print('\n'),slide(ap_stop_loss,0.03), print('\n'), slide(ap_stop_loss_frase, 0.04), print('\n'),time.sleep(0.5)
        break
    
    while True:
        try:
            stop_loss = (int(input('\n\033[35m+\033[0m Defina o valor de Stop Loss: ')))* - 1
            break
        except:
            os.system("clear")
            print('Opcão Inválida!')
      
    #Ánalise de micro-tendência

    v = 5 # Parâmetro MHi 

    # Parametros de gerenciamento

    buy_amount = ini_buy_amount
    last_loss = 0
    last_gale = 0


    # Tipo de ciclo (recuperação // fator martigale)
    
    os.system("clear")
    print(f' [ RECUPERAÇÃO ]')
    time.sleep(0.5)
    while True:
        if duc == 0: break
        print('\n')
        ap_recuperação = " As estratégias de recuperação tem a função de tentar manter a liquidez de seus reultados, visando alcançar suas metas de lucro."
        print('\n'), slide(ap_recuperação, 0.05),print('\n'), time.sleep(0.5)
        dej = " O que acha de usar recuperação?"
        slide(dej,0.05), print('\n')
        break

    while True:
        try:
            global max_gales
            
            tipe_cicle = 0
            max_gales = 0
            einstein = 0
            init = int(input('\n 0 - não desejo utilizar \n 1 - desejo utilizar \n [\033[35m...\033[0m]: '))
            if init == 0 or init == 1: 
                os.system("clear")
                break
            else:
                os.system("clear")
                print('\n Opção invalida')
        except:
            os.system("clear")
            print('\n Error')
    
    while True:
        if init == 0 : break
        print (f' TIPOS DE RECUPERAÇÃO:')
        break
    
    while True:
        if duc == 0: break
        print('\n')
        ciclos = " na próxima operação há reajuste no valor de entrada visando recuperar valor perdido na(s) última(s) entrada(s)."
        print(f' CICLOS     :',end =''), slide(ciclos,0.01), print('\n'), time.sleep(0.5)
        mars = " na próxima operação há reajuste no valor de entrada visando recuperar valor perdido na(s) última(s) entrada(s) e ainda obter lucro."
        print (f' MARS       :',end = '' ), slide(mars,0.01), print('\n'), time.sleep(0.5)
        mart = " na próxima vela há reajuste no valor de entrada visando recuperar valor perdido na(s) última(s) entrada(s) e obter lucro."
        print (f' MARTINGALE :',end= ''),slide(mart, 0.01),print('\n'), time.sleep(0.5) 
        break
    
    while True:        
        if init == 0: break
    
        tipe_cicle = int(input('\n\033[35m+\033[0m Em que modo deseja operar?\n 1 - Ciclo \n 2 - MARS \n 3 - Martingale \n [\033[35m...\033[0m]: ')) 
        if tipe_cicle > 0 and tipe_cicle < 4: break
        
        else:
            os.system("clear")
            print('\n Opção invalida')
    
    while True:
        if init == 0: break
        os.system("clear")
        time.sleep(0.5)
        print(' [ NÍVEL DE RECUPERÇÃO ]')
        time.sleep(0.5)
        break
        
    while True:
        if init == 0: break
        try:
            max_gales += int(input('\n\033[35m+\033[0m Indique a quantidade de niveis: '))
            if tipe_cicle == 3: einstein = max_gales
            elif tipe_cicle != 3: einstein = 0
            break
        except: 
            os.system("clear")
            print('\n Opção invalida')
        break
        

    # Definição de buy_amount de delay
    
    os.system("clear")
    print(' [ DELAY ]')
    time.sleep(0.5)
    while True:
        try:
            Delay = int(input('\n\n\033[35m+\033[0m Deseja efetuar operações com quantos segundos de delay?\n [\033[35m...\033[0m]: '))
            if Delay > 0 and Delay < 31 : 
                break
        except Delay > 30:
            os.system("clear")
            print('\n Opção invalida')
        except:
            os.system("clear")
            print('\n Opção invalida')
    break

# Operação para definir delay

delay = Delay / 100

# parâmetro para inversão:
f = 2 # Yoshi // Darvin
t = 3 # Float // Aqua
o = 1
q = 4

# Fator de velas para serem avaliadas (Macro tendência)

vel_a = 15

# Limpar terminal




def scan():
    while True:
        while True:
            os.system("clear")
            break
        print(f'Conectado em: {username}\nUtilizando sua conta \033[34m{str(mo)}\033[0m\n\n')
        time.sleep(0.5)
        nami = f'Olá {str(name)},'
        nami_conf = "essas são suas configurações:"
        slide(nami,0.1), time.sleep(0.5),slide(nami_conf,0.1), time.sleep(0.5)
        
        print(f'\n\n')
        time.sleep(0.6)
        print(f'Conta tipo            :\033[0m {str(mo)} \033[0m')
        time.sleep(0.6)
        print(f'Banca inicial:        :\033[35m {banca}\033[0m')
        time.sleep(0.6)
        print(f'DELAY                 :\033[36m {Delay}\033[0m segundo(s)')
        time.sleep(0.6)
        print(f'Valor de entrada      :\033[36m {ini_buy_amount}\033[0m')
        time.sleep(0.5)
        print(f'Valor de stop gain    :\033[36m {stop_gain}\033[0m')
        time.sleep(0.5)
        print(f'Valor de stop loss    :\033[35m {stop_loss}\033[0m')
        time.sleep(0.5)
        if tipe_cicle == 0:
            print(f'Utlilizar recuperação :\033[35m DESATIVADO\033[0m ')
        if tipe_cicle == 1:
            print(f'Utlilizar Recuperação :\033[34m ATIVADO\033[0m, em modo de RECUPERAÇÃO de {max_gales} nývel(s) ')
        if tipe_cicle == 2:
            print(f'Utlilizar Recuperação :\033[34m ATIVADO\033[0m, em modo de MARS de {max_gales} nível(s)')
        if tipe_cicle == 3:
            print(f'Utlilizar Recuperação :\033[34m ATIVADO\033[0m, em modo de MARTIGALE de {max_gales} nível(s)')
        time.sleep(0.5)
        print(f'\n\n Qual par deseja operar?')
        break

ak = threading.Thread(target=scan)
ak.start()
ak.join()


def bad(): 
    you = Iq.get_all_open_time() 
    return you 
binary = threading.Thread(target = bad)

def payouty():
    payt = Iq.get_all_profit()
    return payt

octal = threading.Thread(target = payouty)
binary.start(),octal.start() 

you = bad()
payt = payouty()
binary.join(), octal.join()

def payout(par,tipo,timeframe = 1):
    if tipo == 'turbo': return int(100 * payt[par]['turbo'])
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
while True:
    hero = light()
    for paridade in you['turbo']:
        if you['turbo'][paridade]['open'] == True:
            
            win_one = 0
            loss_one = 0
            doji_one = 0
            
            while True:
                candles = Iq.get_candles(paridade, 60, 60, hero)
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
            
            winrate = round(100 * ((win_one) / (win_one + loss_one)))
            print ( f'\033[35m+ \033[0m {paridade}             | Payout de  {str(payout(paridade,"turbo"))}%, assertividade de {winrate}%, e {doji_one} operações canceladas')
            time.sleep(0.3)
    break

print('\n')
while True:
    try:
        goal = input(' [\033[35m...\033[0m]: ').upper()    #upper: torna a escrita maiúscula   
        def payout():
            global Iq, goal
            return Iq.get_all_profit ()[goal]['turbo']
        if payout() == {}:
            print(' Opção inválida!')
        else: break
    except: 
        print('Error')
            

        
print('\n')

time.sleep (1)
#função de coleta de candles

def get_data(candles_amount):
    global timeframe, goal
    df = pd.DataFrame()
    candles = []
    candles = Iq.get_candles(goal, timeframe, candles_amount, time.time())
    df = pd.concat([pd.DataFrame(candles), df], ignore_index=True)
    return df

# Função de stop 
    
def stops():
    global total, stop_gain, stop_loss
    
    if total >= stop_gain:
        print (f' Lucro geral: {total}')
        print("\n\n Stop Gain : YAH HUUUU! Mit sumi Luig- i! \n\n")
        input(' Pressione \033[35mENTER\033[0m para Sair!')
        sys.exit()

    if total <= stop_loss:
        print (f' Lucro geral: {total}')
        print("\n\n Stop loss : Game Over!") 
        input(' Pressione \033[35mENTER\033[0m para Sair!')
        sys.exit()

#  Função mhi  - Enumeração base

def mhi(opened, closed):
    
    global r, g, doji, r_q, g_q, doji_q, doji_lu,g_t, r_t,r_last, g_last, r_a, g_a
    
    candles_null = Iq.get_candles(goal,timeframe,5,time.time())
    candles_data = pd.DataFrame.from_dict(candles_null)
    candles_data.rename(columns={"max":"high","min":"low"}, inplace = True)

    doji_lu = 0

    null_doji = candlestick.doji(candles_data, target='result')
    l_doji = null_doji.to_dict('records')
    for data in l_doji:
        if data['result'] == True:
            doji_lu += 1
        
    # Enumeração base Mhi

    last_v_open = opened.tail(v)
    last_v_close = closed.tail(v)
    
    r = 0
    g = 0
    doji = 0
    
    for idx, val in enumerate(last_v_open):
        if last_v_open.iloc[idx] > last_v_close.iloc[idx]:
            r += 1
        elif last_v_open.iloc[idx] < last_v_close.iloc[idx]:
            g += 1
        else:
            doji += 1
    
    signal = None

    #Decisão de minoria    
    
        
    global r_a, g_a, doji_a, g_p, r_p, r_y, g_y, g_one, r_one
    
    r_a = 0
    g_a = 0
    doji_a = 0
    
    # count
    
    for idx, val in enumerate(opened):
        if opened.iloc[idx] > closed.iloc[idx]:
            r_a += 1
        elif opened.iloc[idx] < closed.iloc[idx]:
            g_a += 1
        else:
            doji_a += 1
    
    r_y = 0
    g_y = 0
    r_p = 0
    g_p = 0

    if g_a > r_a:
        if r > g : g_y = g_a - r
        if g > r : g_y = g_a - g
    else: g_y = g_a 
    
    if r_a > g_a:
        if r > g : r_y = r_a - r
        if g > r: r_y = r_a - g
    else: r_y = r_a
    
    if r > g :r_p = r_a - g
    else: r_p = r_a
    
    if g > r : g_p = g_a - r    
    else: g_p = g_a
    
    if tipe_cicle !=3 or last_gale == 0:
        print(f'MT R:{r_a} G:{g_a} D:{doji_a}    TP R:{r_p} G:{g_p} D:{doji_a}     TR R:{r_y} G:{g_y} D:{doji_a}      MiC R:{r} G:{g} D:{doji}     Doj: {doji_lu}            ')
        print(f'----------------+-------------------+-------------------+------------------+----------------')
       
       
# Enumeração para inversão:

    last_f_open = opened.tail(f)
    last_f_close = closed.tail(f)
    
    global r_last, g_last
    
    r_last = 0
    g_last = 0
    doji_last = 0
    
    for idx, val in enumerate(last_f_open):
        if last_f_open.iloc[idx] > last_f_close.iloc[idx]:
            r_last += 1
        elif last_f_open.iloc[idx] < last_f_close.iloc[idx]:
            g_last += 1
        else:
            doji_last += 1
    
    signal = None
    
    
# Enumeração 4:

    last_q_open = opened.tail(q)
    last_q_close = closed.tail(q)
    
    r_q = 0
    g_q = 0
    doji_q = 0
    
    for idx, val in enumerate(last_q_open):
        if last_q_open.iloc[idx] > last_q_close.iloc[idx]:
            r_q += 1
        elif last_q_open.iloc[idx] < last_q_close.iloc[idx]:
            g_q += 1
        else:
            doji_q += 1

    signal = None

# Enumeração 3

    last_t_open = opened.tail(t)
    last_t_close = closed.tail(t)
    global r_t, g_t
    r_t = 0
    g_t = 0
    doji_t = 0
    
    for idx, val in enumerate(last_t_open):
        if last_t_open.iloc[idx] > last_t_close.iloc[idx]:
            r_t += 1
        elif last_t_open.iloc[idx] < last_t_close.iloc[idx]:
            g_t += 1
        else:
            doji_t += 1
    
    signal = None
    
    # enumeração

    last_o_open = opened.tail(o)
    last_o_close = closed.tail(o)

    r_one = 0
    g_one = 0
    doji_one = 0
    
    for idx, val in enumerate(last_o_open):
        if last_o_open.iloc[idx] > last_o_close.iloc[idx]:
            r_one += 1
        elif last_o_open.iloc[idx] < last_o_close.iloc[idx]:
            g_one += 1
        else:
            doji_one += 1
    
    signal = None

    if r_a >= 13:
        if doji_lu == 0: signal = 'call'
    if g_a >= 13:
        if doji_lu == 0: signal = 'put'
        
    if r_a == 12: signal = 'call'
    if g_a == 12: signal = 'put'
    
    if doji_lu <= 1 :
        if g_q < 4 and r_q < 4:
            if r_a >= 11: signal = 'call'
            if g_a >= 11: signal = 'put'

    if r == 5: 
        if r_a - 1 == g_a or g_a - 1 == r_a:
            if r_a > g_a: signal = 'put'
            if g_a > r_a: signal = 'call'
        
        if r_a - 1 > g_a or g_a - 1 > g_a:
            if r_a < 10 and g_a < 10:
                if doji_lu == 0: signal = 'call'
            if doji_lu == 0:
                if r_a == 10: signal = 'put'
            if doji_lu <= 1:
                if r_a > 11: signal = 'call'
            if r_a == 11:
                if doji_lu == 1:
                    signal = 'put'
                if doji_lu == 0:
                    signal = 'call'
    if g == 5:
        
        if r_a - 1 == g_a or g_a - 1 == r_a:
            if r_a > g_a: signal = 'put'
            if g_a > r_a: signal = 'call'
        if r_a - 1 > g_a or g_a - 1 > g_a:
            if r_a < 10 and g_a < 10:
                if doji_lu == 0: signal = 'put'
            if doji_lu == 1: 
                if g_a == 10: signal = 'put'
            if doji_lu == 0:
                if g_a == 10: signal = 'call'
            if doji_lu <=1:
                if g_a > 11: signal = 'put'
            if g_a == 11:
                if doji_lu == 1:
                    signal = 'put'
                if doji_lu == 0:
                    signal = 'call'            
    
    if r_a < 11 and g_a < 11:
        if r < 5 and g < 5: # doji operacional
            if doji == 0:
                if doji_lu <=1:

                    if r_p - 1 > g_p: signal = 'put'
                    if g_p - 1 > r_p: signal = 'call'
                    
                    if r_p - 1 == g_p or g_p - 1 == r_p:
                        if g_y > r_y: signal = 'call'
                        if r_y > g_y: signal = 'put'
                    
                    if g_p == r_p: 
                        if g_a > r_a: signal = 'call'
                        if r_a > g_a: signal = 'put'
                    
                    else:
                        if g_a > r_a: signal = 'call'
                        if r_a > g_a: signal ='put'               
    return signal 

time.sleep(0.5)

def scan_mhi():

    if doji > 0 or doji_lu >= 2: a = 'False'
    if r == 5: a = " Full \033[31mR \033[0m"
    if g == 5: a = " Full \033[32mG \033[0m"
    
    if r < 5 and g < 5: # doji operacional
        if doji == 0:
            if doji_lu <= 1:
                
                # Padrão - # G R R R R ---força
                
                if r_q == 4: a = " \033[32mG \033[31mR R R R \033[0m" 
                    
                # Padrão - R G G G G --- força
                
                if g_q == 4: a = " \033[31mR \033[32mG G G G \033[0m " 
                    

                if g_q < 4:
                    
                    # Padrões de inversão
                    
                    if g_q == 3 and g_t == 3:   
                        
                        # Padrão - R R G G G --- inversão para minoria (saturada)
                        if g == 3: a = " \033[31mR R \033[32mG G G \033[0m " 
                        
                        # Padrão - G R G G G --- inversão

                        if g == 4:
                            if r_q == 1: a = " \033[32mG \033[31mR \033[32mG G G \033[0m" 

                    # Padrões de G
                    if g_t < 3:
                        
                        # Padrões de força
                        # Respectivamente - G G G G R , G G R G G --- força sem filtro -- ult mud
                        if g == 4:
                            if r_one == 1: a = " \033[32m G G G G \033[31mR \033[0m" 
                            
                            if r_t == 1 and g_last ==2: a = " \033[32mG G \033[31mR \033[32mG G \033[0m" 
                        
                        # Padrão - G G G R G --- minoria
                            
                            if g_q == 3 and r_last == 1 and g_one == 1:a = " \033[32mG G G \033[31mR \033[32mG \033[0m"
                                                        
                        #Padrões comuns
                        
                        if g ==3:
                            
                            # Padrão -  G G G R R --- inversão para maioria(saturada)
                            if r_last == 2: a = " \033[32mG G G \033[31mR R \033[0m"  
                            
                            # Padrão - G G R G R --- maioria
                        
                            if r_t == 2 and g_last==1 and r_one == 1: a = " \033[32mG G \033[31mR \033[32mG \033[31mR \033[0m" 

                            # Outros padrões :
                            
                            # Padrão - R G G G R --- força
                            
                            if g_q == 3 and r_one == 1:a = " \033[31mR \033[32mG G G \033[31mR \033[0m" 
                            
                            # Padrão - G R G G R --- maioria 

                            if g_q == 2 and g_t == 2 and r_one == 1: a = ' \033[32mG \033[31mR \033[32mG G \033[31mR \033[0m'
                            
                            # Padrão - # G G R R G --- maioria
                                
                            if r_t==2 and g_one == 1:a = " \033[32mG G \033[31mR R \033[32mG \033[0m" 
                        
                            # Padrão - R G G R G --- minoria 

                            if g_q == 3 and r_last == 1 and g_one == 1:a = " \033[31mR \033[32mG G \033[31mR \033[32mG \033[0m"
                            
                            # Padrão - G R G R G --- indecisão
                            if g_t == 2 and r_last == 1 and g_one == 1: 
                                if r_q == 2:a = " \033[32mG \033[31mR \033[32mG \033[31mR \033[32mG \033[0m" 

                            # Padrão - G R R G G --- maioria // inversão mai
                            
                            if g_last == 2 and g_t == 2:
                                if r_q == 2: a = " \033[32mG \033[31mR R \033[32mG G \033[0m " 
                            
                            #Padrão R G R G G --- inversão mi // minoria 
                                
                                if r_t == 1 and g_q == 3:a = " \033[31mR \033[32mG \033[31mR \033[32mG G \033[0m " 
                
                if r_q < 4:
                    
                    if r_q == 3 and r_t == 3:     
                        
                        # Padrão - G G R R R --- inversão para minoria (saturada)

                        if r == 3:a = " \033[32mG G \033[31mR R R  \033[0m " 
                            
                        # Padrâo - R G R R R --- inversão
                        
                        if r == 4:
                            if g_q == 1: a = " \033[31mR \033[32mG \033[31mR R R \033[0m" 
                    
                    if r_t < 3:
                        
                        #Padrões de força:
                        # Padrões, respectivamente, R R R R G, R R G R R ---força 
                        if r == 4:
                            if g_one == 1: a = " \033[31mR R R R \033[32mG \033[0m" 
                            
                            if g_t == 1 and r_last == 2: a = " \033[31mR R \033[32mG \033[31mR R \033[0m" 
                
                        # Padrão - R R R G R --- min 
                            
                            if g_last == 1 and r_one == 1: a = " \033[31mR R R \033[32mG \033[31mR \033[0m" 
                    
                        # Padrões comuns
                        
                        if r == 3:
                            # Padrão - R R R G G --- inversão para maioria (saturada)
                            if g_last == 2: a = " \033[31mR R R \033[32mG G \033[0m " 
                            
                            # Padrão -  G R R G R --- maioria
                            
                            if r_q == 3 and g_last==1 and r_one == 1: a = " \033[32mG \033[31mR R \033[32mG \033[31mR \033[0m" 

                            # Padrão - R G R G R ---  indecisão 

                            if r_q == 2 and r_t == 2 and g_last == 1 and r_one == 1: a = " \033[31mR \033[32mG \033[31mR \033[32mG \033[31mR \033[0m" 

                            # Padrão - R R G R G - - - maioria
                            
                            if g_t==2 and r_last==1 and g_one ==1:  a = " \033[31mR R \033[32mG \033[31mR \033[32mG \033[0m" 
                            
                            # Outros padrões:

                            # Padrão - R G R R G --- maioria 
                            if r_q == 2 and r_t==2 and g_one == 1 and g_q == 2:  a = " \033[31mR \033[32mG \033[31mR R \033[32mG \033[0m" 
                            
                            # Padrão -  G R R R G --- força 
                            if r_q == 3 and g_one == 1: a = " \033[32mG \033[31mR R R \033[32mG \033[0m " 
                        
                            
                            # Padrão - R R G G R --- inversão// minoria
                            if g_t == 2 and r_one == 1: a = " \033[31mR R \033[32mG G \033[31mR \033[0m" 
                                
                            # Padrao - R G G R R --- maioria // inversão para minoria
                            if r_last == 2 and r_t ==2:
                                if g_q == 2: a = " \033[31mR \033[32mG G \033[31mR R \033[0m" 
                            
                            # Padrão - G R G R R --- inversão  
                                if r_q == 3 and g_t ==1:
                                    if r_last == 2:  a = " \033[32mG \033[31mR \033[32mG \033[31mR R \033[0m "
    return a

## Função Martingale no próximo sinal (sistema de ciclo de recuperação)

def martingale(resultado, payout=0):
    #payout em decimal,ex: 0.87
    global ini_buy_amount, buy_amount, last_loss, last_gale
    
   
    if last_gale < max_gales and resultado < 0:
        last_gale += 1
        if tipe_cicle == 1:
            buy_amount = round((abs(last_loss) / float(payout)),2)     
        if tipe_cicle == 2: 
            buy_amount = round(round((abs(last_loss) / float(payout)),2) + round((abs(ini_buy_amount)),2),2) 
        if tipe_cicle == 3:
            buy_amount = round(round((abs(last_loss) / float(payout)),2) + round((abs(ini_buy_amount)),2),2) 
            
    elif resultado > 0 or last_gale >= max_gales:
        buy_amount = ini_buy_amount
        last_gale = 0
        last_loss = 0
    else: 
        buy_amount = ini_buy_amount
        last_gale = 0
        last_loss = 0

                    

# função de entrada

def is_time():
    global enter
    minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
    enter = False
    if minutos == 4.59 - delay or minutos == 9.59 - delay:
        enter = True
    return enter

# Função payout

def payouti():
    global Iq, goal
    return Iq.get_all_profit ()[goal]['turbo']

def check_order(order_check, order_id):
    global total, last_loss,pay_conv
    if order_check:
        result = Iq.check_binary_order(order_id)
        if result['result']:
            res = round(float(result['profit_amount']) -
                        float(result['amount']), 2)
            total = round(total + res, 2)
            if res > 0:
                last_loss = 0
            elif res < 0:
                last_loss += round(float(res), 2)
            elif res == 0:
                last_loss = 0
            return res
        return None

def rex():
    
    if res is None: 
        b = f' Paridade Fechada!                                         '
    if res is not None:
        if res > 0:
            b = f'        \033[32mWin\033[0m: {res}      \n\n\n'
        
        elif res < 0:
            if max_gales == 0: b = f'      \033[31mLoss\033[0m: {res}     \n\n\n'
            if max_gales > 0:
                if tipe_cicle == 3 and last_gale < max_gales:
                    b = f'        \033[31mLoss\033[0m: {res}          '
                if tipe_cicle != 3 or max_gales == last_gale:
                    b = f'        \033[31mLoss\033[0m: {res}         \n\n\n'
        elif res == 0:
            b = f'        \033[37mDoji\033[0m: {res}        \n\n\n'
        return b

def timer():
    minuts = float(((datetime.now()).strftime('%M.%S'))[1:])
    minmin = float(0)
    if minuts < 4.59 and minuts > 0.00: minmin = abs(minuts - 4.59)
    if minuts > 4.59 and minuts < 9.59: minmin = abs(minuts - 9.59)
    mk = '{:.2f}'.format(minmin)
    mmm = mk.replace(".", ":")
    return mmm

def ted():
    
    shit = None
   
    if g_a == 10: shit = True
    if r_a == 10: shit = False
    return shit
try:
    while True:
        
        if not is_time():
            print(f'* Analisando operações, possível entrada em {timer()}, lucro geral: {float(total)}', end ='\r')
        
        if is_time():
            data = get_data(vel_a)
            opened = data['open']
            closed = data['close']
            pay_conv = float(payouti()*100.0)
            if tipe_cicle != 3 or last_gale == 0:
                print('\033[37mAnálise finalizada\033[0m: ',datetime.now().strftime('%H:%M:%S'),f'                                                Payout: {pay_conv}%             ')
                print(f'----------------+-------------------+-------------------+------------------+----------------')     
            signal = mhi(opened, closed)
            esc = ted()
            
            if signal is None:
                while True:
                    print(f'Sinal: ',f'\033[35m{signal}\033[0m      {scan_mhi()} \n\n')
                    break
            
            if signal is not None:
                for i in range (einstein + 1):
                    
                    if einstein > 0 and last_gale > 0: 
                        print(f'----------------+-------------------+-------------------+------------------+----------------')
                    
                    while True:
                        order_check, order_id = Iq.buy(
                            buy_amount, goal, signal, expirations_mode)
                        
                        from time import time as tm
                        tempoAEsperar= 58 #Espera por ...
                        start = tm()
                        
                        while (tm()-start < tempoAEsperar):
                            print(f'* Operação em andamento, {timer()}, lucro geral: {total}', end ='\r')
                            time.sleep(0.5)  
                        res = check_order(order_check, order_id)
                        
                        break
                    
                    if res is None: rex()
                        
                    
                    if res is not None:
                        if signal == 'put' : print(f'{scan_mhi()}       Ação: {signal}             Ciclo: {last_gale}           com: {buy_amount} {rex()}')
                        if signal == 'call': print(f'{scan_mhi()}       Ação: {signal}            Ciclo: {last_gale}           com: {buy_amount} {rex()}')
        
                        stops()      
                        
                        if tipe_cicle == 3:
                            if res < 0 :
                                if signal == 'call':
                                    if esc is True : 
                                        buy_amount = round((abs(last_loss) / float(payouti())),2)     
                                        signal = 'put'
                                        
                                    if esc is False:
                                        buy_amount = ini_buy_amount
                                        last_gale = int(0)
                                        last_loss = float(0) 
                                        print('\n\n')
                                        break
                                
                                if signal == 'put':
                                    if esc is False:
                                        buy_amount = round((abs(last_loss) / float(payouti())),2)   
                                        signal = 'call'
                                    
                                    if esc is True:
                                        buy_amount = ini_buy_amount
                                        last_gale = int(0)
                                        last_loss = float(0)
                                        print('\n\n')
                                        break
                        
                        if res is not None:
                            if i < (einstein + 1):
                                pay = payouti()
                                martingale(res, pay)
                                enter = False
                            else: buy_amount = ini_buy_amount
                        if res >= 0 : break 
        time.sleep(0.5)
except KeyboardInterrupt:
    print('Parando o Robô!                                                               ')
    
    





