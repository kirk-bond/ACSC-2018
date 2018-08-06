## Problem

Remember when AOL used the be all the rage?  For some reason AOL still thinks it is.  So they have released a pretty cool feature, but the system will only allow their own browser to access it.  Do you still have one of their free disks?  (NOTE:  Please don't actually install this crap on your system)

## Flag
acsc18{DisableCallWaiting}

## Category
Web Exploitation

## Hints
1. Browsers tell the servers alot about themselves.  Can you manipulate that?
1. User-agent strings can be manipulated pretty easily

## Steps
1. This just requires a minipulation of the user-agent string you browse with.  Instructions for several browsers can be found at https://www.howtogeek.com/113439/how-to-change-your-browsers-user-agent-without-installing-any-extensions/
1. A list of AOL user-agent strings can be found at http://www.useragentstring.com/pages/useragentstring.php?name=AOL


## Resources Required
* Web server running apache
