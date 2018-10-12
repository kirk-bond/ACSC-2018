#include "helper.h"
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void)
{
    char string[] = {0x61, 0x68, 0x73, 0x68, 0x31, 0x3d, 0x7b, 0x4f, 0x41, 0x48, 0x4b, 0x55, 0x4f, 0x59, 0x21, 0x26,
    0x7d, 0x05};

    srand(time(NULL));
    int selection = 'S';

    printf("Welcome to Aces Wild's\n");

    while ('Q' != selection && 'q' != selection)
    {
        printf("(S)pin\n"
               "(Q)uit\n");

        selection = getchar();

        // Clear the buffer
        int buf;
        while ('\n' != (buf = getchar()))
        buf = ' ';

        bool result;

        if ('S' == selection || 's' == selection)
        {
            result = helper_pullHandle();

            if (true == result)
            {
                for (int i = 0; i < 18; i++)
                {
                    if (i % 2 == 1)
                    {
                        string[i] -= 0x05;
                    }
                }

                printf("%s\n", string);

                return 0;
            }
        }

    }
}
