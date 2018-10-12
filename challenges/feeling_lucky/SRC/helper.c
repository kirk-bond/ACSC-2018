#include "helper.h"
#include <stdio.h>
#include <dirent.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_REEL 9

bool helper_pullHandle(void)
{
    char spin[MAX_REEL];
    int random_letter;
    bool success = false;

    for (int i = 0; i < MAX_REEL; i++)
    {
        random_letter = helper_getRandom();

        spin[i] = helper_valueLookup(random_letter);
    }

    helper_displaySpin(spin);

    if (spin[3] == 'A' && spin[4] == 'A' && spin[5] == 'A')
    {
        success = true;
    }

    return success;
}

char helper_valueLookup(int reel_num)
{
    if (reel_num == 87)
    {
        return 'A';
    }
    
    else if (reel_num >= 0 && reel_num < 30)
    {
        return 'K';
    }

    else if (reel_num >= 30 && reel_num < 60)
    {
        return '$';
    }

    else if (reel_num >= 60 && reel_num < 90)
    {
        return 'J';
    }

    else if (reel_num >= 90 && reel_num < 120)
    {
        return 'Q';
    }

    return '#';
}

int helper_getRandom(void)
{
    const char *lookup_dir = ".";

    int file_count = helper_getFileCount(lookup_dir);

    return helper_getRandLetter(file_count);
}

int helper_getFileCount(const char *dir_name)
{
    DIR * current_dir = NULL;
    int file_count = 0;
    struct dirent *current_file = NULL;
    
    if (NULL == dir_name)
    {
        return -1;
    }

    current_dir = opendir(dir_name);
    current_file = readdir(current_dir);

    while (NULL != current_file)
    {
        file_count++;
        current_file = readdir(current_dir);
    }
    
    closedir(current_dir);
    return file_count;
}

int helper_getRandLetter(int file_count)
{
    DIR * current_dir;
    struct dirent * current_file;
    int counter = 0, length = 0, rand_letterNum = 0;
    bool success = false;


    counter = rand() % file_count;
    current_dir = opendir(".");
    current_file = readdir(current_dir);

    while (NULL != current_file)
    {
        if (0 == counter)
        {
            length = strlen(current_file->d_name);
            rand_letterNum = rand() % length;
            success = true;
            goto end;

        }

        counter--;
        current_file = readdir(current_dir);
    }

end:
    closedir(current_dir);

    if (true == success)
    {
        return current_file->d_name[rand_letterNum];
    }
    else
    {
        return -1;
    }

}


int helper_displaySpin(char spin[])
{
    printf("\toO{-JACKPOT-}Oo\n"
           "\t.=============.\n"
           "\t| [%c] [%c] [%c] |(  )\n"
           "\t|-[%c]-[%c]-[%c]-| ||\n"
           "\t| [%c] [%c] [%c] | ||\n"
           "\t|             |_||\n"
           "\t| xxx ::::::: |--'\n"
           "\t| ooo ::::::: |\n"
           "\t| $$$ ::::::: |\n"
           "\t|             |\n"
           "\t|      __ === |\n"
           "\t|_____/__\\____|\n"
           "\t###############\n"
           "\t###############\n"
           "\t###############\n",
           spin[0], spin[1], spin[2],
           spin[3], spin[4], spin[5],
           spin[6], spin[7], spin[8]);

    return 0;
}
