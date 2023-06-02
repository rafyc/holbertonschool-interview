#include "slide_line.h"

void merge_left(int *line, int size)
{
    int i;
    int j;
    int k;
    int new;
    int arr[size];

    for (i = 0; i < size; i++)
    {
        if(line[i] != 0)
        {
            for (j = i; j < size; j++)
            {
                if (line[i] == line[j])
                {
                    new = line[i] * 2;
                    line[j] = 0;
                    line[i] = 0;
                    for (k = 0; k < size; k++)
                    {
                        arr[k] = new;
                    }
                }
            }
        }
    }
}


int slide_line(int *line, size_t size, int direction)
{
	if (direction == SLIDE_LEFT)
	{
		merge_left(line, size);
	}

	else
		return (0);
	return (1);
}
