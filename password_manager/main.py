import json


import os

#user_input=input('Enter the Key - ')

def add():
    Name=input("Enter Name of your password - ")
    password=input("Enter your password - ")

    with open("password_manager\password_list.txt",'a') as f:
        f.write(f'{Name} = {password}\n')

    # 'r' - use to read file
    # 'a' - use to append 
    #'w' - use to write file every time you run the code 

def view():

    with open ('password_manager\password_list.txt','r') as f:
        for line in f.readlines():
            print(line)

def load():
    #This function is used to load the Json file ,to get the detail of contact
    with open('password_manager/login.json','r') as f:
       i = json.load(f)
       return i

def login():

    login=input("Enter Username = ")
    login_pass=input("Enter Password = ")
    [login]=login_pass

    if i[login] and i[login][login_pass]:
        print(i[login][login_pass])

        with open('password_manager\login.json', 'w') as f:
            json.dump(i, f)
    
    else:
        print('er')
    
login()

def signup():

    i=load()

    login=input("Enter Username = ")
    login_pass=input("Enter Password = ")
    
    i[login]=login_pass

    with open('password_manager\login.json', 'w') as f:
        json.dump(i, f)

    i=load()



    



def main():
    
    print("To view password press - [ V ]\n"
          "To add new password press - [ A ]\n"
          "To delete password press - [ D ]")
