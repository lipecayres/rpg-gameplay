import csv

titles =  {}

with open ("CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"].strip().upper()
        if title not in titles:
            titles[title] = 1
        if title in titles:
            titles[title] += 1

for title in sorted(titles):
    print(title, titles[title])