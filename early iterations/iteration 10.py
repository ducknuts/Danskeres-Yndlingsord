import random

ord_liste = []
tom_database = {
}


with open("C:/Users/Mumle/Desktop/Ordsammenligning/data/ord_database.txt") as f:
    for line in f:
        stripped_line_ord = line.strip()
        ord_liste.append(stripped_line_ord)

print (ord_liste)
while True:
    print("Hvilket ord kan du bedst lide? ")
    """Constant loop, that continously asks the user to pick a word"""

    ord = random.sample(list(ord_liste), 1)
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
        tom_database[userinput] += 1
        """The word receives 1 point, which is stored in the dictionary"""

    else: 
        print("Det var ikke et af ordene. Prøv igen.")
    print(f"Den nuværende score er følgende:")


    for key in tom_database.keys():
        """Iteration over keys i databasen, og printer keyens navn, samt det tilsvarende index for hver key-iteration."""
        print(f"{key} har {tom_database[key]} point!")