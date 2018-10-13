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
1. Open PowerShell and navigate to the directory where the zip file is
1. Type the following:
```powershell
New-Item -Name secrets -ItemType Directory
Copy-Item .\secrets1001.zip .\secrets
set-location .\secrets
for($i=1001; $i -ge 1; $i--)
   {   
   $7ZipPath = "C:\Program Files\7-Zip\7z.exe"
   $zipFile = "secrets$i.zip"
   $zipFilePassword = "powershell" 
   & $7ZipPath e $zipFile "-p$zipFilePassword" -y
   }
 
 & $7ZipPath e secrets.zip "-p$zipFilePassword" -y
 get-content password.txt
```
1. Flag still needs to be submitted correctly as acsc18{too_much_sauce}

## Resources Required
* PowerShell (or some langauge)
* 7 zip (or something that you can pass a password to in order to unzip a file)
