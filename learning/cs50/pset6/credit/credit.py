from cs50 import get_string

def main():
    card_number = get_string("Credit Card Number: ")
    checksum(card_number)

def checksum():
    not_mult_two_sequence = 0
    mult_two_sequence = 0
    for i in range(len(card_number)):
        curr_num = (card_number[len(card_number)-1-i])
        if i % 2 == 0:
            not_mult_two_sequence += curr_num

main()

num = 1234
count_digits = 0
while num != 0:
    count_digits +=1
    num //= 10

#