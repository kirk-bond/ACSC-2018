# Feeling Lucky

You found the source code to a slot machine, can you use your insider knowledge to win big?

## Flag

acsc18{JACKPOT!!}

## Category
Reading/Understanding C

## Hints
1. [deduct 15%] Direct them to look at the helper_pullHandle function
2. [deduct 15%] Direct them to look at the helper_getRandLetter function
3. [deduct 50%] Explain the process of random number generation detailed in the answer section.

## Steps
1. Review the two source files to see how the slot machine operates.
2. Hone in on the random number generation
3. Place files in current directory that have 'W' in the filename
4. Pull the handle on the slot machine

## Resources required
Vim/text editor

## Answer
The slot machine uses a custom random number generator. It looks at all of the files in the current directory and
randomly chooses one. It then randomly chooses a letter within that filename use. If that letter happens to be a 'W'
(uppercase) then the reel will display an 'A'. If you create multiple files in the current directory with W in the
filename, you can increase your chance of winning.
