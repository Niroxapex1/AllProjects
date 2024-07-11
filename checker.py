number = [2,4,3,5,7,2,9,7]
far = []
joft = []

def cheack(num):
    for i in num:
        if i%2 != 0 and num.count(i) == 2:
            num.remove(i)
            far.append(i)
    return far        
    

m = cheack(number)        
