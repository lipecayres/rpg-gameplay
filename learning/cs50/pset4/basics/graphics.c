#include <stdint.h>
#include <stdio.h>

typedef uint8_t BYTE;

int main (int argc, char *argv[])
{
    // Checking usability
    if (argc != 2)
    {
        return 1;
    }

    // Open file
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        return 1;
    }
    //Read three first bytes
    BYTE bytes[3];
    fread(bytes, sizeof(BYTE), 3, file);

    //Verify three first bytes
    if (bytes[0] == 0xf && bytes[1] == 0xd8 && bytes[2] == 0xff)
    {
        printf("Maybe\n");
    }
    else
    {
        printf("No\n");
    }

    // Close program

    fclose(file);
}