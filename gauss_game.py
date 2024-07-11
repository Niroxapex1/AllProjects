def number():
    global num
    num = input('What is Your Number , 0 to 1000 : ')
    if num.isdigit() is False:
        print('you have to enter a number')
        number()
    elif num.isdigit(): 
        num = int(num)
        if num > 1000 and num < 0 :
            print('You have to choice numbers Between 0 to 1000')
            number()
number()
gaussesi = 19

while True:
    gaussesi -= 1
    gauss = input('Your gauss : ')
    if gauss.isdigit() is False:
        print('You have to enter a number')
        gaussesi += 1
    elif gauss.isdigit():
        gauss = int(gauss)
        if gauss == num:
            print('yay You did it !!!')
            break
        else:
            print(f'try again , You have {gaussesi +1} gausses left ')
            if gaussesi == 0:
                print('Game Ower')
                break