
import csv
import time
import random

films=[]
searched=[]
mega_genre = "ernests"

with open('filmss.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        films.append(row)

films.pop(0)
def sorting_lenght(film):
    return str(film[9])

def sorting_year(film):
    return str(film[7])


while True:
    print('''
1. Meklēt pēc filmas nosaukuma
2. Meklēt pēc žanra
3. Filtrēt pēc ilguma 
4. Filtrēt pēc uzņemšanas gada
5. Random filma
e. save and exit
''')
    choose = input("Izvēliesfunkciju: ")

    if choose == "1":
        search = input("Mekklēt: ")
        for film in films:
            if search in film[1]:
                searched.append(film)
        for x in searched:
            print(x)
        
        searched.clear()



    elif choose == "2":
        print(''''
1. Spēlfilma
2. Dokumentālā filma
3. Animācijas filma     
              ''')
        genre = input()
        if genre == "1":
            mega_genre = "spēlfilma"
        elif genre == "2":
            mega_genre = "dokumentālā filma"
        elif genre == "3":
            mega_genre = "animācijas filma"

        for film in films:
            if mega_genre == film[2]:
                searched.append(film)
        for x in searched:
            print(x)

    
    elif choose == "3":
        films.sort(key = sorting_lenght)
        for film in films:
            print(film)

    elif choose == "4":
        films.sort(key = sorting_year)
        for film in films:
            print(film)

    elif choose == "5":
        randomo = random.randint(1,77)
        randomo=randomo-1
        print(films[randomo])
    elif choose == "e":
        print("exiting...")
        print("saving...")
        break


