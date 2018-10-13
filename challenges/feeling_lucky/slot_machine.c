#include "helper.h"
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void)
{
    char string[] = "acsc18{its not going to be that easy}";

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
                printf("%s\n", string);

                return 0;
            }
        }

    }
}
