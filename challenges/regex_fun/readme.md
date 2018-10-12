## Problem

Find a flag that meets all of the below requirements.  FYI on the off chance you find one that you are sure works but don't get it correct, let a cadre know so we can manually ajudicate.

-  (?:[a-z0-9_]+)(?:\{.*?\})
-  ^[csa]{4}.*
-  ^(?:..)+$
-  ^(?:....)+$
-  ^(?:......)+$
-  ^(?:............)+$
-  .{1}.(?:.)[a-z0-9_{}].{1}.{1}.(?:.).{1}[a-z0-9_{}]..{1}[a-z0-9_{}](?:.)(?:.).{1}[a-z0-9_{}].{1}.{1}[a-z0-9_{}].{1}[a-z0-9_{}][a-z0-9_{}].{1}$
-  [a-z0-9]{6}[A-Z{}]{1,5}[a-z0-9]{3}[A-Z]...[a-z0-9]{0,3}[A-Z0-9].[A-Z0-9].{2}[A-Z{}]
-  [a-z0-9{}]{7}([A-Z])[a-z]{3}([A-Z])([a-z]).\1[a-z]{2}\3[A-Z].[A-Z]i\3[a-z0-9{}]
-  a(?:.*)e(?:.*)A(?:.*)i(?:.*)o(?:.*)i(?:.*)
-  (?=(?:.*?[\{].*?){1})(?=(?:.*?[\}].*?){1})(?=(?:.*?[a].*?){1})(?=(?:.*?[A].*?){1})(?=(?:.*?[c].*?){2})(?=(?:.*?[d].*?){1})(?=(?:.*?[e].*?){1})(?=(?:.*?[G].*?){2})(?=(?:.*?[i].*?){2})(?=(?:.*?[n].*?){3})(?=(?:.*?[o].*?){1})(?=(?:.*?[p].*?){1})(?=(?:.*?[r].*?){2})(?=(?:.*?[s].*?){1})(?=(?:.*?[T].*?){1})(?=(?:.*?[W].*?){1})(?=(?:.*?[1].*?){1})(?=(?:.*?[8].*?){1})


## Flag
acsc18{GrepAndGrinToWin}  

## Category
What category is this problem

## Hints
1. regex101.com is a great site (hell it's where we tested this)
1. Figure out the size of the flag and work backwards
1. Every character is explicitly defined

## Steps
1. The first few regexs show that the answer has to be a multiple of 2, 4, 6, and 12
1. The next few regexs help narrow down specific charachters to positions
1. The last regex gives a count of every chacter used


## Resources Required
* None
