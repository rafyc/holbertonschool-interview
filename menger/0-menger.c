#include "menger.h"

/**
 * menger - Function that draws a 2D Menger Sponge
 * @level: the level of the menger sponge to draw
 * Return: Nothing
 */


void menger(int level)
{
    if (level < 0)
        return;

    int i;
    int j;
    int sub = pow(3, level);

    for (i = 0; i < sub; i++)
    {
        for (j = 0; j < sub; j++)
        {
            int x = i;
            int y = j;
            char symbol = '#';

            while (x > 0 || y > 0)
            {
                if (x % 3 == 1 && y % 3 == 1)
                {
                    symbol = ' ';
                    break;
                }

                x /= 3;
                y /= 3;
            }

            printf("%c", symbol);
        }
        printf("\n");
    }
}
