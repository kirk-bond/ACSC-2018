#!/usr/bin/env python3

import os
def main():

    filesize = os.path.getsize("challenge_file.txt")

    for i in range(1, filesize):
        letter_count = 0
        print("Iteration ", i)
        with open("challenge_file.txt", "r") as infile:
            for letter in infile.read():
                if letter_count == i:
                    print("\n")
                    letter_count = 0
                else:
                    letter_count += 1

                print(letter, end="")

if __name__ == '__main__':
    main()
