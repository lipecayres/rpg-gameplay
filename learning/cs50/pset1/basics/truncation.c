#include <cs50.h>
#include <stdio.h>

int main (void)
{
    // Get numbers fom the user
    int x = get_int("x: ");
    int y = get_int("y: ");

    // Division process
    float z = (float) x / (float) y;
    printf("%f\n", z);
}