n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Adicione sua funcao aqui
'''
def flatten(lists):
    results = []
    for numbers in range(len(lists)):
        for i in range(len(numbers)):
            results.append(i)
    return results


print (flatten(n))'''

for numbers in range(len(n)):#numbers = 1
    for i in range(n[numbers]):
        print(n[numbers][i]) 
#results.append(n[numbers][i]):
