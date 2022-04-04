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


def login():
    with open('data/user.json', 'r') as f:
        user = json.load(f)

    login = input("Enter Username = ")
    login_pass = input("Enter Password = ")

    if user[login]==login_pass:
        i=input("want to add account [ ADD ] OR want to view your account [ VIEW ] ")
        n=i.upper()

        if "ADD" in n:
            add()
        elif "VIEW" in n:
            view()

    else:
        print("User incorrect")



def add():
    app=input("enter app name = ")
    name = input("Enter account name - ")
    password = input("Enter password - ")

    with open ('data/password_list.txt','a') as f:
        f.write(f"{app}-{name}-{password}\n")

def view():
    with open("data/password_list.txt",'r') as f:
        print("App-User-Password")
        for line in f.readline():
            print(line.rstrip(),end='')



def main():

    i=input("Signin use Key [SI] or Sign UP use Key [SU] = ")
    m=i.upper()

    if "SU" in m:
        print("Sign UP ")
        signup()
        print("Enter your detail to Login")
        login()
    elif "SI" in m:
        login()
    else:
        print("Invaid")



main()



