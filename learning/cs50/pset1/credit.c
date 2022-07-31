#include <stdio.h>
#include <cs50.h>

int main (void)
{
    //Get credit card number from the user
    long card;
    do
    {
        card = get_long("Credit Card Number: ");
    }
    while (card < 0);

    // Getting numbers

        // Gettinng multiplied numbers
    int card1, card2, card3, card4, card5, card6, card7, card8;
    card1 = ((card % 100)/10) *2;
    card2 = ((card % 10000)/1000) *2;
    card3 = ((card % 1000000)/100000) *2;
    card4 = ((card % 100000000)/10000000) *2;
    card5 = ((card % 10000000000)/1000000000) *2;
    card6 = ((card % 1000000000000)/100000000000) *2;
    card7 = ((card % 100000000000000)/10000000000000) *2;
    card8 = ((card % 10000000000000000)/1000000000000000) *2;

        // Doing the sum of the numbers units

    card1 = (card1 % 100/10) + (card1 %10);
    card2 = (card2 % 100/10) + (card2 %10);
    card3 = (card3 % 100/10) + (card3 %10);
    card4 = (card4 % 100/10) + (card4 %10);
    card5 = (card5 % 100/10) + (card5 %10);
    card6 = (card6 % 100/10) + (card6 %10);
    card7 = (card7 % 100/10) + (card7 %10);
    card8 = (card8 % 100/10) + (card8 %10);

        // First partial sum
    int sum1 = card1 + card2 + card3 + card4 + card5 + card6 + card7 + card8;

        // Getting non multiplied numbers

    int card9, card10, card11, card12, card13, card14, card15, card16;
    card9 = (card % 10);
    card10 = ((card % 1000)/100);
    card11 = ((card % 100000)/10000);
    card12 = ((card % 10000000)/1000000);
    card13 = ((card % 1000000000)/100000000);
    card14 = ((card % 100000000000)/10000000000);
    card15 = ((card % 10000000000000)/1000000000000);
    card16 = ((card % 1000000000000000)/100000000000000);

        // Second partial sum
    int sum2 = card9 + card10 + card11 + card12 + card13 + card14 + card15 + card16;

        // Final sum

    int sum3 = sum1 + sum2;

    // Last digit

    int lastDigit = (sum3 % 10);

    // Validating Card

    if (lastDigit != 0)
    {
        printf("%s\n", "INVALID");
        return 0;
    }

    // Separating card types (Visa, Master, Amex)

        // Card Lenght

    int lenght = 0;
    while (card > 0)
    {
        card = card/10;
        lenght++;
    }

        // VISA card

    long visa = card;
    while (visa >= 10)
    {
        visa = visa/10;
    }
    if (visa == 4 && (lenght ==13 || lenght == 16))
    {
        printf("%s\n", "VISA");
        return 0;
    }

    // AMEX Card
    long amex = card;
    while (amex > 100)
    {
        amex = amex/10;
    }
    if (lenght == 15 && (amex ==34 || lenght == 37))
    {
        printf("%s\n", "AMEX");
        return 0;
    }

    // Marter Card

    long master = card;
    while (master > 100)
    {
        master = master/10;
    }
    if (lenght == 16 && (master >= 51 && master <= 55))
    {
        printf("%s\n", "MASTERCARD");
        return 0;
    }
    else
    {
        printf("%s\n", "INVALID");
        return 0;
    }

}