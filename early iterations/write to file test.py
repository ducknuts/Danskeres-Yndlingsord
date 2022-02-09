ny_fil = ""
with open("C:/Users/Mumle/Desktop/Ordsammenligning/data/database.txt", mode = 'r', encoding = 'utf-8', errors ='ignore') as f:
    for line in f:
        ny_fil += line.strip() + (" 0\n")
    f.close()
with open("C:/Users/Mumle/Desktop/Ordsammenligning/data/database.txt", mode = 'w', encoding = 'utf-8', errors ='ignore') as f:
    f.write(ny_fil)
    f.close()
