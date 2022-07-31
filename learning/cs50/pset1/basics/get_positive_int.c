#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);

int main (void)
{
    int i = get_positive_int();
    printf("%i\n", i);
}

// Ask a positive number to the user
int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Positive number: \n");
    }
    while (n < 1);
    return n;
}