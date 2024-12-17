# MIT License
# Copyright (c) 2024 CCwhiteX

def load_user():
    try:
        with open('user_ids.txt', 'r') as file:
            userc = [line.strip() for line in file.readlines()]
        return userc
    except FileNotFoundError:
        return []

def is_userlist(user_id): 
    userc = load_user()
    return str(user_id) not in userc

def load_admins():
    try:
        with open('admin_list.txt', 'r') as file:
            admins = [line.strip() for line in file.readlines()]
        return admins
    except FileNotFoundError:
        return []

def is_admin(user_id):
    admins = load_admins()
    return str(user_id) in admins

def load_banlist():
    try:
        with open('ban_list.txt', 'r') as file:
            banus = [line.strip() for line in file.readlines()]
        return banus
    except FileNotFoundError:
        return []

def is_banlist(user_id):
    banus = load_banlist()
    return str(user_id) in banus

