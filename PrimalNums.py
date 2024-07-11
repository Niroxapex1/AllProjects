user = input('enter how much do you want to go ')
print(2)
print(3)
print(5)
print(7)


if user.isdigit():
    user = int(user)
for i in range(2,user):
    if not i % 2 == 0 and not i % 3 == 0 and not i % 5 == 0 and not i % 7 == 0:
        print(i)

    