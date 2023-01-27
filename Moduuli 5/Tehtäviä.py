import random
#Tehtävä 1


kerrat = int(input("Anna noppien määrä"))
lista = []
total = 0

for kerrat in range(kerrat):
    luku = int(random.randint(1, 6))
    lista.append(luku)
    total = total + luku

print(total)


#Tehtävä 2

numbers = []

while True:
    user_input = input("Syötä luku tai lopeta syöttämällä tyhjä merkkijono: ")
    if user_input == "":
        break
    numbers.append(float(user_input))

numbers.sort(reverse=True)
print("Viisi suurinta lukua:")
for i in range(5):
    print(numbers[i])


#Tehtävä 3

annettuluku = input("Anna luku")
luku = 1
game_on = True

for luku in range(2, luku):
    #print(f"testataan lukuav{annettuluku} jakamalla se {luku}")
    #print(f"jakojäännös {annettuluku % luku}")
    if annettuluku % luku == 0:
        print(f"{annettuluku} ei ole alkuluku")
        game_on = False
    else:
        print(f"{annettuluku} on alkuluku")