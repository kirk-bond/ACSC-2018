## Problem
You were given a file that is supposed to be a picture, however, you can open it and don't know why at the moment. Normally you would just move on to something else, however, you can't except defeat and are determined to get it open. Once you finally get it open, submit the flag as the color of the shape in the jpg. 
<br>
**NOTE:  Be sure to submit the flag in the correct format ( acsc18{YourFlag} )**

## Flag
acsc18{orange}

## Category
Forensics

## Hints
1. Maybe we need a hex editor.
1. I wonder if the file header information is correct?
1. Wait, you said this was a jpg, right? Maybe we should ensure the header is set for a jpg.

## Steps
1. Open the file in Winhex
1. Change the data in offset 0 - 3 from 7A 7A 7A 7A to FF D8 FF E0. Also, click on the 'z' next to FIF around offset 6, and change it a 'J'
1. Save the file
1. Open the file with a image viewer
1. Notice the orange circle with the word "orange" written below it
1. Flag still needs to be submitted correctly as acsc18{orange}

## Resources Required
* Winhex or some hex editor
* Image viewer
