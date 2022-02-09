import codecs
import random

tom_database = {
}


with codecs.open("C:/Users/Mumle/Desktop/Ordsammenligning/data/database.txt", encoding = 'utf-8') as f:
    for line in f:
        (key, val) = line.split()
        tom_database[key] = int(val)

while True:
    print("Hvilket ord kan du bedst lide? ")
    """Constant loop, that continously asks the user to pick a word"""

    ord = random.sample(list(tom_database), 2)
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