from random import randint

# Gera um numero de 1 a 10, inclusive
random_number = randint(1, 10)

guesses_left = 3
# Comece seu jogo!

while guesses_left > 0 :
    guess = int(input("Seu palpite: "))
    guesses_left -= 1
    print("resta", guesses_left, "chances")
    if(guess == random_number):
        print ("Voce venceu!")
        break  
else:
    print ("Voce perdeu! u.u")
