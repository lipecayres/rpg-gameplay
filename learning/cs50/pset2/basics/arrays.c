#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void)
{
    int scores[3];
    for (int i = 0; i <3; i++)
    {
        scores[i] = get_int("Pontuation %i: ", i+1);
    }
    printf("Average: %f\n", (scores[0] + scores[1] + scores [2]/3.0));
}