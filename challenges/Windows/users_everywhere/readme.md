## Problem
You had an implant on a Windows DC for quite some time. Up until recent, there where only a few domain user accounts in the domain and now there are many more. The more expereinced person on your team inquired about the total number of users to which you said "there are a ton". Sadly enough, the other person doesn't like that as a number and needs the actual number. Determine the total number of users and submit it.
<br>
<br>
Submit the contents of the file at the root of all the zip files
**NOTE:  Be sure to submit the flag in the correct format ( acsc18{flag} )**

## Flag
acsc18{973}

## Category
Forensics

## Hints
1. Only do it manually if you have months to spare
1. There may be a cmdlet for that

## Steps
The PowerShell way
1. Open PowerShell
1. Type the following:
```powershell
(get-aduser -Filter *).count
```
1. Flag still needs to be submitted correctly as acsc18{973}

## Resources Required
* PowerShell (or some langauge)
* A Windows DC with the ad_build.ps1 script ran on it
