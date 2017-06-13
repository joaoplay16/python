# Escreva sua funcao abaixo!

def fizz_count(x):
    count = 0
    
    for item in x:
        if item == "fizz":
            count += 1
    return count
    

lista = ["fibinachi", "fizz", "aooo", "fizz"]

print (fizz_count(lista))

