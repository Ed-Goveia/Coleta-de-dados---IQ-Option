
import threading
from iqoptionapi.stable_api import IQ_Option
import logging
import time
from datetime import datetime
import json
import os
# limpar terminal

while True:
    os.system("cls")
    break

# Modo de conta

logging.disable(level=(logging.DEBUG))

try:
    try_login = 0
    Iq = {}
    status = False
    while status == False and try_login < 3:
        username =  "ed.mi.goveia@gmail.com"   #input("  \nUsuário: ")
        passaword = "24030907*Ed*"    #input("Senha: ")
        Iq = IQ_Option(username, passaword)
        try_login += 1
        status, reason = Iq.connect()
        if status == False:
            res = json.loads(reason)
            if "code" in res and res["code"] == "invalid_credentials":
                
                while True:
                    os.system("cls")
                    break
                print("\n\nErro ao conectar: Usuário ou senha incorreta\n\n")
            else:
                print("\n\nErro ao tentar se conectar:" +
                    res["message"] + "\n\n")

        else:
            break

    if status == False:
        raise ValueError(
            "Você Excedeu 3 tentativas. Tente novamente mais tarde \n\n")
    
    while True:
        os.system("cls")
        break
    
    def bad(): 
        you = Iq.get_all_open_time() 
        return you 
    binary = threading.Thread(target = bad)
    def payouty():
        payt = Iq.get_all_profit()
        return payt
    octal = threading.Thread(target = payouty )
    binary.start(),octal.start() 
    you = bad()
    payt = payouty()
    binary.join(), octal.join()

    while True:
        try:
            mode= int(input('\n Deseja operar na conta PRACTICE ou REAL? \n 1 - PRACTICE\n 2 - REAL\n [\033[35m...\033[0m]: ')) 
            if mode > 0 and mode < 3 : 
                os.system("cls")
                print (" Conectando... \033[0m\n")
                break
        except:
            print('\n Opção invalida')
  
    def m():
        mu = None
        if mode == 1:
            mu = "PRACTICE" 
        if mode == 2:
            mu = "REAL"
        return mu
    
    time.sleep(1)
    
    while True:
        os.system("cls")
        break
    mo = m()
    print("\n\033[1m Conectado com sucesso \033[0m\n")
    time.sleep(1)
    MODE = mo  # /"REAL"
    Iq.change_balance(MODE)
    

except ValueError as ve:
    print(ve)
    print('Parando bot')
except KeyboardInterrupt:
    print('Parando bot')

def payout(par,tipo,timeframe = 1):
    if tipo == 'turbo': return int(100 * payt[par]['turbo'])

for paridade in you['turbo']:
    if you['turbo'][paridade]['open'] == True:
        print ( f'\033[35m+ \033[0m 'f'{paridade}       ''      | Payout de  '+str(payout(paridade, 'turbo'))+'%')

