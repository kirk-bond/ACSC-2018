# Feeling Lucky

You found the source code to a slot machine, can you use your insider knowledge to win big?

## Flag

acsc18{JACKPOT!!}

## Solve
The slot machine uses a custom random number generator. It looks at all of the files in the current directory and
randomly chooses one. It then randomly chooses a letter within that filename use. If that letter happens to be a 'W'
(uppercase) then the reel will display an 'A'. If you create multiple files in the current directory with W in the
filename, you can increase your chance of winning.
