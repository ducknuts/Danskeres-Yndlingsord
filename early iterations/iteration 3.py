import random

ord_database = {
    "ged": 0,
    "æble": 0,
    "fantastisk": 0,
    "hest": 0,
    "mulighed": 0
}

while True:
    """Constant loop, that continously asks the user to pick a word"""
    print("Hvilket ord kan du bedst lide? ")
    ord = random.sample(list(ord_database), 2)
    """.sample is a method from the random-library, which picks samples from the chosen dictionary. Second parameter is how many samples
    we also put the new words in a list, to be able to index them"""
    ord1 = ord[0]
    ord2 = ord[1]
    """We store the .sample-words in new variables, to be able to compare them later. """
    print (f"{ord1} {ord2}")
    userinput = input("Skriv ord: ")
    if userinput == ord1 or userinput == ord2:
        """This if-statement checks whether the user-picked word matches either of the proposes words"""
        print(f"{userinput} får 1 point!")
        ord_database[userinput] += 1
        """The word receives 1 point, which is stored in the dictionary"""
    else: 
        print("Det var ikke et af ordene. Prøv igen.")
    print(ord_database) #unnecessary, just shows that the dictionary keys change value
    
