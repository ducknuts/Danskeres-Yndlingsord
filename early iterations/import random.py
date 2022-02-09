import json
import random

with open("C:/Users/Mumle/Desktop/Ordsammenligning/data/ord.txt", "r") as word_list:
    words = [word.strip() for word in word_list]

with open("C:/Users/Mumle/Desktop/Ordsammenligning/data/point.txt", "r") as number_list:
    numbers = [int(number) for number in number_list]
    
word_dictionary = dict(zip(words, numbers))

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
            file.write(json.dumps(word_dictionary))

    else: 
        print("Det var ikke et af ordene. Prøv igen.")










