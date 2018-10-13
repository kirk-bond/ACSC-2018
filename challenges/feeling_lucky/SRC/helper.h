#ifndef HELPER_H
#define HELPER_H

#include <stdbool.h>

// Function to generate the results of each pull of the slot machine handle
bool helper_pullHandle(void);

int helper_displaySpin(char spin[]);

char helper_valueLookup(int reel_num);

int helper_getRandom(void);

int helper_getRandLetter(int file_count);

int helper_getFileCount(const char *dir_name);

#endif
