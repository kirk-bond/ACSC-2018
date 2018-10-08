#Linux1

## Problem

Find the longest line (most characters) in linux1

## Flag
acsc18{ProvincialRadiationSickness}

## Hints
1. awk has a number of functions besides just printing out parts of a string
1. It's possible to sort numericly
1. Hint 3

## Steps
1. awk '{ print length($0)":"$0; }' linux1 | sort -n


#Linux2

## Problem

How many characters are there in the 3rd column of words? (Ensure you submit the flag with the acsc18{<CharacterCount>}

## Flag
acsc18{71604}

## Hints
1. The cut command allows you to pull out a particular column
1. Word count can tell you a variety of statistics

## Steps
1. cat linux2 | cut -f2 -d$'\t' | wc -c


#Linux3

## Problem

What is the most common 12th chacter in the file.  Case Matters! (Ensure you submit the flag with the acsc18{<Character>}

## Flag
acsc18{e}

## Hints
1. The cut command allows you to pull out a particular character
1. You may need to sort things
1. You can get the count of unique characters

## Steps
1. cat linux3 | cut -c 12 | sort | uniq -c | sort -n


#Linux4

## Problem

What is the name of the file in the Linux4 folder with an md5 hash of 7ae8ef906919add4686419b22ea2e874

## Flag
acsc18{File350}

## Hints
1. md5sum can hash a file

## Steps
1. md5sum * | grep 7ae8ef906919add4686419b22ea2e874


#Linux5

## Problem

Just find the flag

## Flag
acsc18{DontForgetHiddenFiles}

## Hints
1. I promise, it's in the folder

## Steps
1. ls -l
1. cat .hiddenflag

#Linux6

## Problem

What version of yum is being used on the VM?  Note:  Ensure you use the acsc18{#.#.#-###} format

## Flag
acsc18{3.4.3-158}

## Hints
1. Check the man file for yum

## Steps
1. yum --version


#Linux7

## Problem

The flag is contained in a file somewhere on the system (Not in the users folder)

## Flag
acsc18{HopeYouUsedFind}

## Hints
1. You can specify that you are looking for a file with the find command
1. You can execute commands with find as well

## Steps
1. find / -type f -exec grep "acsc18" '{}' \;


