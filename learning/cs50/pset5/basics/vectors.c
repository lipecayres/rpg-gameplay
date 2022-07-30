#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    // Use malloc to get enought memory to 3 integer's
    int *list = malloc(3* sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Defining array values
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    //Now, putting more memory space...
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    //Copying the list of size 3 to a list of size 4
    for (int i = 0; i <3; i++)
    {
        tmp[i] = list[i];
    }

    // Adding a new number to the new list
    tmp[3] = 4;

    // Free memory of size 3
    free(list);

    // New list
    list = tmp;

    // Print new list
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // Free new list
    free(list);

}