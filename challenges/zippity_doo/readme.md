## Problem
You are given a zip file that is zipped over and over multiple times. You must unzip it to the root and supply the password listed in the text file.
<br>
<br>
**NOTE:  Be sure to submit the flag in the correct format ( acsc18{YourFlag} )**

## Flag
acsc18{wargames}

## Category
Forensics

## Hints
1. Only do it manually if you have months to spare
1. Maybe a "For" loop will help

## Steps
The PowerShell way
1. Open PowerShell and navigate to the directory where the zip file is located
1. Type the following:
```powershell
New-Item -Name data -ItemType Directory
Copy-Item .\data500.zip .\data

for($i=500; $i -ge 1; $i--)
   {   
   $ii = $i - 1
   Expand-Archive ".\data\data$i.zip" .\data\
   } 

Get-Content .\data\data.txt
```
1. Flag still needs to be submitted correctly as acsc18{wargames}

## Resources Required
* PowerShell (or some langauge)
