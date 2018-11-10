## Problem
We believe employee Sandy Mills-Mills stole sensitive data and is storing it on her private server. She maintains an active Twitter presence. Use your OSINT abilities to log into her private server and find the hidden flag.

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

Throughout her feed, she mentions her github account. She shares the same user name on github as Twitter (smmacsc2018). 

Searching her github account will reveal her old ssh key `keys.pub`

`cat keys.pub` reveals her smmacsc2018 username on server @ 54.202.21.39

`old_password` reveals her password to be acsc18pemacsc18pemacsc18pem

`sftp smmacsc2018@54.202.21.39`
will give you access to key.txt, but through sftp only 

`sftp> get uploads/key.txt`


## Resources Required
N/A
