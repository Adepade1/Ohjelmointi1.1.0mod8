import random
import math

#Tehtävä 1

tulos = 1
def nopan_heitto():
    return random.randint(1, 6)
while tulos != 6:
    tulos = nopan_heitto()
    print(tulos)


#Tehtävä 2

game_on = True
tahko = int(input("Anna nopan sivujen määrä: "))
def nopan_heitto(tahko):
    return random.randint(1, tahko)


while game_on == True:
    arvo = nopan_heitto(tahko)
    if arvo == tahko:
        print("lopetus")
        game_on = False


#Tehtävä 3

def gallon_to_liters(gallons):
    liters = gallons * 3.785
    return liters
userinput = 0
while userinput >= 0:
    userinput = float(input("Anna gallonien määrä"))
    result = gallon_to_liters(userinput)
    print(result)


#Tehtävä 4

def SumList(Numbers):
    return sum(Numbers)

Numbers = [1, 2, 3, 4, 5]
print("Numerot: ", Numbers)
Result = SumList(Numbers)
print("Summa: ", Result)


#Tehtävä 5

def RemoveOddNumbers(Numbers):
    return [x for x in Numbers if x % 2 == 0]

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Alkuperäiset numerot: ", Numbers)
Result = RemoveOddNumbers(Numbers)
print("Parilliset numerot: ", Result)


#Tehtävä 6

def PizzaUnitPrice(Diameter, Price):
    Area = math.pi * (Diameter/2)**2
    UnitPrice = Price / Area
    return UnitPrice

Result1 = PizzaUnitPrice(float(input("Pizza 1 halkaisia: ")), float(input("Pizza 1 hinta: ")))
Result2 = PizzaUnitPrice(float(input("Pizza 2 halkaisa: ")), float(input("Pizza2 hinta: ")))

if Result1 < Result2:
    print("Pizza 1 on parempi valinta.")
else:
    print("Pizza 2 on parempi valinta.")