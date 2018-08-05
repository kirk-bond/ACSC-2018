## Problem

Business has been going great and we are rapidly approaching our 1 millionth visitor.  If you happen to be that lucky person, we've got a great prize for you

## Flag
acsc18{WinnerWinnerChickenDinner}

## Category
Web Exploitation

## Hints
1. Cookies aren't just tasty, they are useful too
1. That second cookie doesn't look encrypted, maybe encoded?
1. Is that a hash in there too?

## Steps
1. Visit the site, and you'll be assigned a random number of "visits"
1. Open your cookie editor of choice and change the count cookie to 999999
1. Change the checksum cookie to value of base64(999999:md5(999999))


## Resources Required
* A web server running apache
