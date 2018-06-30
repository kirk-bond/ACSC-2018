#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SECRET_LEN 16

/* flag = 'wonphpwvyxnyekmq' */

char *key = "qmkeynxyvwphpnow";
char secret[SECRET_LEN + 1];

int win(void)
{
    printf("you win!\n");
    printf("submit the flag in the form:\n");
    printf("acsc18{<secret>}\n");
}

int lose(void)
{
    printf("sorry, you lose\n");
}

int decode_secret(void)
{
    int status = 1;

    for (int i = 0; i < 8; i++) {
        if (secret[i] != key[15 - i]) {
            goto done;
        }
        if (secret[15 - i] != key[i]) {
            goto done;
        }
    }

    status = 0;

    done:
    return status;
}

int main(int argc, char **argv)
{
    int is_flag = 1;

    if (argc < 2) {
        printf("usage: %s <secret>\n", argv[0]);
        printf("you've got to tell me the secret if you want to win\n");
        exit(-1);
    }
    
    if (strlen(argv[1]) != SECRET_LEN) { goto done; }

    strncpy(secret, argv[1], SECRET_LEN);

    is_flag = decode_secret();

    if (0 == is_flag) { win(); }
    else { lose(); }

    done:
    exit(is_flag);
}
