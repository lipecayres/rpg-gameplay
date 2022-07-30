#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Implement a substitution cypher

int main (int argc, string argv[])
{

        // Quantity of characters in the key

    const int lenght = 26;

        // Validating quantity of arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

        // Checking key lenght

    if (strlen(argv[1]) != lenght)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }

        // Checking for non-alphabetic characters

    for (int i = 0; i < lenght; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Invalid Key - No alphabetic characters\n");
            return 1;
        }
    }
        // Checking for repeated characters

            // Characters repeatability iteration
    for (int i = 0; i < lenght; i++)
    {
        for (int j = i +1 ; j < lenght; j++)
        {
            if (toupper(argv[1][i]) == toupper(argv[1][j]))
            {
                printf("Invalid Key - Character repetition\n");
                return 1;
            }
         }

    // Getting plaintext from the user

    string plainText = get_string("Plaintext: ");

    // Printing cyphertext

    printf("Cyphertext: ");

    for (int a = 0, n = strlen(plainText); a < n; a++)
    {
        // Uppercase characters

        if (isupper(plainText[a]))
        {
            int index = plainText[a] - 'A';
            printf("%c", argv[1][index] );
        }

        // Lowercase characters

        else if (islower(plainText[a]))
        {
            int index = plainText[a] - 'a';
            printf("%c", argv[1][index] );
        }

        // Another characters

        else
        {
            printf("%c", plainText[a]);
        }
    }
    printf("\n");
    return 0;
    }

}