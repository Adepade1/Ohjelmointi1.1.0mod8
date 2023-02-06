import mysql.connector

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'user1',
    password = '1234',
    autocommit = True
    )

def funktio()


ICAO = input("Anna ICAO tunnus: ")
while True:
    ICAO = input("Anna ICAO tunnus: ")
    if ICAO == "":
        print("ohjelma lopetettiin")
        break
    else:
        funktio()


