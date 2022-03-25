
menu={'c':{'1':'Espresso Coffee',
           '2':'Cappuccino Coffee',
           '3':'Latte Coffee'},
      't':{'1':'Plain Tea',
           '2':'Assam Tea',
           '3':'Ginger Tea',
           '4':'Cardamom Tea',
           '5':'Masala Tea',
           '6':'Lemon Tea',
           '7':'Green Tea',
           '8':'Organic Darjeeling Tea'},
      's':{'1':'Hot and Sour Soup',
           '2':'Veg Corn Soup',
           '3':'Tomato Soup',
           '4':'Spicy Tomato Soup'},
      'b':{'1':'Hot Chocolate Drink',
           '2':'Badam Drink',
           '3':'Badam-Pista Drink'}}

print("Welcome to CCD!")
print('Enter the First word of the product \nC = Coffee \nT = Tea\nS = Soup\nB = Beverages')

user=input('Enter the Product ')



if  user=='c':

    print(menu[user])

    coffe=input("Enter the number ")

    print('Enjoy your' ,menu['c'][coffe])

elif user =='t':

    print(menu[user])
    tea = input("Enter the number ")
    print('Enjoy your', menu['t'][tea])

elif user =='s':

    print(menu[user])
    soups = input("Enter the number ")
    print('Enjoy your',menu['s'][soups])

elif user == 'b':

    print(menu[user])
    beverage = input("Enter the number ")
    print('Enjoy your',menu['b'][beverage])

else:
    print("INVALID OUTPUT!")









