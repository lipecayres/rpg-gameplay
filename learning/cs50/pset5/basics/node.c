#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main (void)
{
    // Creating a list of size 0. We use NULL to be sure haven't no garbage value on the list.
    node *list = NULL;

    // Memory alocation to a node, n
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    // Defining the pointer value at node
    n -> number = 1;
    n -> next = NULL;

    // Adding the node n pointing to list (first element)
    list = n;

    // ***** Memory alocation to another node
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }

    // Values definition of the new node
    n -> number = 2;
    n -> next = NULL;

    // Updating the first pointer to point to the second node
    list -> next = n;

    //Memory alocation to one more node
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list->next);
        free(list);
        return 1;
    }

    // Values definition of third node
    n -> number = 3;
    n -> next -> next = NULL;

    //Updating second pointer to go to the third pointer
    list -> next -> next = n;

    // Printing list using a loop
    for( node *tmp = list; tmp != NULL; tmp = tmp -> next)
    {
        printf("%i\n", tmp -> number);
    }

    // Free list with a while loop (First we point to the next node)
    while (list != NULL)
    {
        //Pointing to the next node
        node *tmp = list->next;

        // Now free previous node
        free(list);
    }


}