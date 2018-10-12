## Problem
A shiny new privilege escalation browser exploit was passed on to you and your team. You are so excited, you can hardly contain yourself and with that, want to let 'er rip as soon as possible. You've been working on escalate your privleges for a while and it seems the time has come! As you begin to prep your launcher, you decide to verify the browser platform version on the target one more time. Submit the browser version.
<br>
<br>
**NOTE:  Be sure to submit the flag in the correct format ( acsc18{flag} )**

## Flag
acsc18{58.0}

## Category
Forensics

## Hints
1. If I was Firefox, where would I keep this data?
1. Maybe you can loop through each file looking for a keyword or two.

## Steps
The PowerShell way
1. Uncompress the Firefox.zip file
1. Open PowerShell and navigate to the directory hosting the contains of the zip file
1. Type the following:
```powershell
select-string -path  .\firefox\z2oarlyx.default\* -Pattern "platformversion"
```
1. Flag still needs to be submitted correctly as acsc18{58.0}

## Resources Required
* PowerShell (or some langauge) or GUI
* Winzip, 7-zip, etc..
