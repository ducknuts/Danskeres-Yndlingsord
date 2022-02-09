import codecs

tom_database = {
}


with codecs.open("C:/Users/Mumle/Desktop/Ordsammenligning/data/lille_test.txt", encoding = 'utf-8') as f:
    for line in f:
        (key, val) = line.split()
        tom_database[key] = int(val)
