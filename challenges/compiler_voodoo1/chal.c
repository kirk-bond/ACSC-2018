#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#if defined(HARD_MODE)

#include "key_hard.h"
#define SRAND_SEED  0x4ae9ef4c
void decrypt(char *plaintext, size_t len)
{
    srand(SRAND_SEED);
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < i; j++) {
            (void)rand();
        }
        plaintext[i] ^= (~rand()) & 0xff;
    }
}

#else

#include "key.h"
#define SRAND_SEED  0xd0c96a49
void decrypt(char *plaintext, size_t len)
{
    srand(SRAND_SEED);
    for (int i = 0; i < len; i++) {
        if (i % 2 == 0) {
            rand();
        }
        plaintext[i] ^= rand() & 0xff;
    }
}

#endif  // HARD_MODE


int main(int argc, char *argv[])
{
    char input[64] = {0};

    printf("Enter the password: ");
    if (scanf("%63s", input) != 1) {
        return 1;
    }

    decrypt(input, strlen(input));

    if (memcmp(input, key_bin, key_bin_len) != 0) {
        puts("Nope.");
        return 1;
    }

    puts("Good password!");
    return 0;
}
