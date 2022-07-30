import csv

title = input("Title: ").strip().upper()

with open ("CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file)

    counter = 0
    for row in reader:
        if row['title'].strip().upper() == title:
            counter +=1

print(counter)