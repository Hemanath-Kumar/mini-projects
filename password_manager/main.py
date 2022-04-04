import json
import os




def signup():
    if os.path.exists('data/user.json'):
        with open('data/user.json','r') as f:
            user = json.load(f)
    else:
        user={}
    login = input("Enter Username = ")
    login_pass = input("Enter Password = ")
    user[login]=login_pass
    with open('data/user.json', 'w') as f:
        json.dump(user,f)


def login()

