
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

i=user.lower()

if  i=='c':

    print(menu[i])

    coffe=input("Enter the number ")

    print('Enjoy your' ,menu['c'][coffe])

elif i =='t':

    print(menu[i])
    tea = input("Enter the number ")
    print('Enjoy your', menu['t'][tea])

elif i =='s':

    print(menu[i])
    soups = input("Enter the number ")
    print('Enjoy your',menu['s'][soups])

elif i == 'b':

    print(menu[i])
    beverage = input("Enter the number ")
    print('Enjoy your',menu['b'][beverage])

else:
    print("INVALID OUTPUT!")









