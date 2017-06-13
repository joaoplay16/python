def factorial(x):
    i = x   #4
    l =[]
    res = 0
    for n in range(x): #4
        l.append(i-1)
        print(i)
        for n in l:
            res *= int(n)
    return res

#print (factorial(4))
        
        
    
