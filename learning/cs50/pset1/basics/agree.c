#include <stdio.h>
#include <cs50.h>

int main (void)
{
    // Get a char from the user
    char c = get_char("Do you agree?");

    //Check agreement
    if (c=='y' || c=='y')
    {
        printf("Agreed!\n");
    }
    else if (c=='n' || c=='N')
    {
        printf("Didn't agree!\n");
    }
    else
    {
        printf("Try again!\n");
    }
}