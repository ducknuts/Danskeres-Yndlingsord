import random

ord_database = {
    "ged": 0,
    "pik": 4,
    "fantastisk": 3,
    "hest": 0
}

while True:
    print("Hvilket ord kan du bedst lide? ")
    ord1 = random.choice(list(ord_database))
    ord2 = random.choice(list(ord_database))
    print(f"{ord1} eller {ord2}?")
    userinput = input("Skriv ord: ").lower()
    if userinput == ord1 or ord2:
        ord_database[userinput] += 1
        print(f"1 point til {userinput}")
        print(ord_database)

