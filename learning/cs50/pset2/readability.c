#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

// Calculating the readability level of a text

int main (void)
{
    // Getting text from the user
    string text = get_string("Text: ");

    // Defining the number of letters, words and sentences
    int letters = 0;
    int words = 0;
    int sentences = 0;

    // Counting letters
    for(int i = 0, n = strlen(text); i < n; i++)
    {
        if ((text[i] >= 'a' && text[i] <='z') || (text[i] >= 'A' && text[i] <='Z'))
        {
            letters += 1;
        }
    }

    // Counting words
    for(int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ')
        {
            words += 1;
        }
    }
    words += 1;

    // Counting sentences

    for(int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.'  || text[i] == '!' || text[i] == '?')
        {
            sentences += 1;
        }
    }

    // Calculatint the Coleman-Liau index

        // Average number of letters per 100 words
        float L = (letters/ (float) words)*100.0;

        // Average number of sentences per 100 words
        float S = (sentences/ (float) words)*100.0;

        // Coleman-Liai equation
        int index = round( 0.0588 * L - 0.296 * S - 15.8);

    // Printing grade

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >=1 && index <= 16)
    {
        printf("Grade %i\n", index);
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("INVALID\n");
    }

}