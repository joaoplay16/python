def reverse(text):
    size = len(text)
    l = []
    string = ""
    for caractere in text:
        size -= 1
        l.append(text[size])
    for letra in l:
        string += letra
    return string

print (reverse('!nohtyP'))

'''
def reverse(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev

print (reverse("joao"))
'''
