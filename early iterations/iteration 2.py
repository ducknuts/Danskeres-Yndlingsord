import random

ord_database = {
    "ged": 0,
    "æble": 0,
    "fantastisk": 0,
    "hest": 0,
    "mulighed": 0
}

while True:
    print("Hvilket ord kan du bedst lide? ")
    ord = random.sample(list(ord_database), 2)
    ord1 = ord[0]
    ord2 = ord[1]
    print (f"{ord1} {ord2}")
    userinput = input("Skriv ord: ")
    if userinput == ord1 or userinput == ord2:
        print(f"{userinput} får 1 point!")
        ord_database[userinput] += 1
    else: 
        print("Det var ikke et af ordene. Prøv igen.")
    print(ord_database)
    
