import random


#Tehtävä 1

numero = 0

while numero <= 1000:
    if numero % 3 == 0:
        print(numero)
        numero += 1
    else:
        numero += 1


#Tehtävä 2

tuumat = float(input("Anna tuumien määrä"))

while tuumat >= 0:
    tulos = tuumat * 2.54
    print(f"Se on {tulos} senttimetriä")
    tuumat = float(input("Anna tuumien määrä"))
print("Ohjelma lopetettiin")


#Tehtävä 3

Numbers = []

while True:
    Input = input("Anna luku:")
    if not Input:
        break
    Numbers.append(float(Input))

if len(Numbers) >= 0:
    print("Pienin luku: ", min(Numbers))
    print("Suurin luku: ", max(Numbers))



#Tehtävä 4

satunnainenluku = random.randint(1, 10)
luku = int(input("Arvaa luku"))

while luku != satunnainenluku:
    if luku < satunnainenluku:
        print("Liian pieni arvaus")
    elif luku > satunnainenluku:
        print("Liian suuri arvaus")
    luku = int(input("Arvaa luku"))
print("Oikein meni")


#Tehtävä 5

trueusername = "python"
truepassword = "rules"

attempts = 1
while attempts <= 5:
    username = input("Anna käyttäjätunnus")
    password = input("Anna salasana")
    if trueusername == username and truepassword == password:
        print("Käyttäjänimi ja salasana oikein")
        break
    else:
        print("salasana väärin")
    attempts += 1
if attempts >= 5:
    print("Liian monta yritystä. Ohjelma lopetettiin")




#Tehtävä 6


N = 10000000
counter = 0
n = 0
while counter < N:
    counter = counter + 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    #print(f"arvottu piste {x}, {y}")
    if x * x + y * y < 1:
        #print("on sisällä")
        n += 1
print(f"pisteitä yhteensä {counter} joista {n} on ympyrän sisällä")