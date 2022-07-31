#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0; i < height; i++)
    {
        for (int j=0; j < width; j++)
        {
            // Converting pixels to float
            float Red = image[i][j].rgbtRed;
            float Green = image[i][j].rgbtGreen;
            float Blue = image[i][j].rgbtBlue;

            // Find the average value
            int average = round((Red + Green + Blue) / 3);

            // New values
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i= 0; i < height; i++)
    {
        for (int j=0; j < width; j++)
        {
            // Converting pixels to float
            float originalRed = image[i][j].rgbtRed;
            float originalGreen = image[i][j].rgbtGreen;
            float originalBlue = image[i][j].rgbtBlue;

            // Find the updetade pixel value
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            // Updating pixels greater than RGB scale
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            else if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            else if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            // Updating image

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
            for (int i=0; i<height; i++)
    {
        for (int j=0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - (j+1)];
            image[i][width - (j+1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
            // Copy of the image
        RGBTRIPLE temp[height][width];
        for (int i = 0; i < height ; i++)
        {
            for (int j = 0; j < width; j++)
            {
                temp[i][j] = image[i][j];
            }
        }

        for (int i = 0; i < height ; i++)
        {
            for (int j = 0; j < width; j++)
            {
                int totalRed, totalBlue, totalGreen;
                totalRed = totalBlue = totalGreen = 0;
                float counter = 0.00;

                //Get neighbouring pixels
                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        int currentX = i +x;
                        int currentY = j + y;

                        //Check if neighbouring pixel is valid
                        if (currentX < 0 || currentX > (height -1) || currentY < 0 || currentY >(width -1))
                        {
                            continue;
                        }

                        // Get image value
                        totalRed += image[currentX][currentY].rgbtRed;
                        totalGreen += image[currentX][currentY].rgbtGreen;
                        totalBlue += image[currentX][currentY].rgbtBlue;

                        counter++;
                    }
                    // Calculating average of neighbouring pixels
                    temp[i][j].rgbtRed = round(totalRed / counter);
                    temp[i][j].rgbtGreen = round(totalGreen / counter);
                    temp[i][j].rgbtBlue = round(totalBlue / counter);
                }
            }
        }
        // Copy into the original image
        for(int i = 0; i < height; i++)
        {
            for (int j = 0; j < width ; j++)
            {
                image[i][j].rgbtRed = temp[i][j].rgbtRed;
                image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
                image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            }
        }
    return;
}
