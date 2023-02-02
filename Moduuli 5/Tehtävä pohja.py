def gallon_to_liters(gallons):
    liters = gallons * 3.785
    return liters
userinput = 0
while userinput >= 0:
    userinput = float(input("Anna gallonien määrä"))
    result = gallon_to_liters(userinput)
    print(result)