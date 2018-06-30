#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* flag = 'wonphpwvyxnyekmq' */

char *key = "qmkeynxyvwphpnow";

int win(void)
{
    printf("you win!\n");
    printf("submit the flag in the form:\n");
    printf("acsc{<secret>}\n");
}

int lose(void)
{
    printf("sorry, you lose\n");
}

int decode_secret(char *input)
{
    int status = 1;

    if (strlen(input) != 16) { return status; }

    for (int i = 0; i < 8; i++) {
        if (input[i] != key[15 - i]) {
            goto done;
        }
        if (input[15 - i] != key[i]) {
            goto done;
        }
    }

    status = 0;

    done:
    return status;
}

int main(int argc, char **argv)
{

    if (argc < 2) {
        printf("usage: %s <secret>\n", argv[0]);
        printf("you've got to tell me the secret if you want to win\n");
        exit(-1);
    }

    char *secret = argv[1];

    int is_flag = decode_secret(secret);

    if (0 == is_flag) { win(); }
    else { lose(); }

    exit(is_flag);
}
