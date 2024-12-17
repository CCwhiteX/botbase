# MIT License
# Copyright (c) 2024 CCwhiteX

from console.UserManager import is_userlist

banlist_user = "ban_list.txt"
adminlist_user = "admin_list.txt"

def add_ban(user_id):
    with open(banlist_user, 'a') as f:
        f.write(f"{user_id}\n")
        
def add_admin(user_id):
    with open(adminlist_user, 'a') as f:
        f.write(f"{user_id}\n")

def ban(user_id):
    if is_userlist(user_id):
        print("Пользователь " + str(user_id) + " не может быть заблокирован, так как не зарегистрирован!")
    else:
        add_ban(user_id)
        print("Пользователь " + str(user_id) + " был заблокирован")
    
def admin(user_id):
    if is_userlist(user_id):
        print("Пользователь " + str(user_id) + " не может быть назначен админом, так как не зарегистрирован!")
    else:
        add_admin(user_id)
        print("Пользователь " + str(user_id) + " назначен админом")

