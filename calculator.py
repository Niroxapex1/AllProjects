num1 = input('Please enter your first number : ')
if num1.isdigit():
    num1 = int(num1)
else:
    print('you have to enter a number')

def plus():
    global num1
    num1 += num2
    print(num1)

def menha():
    global num1
    num1 -= num2
    print(num1)
    
def zarb():
    global num1
    num1 *= num2
    print(num1)
    
def taghsim():
    global num1
    num1 /= num2
    print(num1)
    
while True:
    amal = input('\nEnter Your cal func, [+] , [-], [*], [/] : ')
    num2 = input('\nPlease enter your second number : ')
    if num2.isdigit():
        num2 = int(num2)
    else:
        print('you have to enter a number')
    if amal == '+':
        plus()
        
        exiti  = input('\nDo you want to leave? : ')
        if exiti == 'quit' or exiti == 'leave' or exiti == 'yes':
            print('Have Fun Bye')
            break
        else:
            continue
    elif amal == '-':
        menha()
        exiti  = input('\nDo you want to leave? : ')
        if exiti == 'quit' or exiti == 'leave' or exiti == 'yes':
            print('Have Fun Bye')
            break
        else:
            continue
    elif amal == '*':
        zarb()
        exiti  = input('\nDo you want to leave? : ')
        if exiti == 'quit' or exiti == 'leave' or exiti == 'yes':
            print('Have Fun Bye')
            break
        else:
            continue
    elif amal == '/':
        taghsim()
        exiti  = input('\nDo you want to leave? : ')
        if exiti == 'quit' or exiti == 'leave' or exiti == 'yes':
            print('Have Fun Bye')
            break
        else:
            continue
