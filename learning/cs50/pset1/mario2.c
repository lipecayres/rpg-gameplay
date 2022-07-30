#include <stdio.h>
#include <cs50.h>

int main (void)
{
    // Get Height from the user
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    // Printing blanck and hashes
    for (int i = 0; i < n ; i++)
    {
        // Left blanck
        for (int j = n-1 ; j > i; j--)
        {
            printf(" ");
        }

        // Left hashes
        for (int j=0; j <= i; j++)
        {
            printf("#");
        }

        // Middle blanck

            printf("  ");

        // Right hashes
        for (int j=0; j <= i; j++)
        {
            printf("#");
        }

    // Next line
    printf("\n");
    }
}
