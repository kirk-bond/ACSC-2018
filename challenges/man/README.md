## Problem

Did you know man pages have their own markup language?  Check out the man page for strings on this alpine linux docker.

## Flag

    * acsc18{man_strings_is_a_terrible_Google_image_search}

## Category

*Nix Trix

## Hints

    1.Hint 1: Some markup languages hide comments from display when rendered.
    1.Hint 2: Try to view the source file
    1.Hint 3: cat /usr/share/man/man0/strings/h.0p

## Steps

    1.Step 1: man strings (won't display the flag)
    1.Step 2: cat /usr/share/man/man0/strings.h.0p

## Resources Required

    alpine docker with bash vim nano mdocml-apropos man man-pages docs
    challenge file
    timestop-fu


```
if you use docker-compose.ymlfile:

services:
    varnish:
        ports:
            - 80
            - 6081

You can also specify the host/network port

varnish:
    ports:
        - 80:80
        - 6081:6081
```
