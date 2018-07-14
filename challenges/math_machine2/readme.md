## Problem

Think you're good at math?  Answer 100 simple problems in 2 minutes and you'll get your flag.

## Flag
acsc18{SameScriptMinorChange}

## Category
Scripting

## Hints
1. There is probably a way to automate this task and complete it a lot faster than you can
1. Try seperating the input recieved by each new line

## Steps
1. Build a script that connects to the server and gets the first problem
1. Take that input and split it by \n
1. Strip any spaces off the first line
1. Split based on spaces on the second line to get the operation (i.e. add) and the 2nd number
1. Do the math and send back the answer


## Resources Required
* The script along with the Docker build file
* A docker running the script

