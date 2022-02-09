import json
import random

with open("C:/Users/Mumle/Desktop/Ordsammenligning/data/ord.txt", "r") as word_list:
    words = [word.strip() for word in word_list]
"""List of words are read"""

with open("C:/Users/Mumle/Desktop/Ordsammenligning/data/point.txt", "r") as number_list:
    numbers = [int(number) for number in number_list]
"""List of # points are read (default is 0). Numbers are cast into integers"""
    
word_dictionary = dict(zip(words, numbers))
"""List of words and list of # points are zipped into a dictionary. """

while True:
    print("Hvilket ord kan du bedst lide? ")
    """Constant loop, that continously asks the user to pick a word"""

    ord = random.sample(word_dictionary.keys(), 2)

    ord1 = ord[0]
    ord2 = ord[1]

    print (f"{ord1} {ord2}")
    userinput = input("Skriv ord: ")
    if userinput == ord1 or userinput == ord2:
        """This if-statement checks whether the user-picked word matches either of the proposes words"""

        print(f"{userinput} får 1 point!")
        word_dictionary[userinput] += 1
        """The word receives 1 point, which is stored in the dictionary"""

        with open ("C:/Users/Mumle/Desktop/Ordsammenligning/data/database.txt", "w") as file:
            file.write((json.dumps(word_dictionary)))
        """The chosen word is updated in the dictionary, receiving an additional point. This new dictionary is written to the database-document"""

    else: 
        print("Det var ikke et af ordene. Prøv igen.")

