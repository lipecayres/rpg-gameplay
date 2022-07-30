#include <cs50.h>
#include <stdio.h>

int main (void)
{
    //Get value from the user
    int n;
    do
    {
        n = get_int("Weight: ");
    }
    while(n < 1);

    // Print ? points
    for(int i=0; i<n;i++)
    {
        printf("?");
    }
    printf("\n");
}