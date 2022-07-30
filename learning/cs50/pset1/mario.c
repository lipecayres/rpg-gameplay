#include <stdio.h>
#include <cs50.h>

int main (void)
{

    //Get Height from the user
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while(n < 1 || n > 8);

    // Printing squares;
    for (int i = 0; i < n; i++)
    {
        // Blanck :
        for (int j = n - 1; j > i; j--)
        {
            printf(" ");
        }

        // hashes :
        for (int j = 0; j <= i ; j++)
        {
            printf("#");
        }
    printf("\n");
    }
}