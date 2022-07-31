#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void)
{
    // Asking an owe value to the user
    float n;
    do
    {
        n = get_float("Change owed: ");
    }
    while (n <= 0);

    // Rounding value
    int owe = round (n*100);

    // Coins available
    int a = 25;
    int b = 10;
    int c = 5;
    int d = 1;

            // Running program

    // Counter to number of coins
    int coins = 0;

            // Checking the number of coins to owe

    // Check 0.25 coins

    while (owe >= a)
    {
        owe -= a;
        coins++;
    }

    // Check 0.10 coins

    while (owe >= b)
    {
        owe -= b;
        coins++;
    }

    // Check 0.05 coins

    while (owe >= c)
    {
        owe -= c;
        coins++;
    }

    // Check 0.01 coins

    while (owe >= d)
    {
        owe -= d;
        coins++;
    }

    // Printing coins on the screen
    printf("%i\n", coins);

}