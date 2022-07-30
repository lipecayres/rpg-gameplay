#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void)
{
    // Getting initial value of population

    int startPop;
    do
    {
        startPop = get_int("Start size: ");
    }
    while(startPop < 9);

    // Getting final value of population
    int endPop;
    do
    {
        endPop = get_int("End size: ");
    }
    while(endPop < startPop);

    // Population
    int years = 0;

    while (startPop < endPop)
    {
        startPop = startPop + (startPop/3) - (startPop/4);
        years++;
    }
    printf("Years: %i\n", years);
}