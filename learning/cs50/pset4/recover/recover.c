#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Checking usability
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    // Opening the file

    FILE *input_file = fopen(argv[1], "r");


    // Checking if input is valid

    if(input_file == NULL)
    {
        printf("Could not open the file!\n");
        return 1;
    }

    // Storing blocks of 512 in a array
    unsigned char buffer[512];

    // Track number of images generated
    int count_image = 0;

    // File pointer for recovered images
    FILE *output_file = NULL;

    // char filename[8]
    char *filename = malloc(8 * sizeof(char));

    // Read blocks of 512 bytes
    while (fread(buffer, sizeof(char), 512, input_file))
    {
        // Check in bytes indicated start of JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Write the JPEG filenames
            sprintf(filename, "%03i.jpg",count_image);

            // Open output_file for writing
            output_file = fopen(filename, "w");

            // Count number of images found
            count_image++;
        }
        // Check if output is invalid
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }
    free(filename);
    fclose(output_file);
    fclose(input_file);

}