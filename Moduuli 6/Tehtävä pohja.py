#Tehtävä 2
import random
game_on = True
tahko = int(input("Anna nopan sivujen määrä: "))
def nopan_heitto(tahko):
    return random.randint(1, tahko)

while game_on == True:
    arvo = nopan_heitto(tahko)
    if arvo == tahko:
        print("lopetus")
        game_on = False