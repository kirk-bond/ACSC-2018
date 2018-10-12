
## Problem

Pretty sure there's more information to this report then meets the eye

## Flag
acsc18{TalkAboutLayersOfSecurity}  (This is the flag that they will have to enter.  Please use this format)

## Category
Forensics

## Hints
1. A pdf file is made up of many parts, there's a unique part in this one when you look
1. You can embed a file within an image file pretty easily
1. Just convert it

## Steps
1. Run pdf-parser --stats on it
1. You will see a single FileSpec entry in the list for object 2191
1. Run pdf-parser --object 2191 --raw --filter and you'll see a reference to two other objects (2192 and 2193)
1. Rerun the command for 2193 and you'll get the layers.png image
1. Run binwalk on the image and you'll see the zip file
1. Carve the zip file
1. Open the zip and view secret.txt
1. Convert secret.txt into binary from base64 and get the image


## Resources Required
* 2018 SANS Security Awareness Report.pdf

based on https://github.com/krx/CTF-Writeups/tree/master/CSAW%2015%20Finals/for300%20-%20Mandiant
