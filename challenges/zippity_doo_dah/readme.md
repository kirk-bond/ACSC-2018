## Problem
You were given another zip file off of the hard drive we were analyzing. We also found a text file with it called "password.txt" and the password was "powershell". When we unzipped the file with the password, there was another zip, and another zip. It seems that this file is zipped over and over again with this same password.
<br>
<br>
Submit the contents of the file at the root of all the zip files
**NOTE:  Be sure to submit the flag in the correct format ( acsc18{YourFlag} )**

## Flag
acsc18{too_much_sauce}

## Category
Forensics

## Hints
1. Only do it manually if you have months to spare
1. Maybe a "For" loop will help

## Steps
The PowerShell way
1. Open PowerShell
1. Type the following:
    PS C:\> .\Deploy-YarPosH.ps1 -ComputerName c:\users\blue\computers.txt -Dir c:\windows\system32 -Path C:\users\blue\Desktop\yara32.exe -Rules C:\users\blue\Desktop\my_yara_rules.yar

1. Flag still needs to be submitted correctly as acsc18{ROCKETMAN-PC}

## Resources Required
* PCAP File
