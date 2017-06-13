def remove_duplicates(lista):
    l2 = []
    for n in lista:
        if n not in l2:
            l2.append(n)
    return l2

print (remove_duplicates([1,1,1,1,2.3,2,3,3]))
