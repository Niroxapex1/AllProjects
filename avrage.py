nums = [1,2,3,20,30,10,90]

def avg(num):
    p = 0
    for i in num:
        p += i
    a = i / len(num)
    a = int(a)
    return a,p
number = avg(nums)

n = number + 10
print(n)
n = number + 10
print(n)