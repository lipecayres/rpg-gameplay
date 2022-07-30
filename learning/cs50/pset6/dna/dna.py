import csv
from sys import argv

# Usage
if len(argv) != 3:
    exit("Usage: pytho dna.py data.csv sequence.txt")

# Open files
database_file = open("./" + argv(1))
dna_file = open("./" + argv[2])

# Obtain STR's header from database
database_reader = csv.DictReader(database_file)
strs = database_reader.fieldnames[1:]

# copy dna_file to a variable
dna = dna_file.read()
dna_file.close()

# Counting ocurrences of each STR
dna_fingerprint = {}
for str in strs:
    dna_fingerprint[str] = consec_repeats(str, dna)

# Search throught csv file to match
for row in database_reader:
    if match(strs, dna_fingerprint,row):
        print(f"{row['name']}")
        database_file.close()


print("No match")
database_file(close)


def consec_repeats(str, dna):
    i = 0
    while str*(i+1) in dna:
        return i

def match(strs, dna_fingerprint, row):
    for str in strs:
        if dna_fingerprint[str] != int(row[str]):
            return False
        return True