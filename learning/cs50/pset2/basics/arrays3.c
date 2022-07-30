#include <cs50.h>
#include <stdio.h>

float mean (int quantity, int array []);

int main (void)
{

int TOTAL;
do
{
    TOTAL = get_int("Quantity of grades: ");
}
while (TOTAL <=0);

    int scores[TOTAL];
    for (int i = 0; i < TOTAL; i++)
    {
        scores[i] = get_int("Pontuaction %i: ", i+1);
    }
    printf("Average: %f\n", mean (TOTAL, scores));

}


float mean (int quantity, int array [])
{
    int soma = 0;
    for(int i = 0; i < quantity; i++)
    {
        soma += array[i];
    }
    return soma / (float) quantity;
}
