#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Encripting a text with a caesar key

    // Starting function prompting the key

int main (int argc, string argv[])
{
        // Validating function usage
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
        // Verifying if key are digits

    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
         if (!isdigit(argv[1][i]))
         {
            printf("Usage: ./caesar key\n");
            return 1;
         }
    }

    // Defining the key to encriptation

    int key = atoi(argv[1]);


    // Getting plaintext from the user
    string plainText = get_string("plaintext: ");


    // Printing ciphertext:

    printf("ciphertext: ");

    // Iterating characters
    for(int i = 0, n = strlen(plainText); i < n; i++)
    {
            // Uppercase characters
        if (isupper(plainText[i]))
        {
            printf("%c", ((plainText[i] + key - 'A') % 26) + 'A' );
        }

            // Lowercase characters
        else if (islower(plainText[i]))
        {
            printf("%c", ((plainText[i] + key - 'a') % 26) + 'a' );
        }

            // Another characters
        else
        {
            printf("%c", plainText[i]);
        }
    }
    printf("\n");
}