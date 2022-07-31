#include <stdio.h>
#include <cs50.h>

int main (void)
{

    //Get weight from the user
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while(n < 1);

    // Printing squares;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("#");
        }
    printf("\n");
    }
}