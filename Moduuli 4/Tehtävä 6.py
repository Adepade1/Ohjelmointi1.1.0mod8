#Tehtävä 6
import random

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