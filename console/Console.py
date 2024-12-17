# MIT License
# Copyright (c) 2024 CCwhiteX

from console.contools.status import status
from console.contools.speedtg import speedtg
from console.contools.controls import ban
from console.contools.controls import admin

def status1():
    status()

def speedtg1():
    speedtg()
    
def admin1(adminid):
    admin(adminid)

def ban1(banid):
    ban(banid)

def console():
    ttys = input(">> ")
    parts = ttys.split(' ')
    if ttys == "help":
        print("""
        
#Список команд 
    status - Статус
    speedtg - Замеряет скорость соединения до серверов Telegram 
    admin {id_users} - Выдать правда администратора по ID
    ban {id_users} - Заблокировать пользователю доступ к боту по ID

        """)
        
        console()
    elif ttys == "status":
        status1()
        console()
    elif ttys == "speedtg":
        speedtg1()
        console()
    elif ttys.startswith("admin "):
        adminid = ttys.split(' ', 1)[1]
        if len(parts) > 1:
            adminid = parts[1]
            admin1(adminid)
        else:
            print("Не указан ID, правилньый ввод admin {id}")
        console()
    elif ttys.startswith("ban "):
        banid = ttys.split(' ', 1)[1]
        if len(parts) > 1:
            banid = parts[1]
            ban1(banid)
        else:
            print("Не указан ID, правильный ввод admin {id}")
        console()
    else:
        print("Команды нет! Напиши help для вывода помощи help")
        console()
    
    
