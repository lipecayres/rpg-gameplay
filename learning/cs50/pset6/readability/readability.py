# Getting text from user

text = input("Text: ")

# Defining number of letters, words and sentences
letters = 0
words = 0
sentences = 0

#Counting letters, words and sentences

for i in range(len(text)):

#       # Letters
    if text[i].isalpha():
        letters += 1

#       # Words
    if (i == 0 and text[i].isalpha()) or (i != len(text)-1 and text[i] == " " and text[i+1].isalpha()):
        words += 1

#       # Sentences
    if text[i] in ["!", ".", "?"]:
        sentences += 1

L = (letters / words) *100
S = (sentences / words) *100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index <1:
    print("Before Grade 1")

elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade: {index}")
