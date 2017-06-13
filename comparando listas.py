lista_1 = [2, 4, 6, 51, 45 ,4, 5]
lista_2 = [45,3,25,14,45,52 ]

for a, b in zip(lista_1, lista_2):
    if a > b:
        print(a)
    else:
        print(b)
