def anti_vowel(text):
    anti = ""
    for vog in text:
            if vog not in "aeiouAEIOU":
                anti = anti+vog
                print(anti)
    return anti
        
print (anti_vowel('Hey You!'))

