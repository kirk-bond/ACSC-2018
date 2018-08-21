Please place all of your challenges in here in their own individual folders.  Please use this as a template for your readme.md file

## Problem

The server guy has recently upgrade the security on the web portal to ensure that no one can get the flag.  Prove him wrong

## Flag
acsc18{ObscurityIsNotSecurity}

## Category
Web Exploitation

## Hints
1. What is the javascript function doing
1. Where do you get redirected to?

## Steps
1. Go to the index.html page
1. View source code
1. The hash isn't well known
1. The javascript is looking to see if the password entered hash to a specific value
1. If it does, the javascript redirects you to a webpage called admin_<password_hash>.html


## Resources Required
* webserver
