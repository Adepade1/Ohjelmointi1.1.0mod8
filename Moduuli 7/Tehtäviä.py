#Tehtävä 1

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
kuukausinumero = int(input("monesko kuukausi? "))
tulos = vuodenajat[kuukausinumero - 1]
print(f"vuodenaika on {tulos}")



#Tehtävä 2

nimet = set()

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Syötetyt nimet:")
for nimi in nimet:
    print(nimi)



#Tehtävä 3

Airports = {}
while True:
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")
    Choice = input("Valitse toiminto (1-3): ")

    if Choice == "1":
        ICAO = input("Syötä ICAO-koodi: ")
        Name = input("Syötä lentoaseman nimi: ")
        Airports[ICAO] = Name
    elif Choice == "2":
        ICAO = input("Syötä ICAO-koodi: ")
        if ICAO in Airports:
            print("Lentoaseman nimi:", Airports[ICAO])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif Choice == "3":
        break
    else:
        print("Virheellinen valinta.")