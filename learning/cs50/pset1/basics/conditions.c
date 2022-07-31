#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // User inserts x value
    int x = get_int("x: ");

    // User inserts y value
    int y = get_int("y: ");

    // Comparation between numbers
    if (x < y)
    {
        printf("x é menor do que y\n");
    }
    else if (x > y)
    {
        printf("x é maior do que y\n");
    }
    else
    {
        printf("x é igual a y\n");
    }
}