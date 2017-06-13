def digit_sum(n):
    digito = str(n)
    res = 0
    for dig in digito:
         res+=int(dig)   
    return res

print(digit_sum(1234))
