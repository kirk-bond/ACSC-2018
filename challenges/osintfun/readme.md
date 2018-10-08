## Problem
Access Sandy Mills-Mills' private server and find the key

## Flag
acsc2018{90c17db65f1822eb2ecc9a087106de4a}

## Category
OSINT

## Hints
1. Twitter
2. Read the feed
3. Username re-use?

## Steps
Searching for Sandy Mills-Mills will reveal https://twitter.com/smmacsc2018

Throughout her feed, she mentions her server @ trogdor.cs.umd.edu and her github account. She shares the same user name on github as Twitter (smmacsc2018)

Searching her github account will reveal her ssh keys `privaat` and `openbare.pub`

`cat openbare.pub` reveals her sandymillsmills username on server @ trogdor.cs.umd.edu

`sftp -i privaat sandymillsmills@trogdor.cs.umd.edu`
will give you access to key.txt, but through sftp only and with the correct sshkey perms (chmod 600 {privaat,openbare.pub}).

`sftp> get key.txt`


## Resources Required
N/A
