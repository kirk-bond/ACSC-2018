# Challenge: 
Access Sandy Mills-Mills' private server and find the key

# Write-up:
Searching for Sandy Mills-Mills will reveal https://twitter.com/smmacsc2018

Throughout her feed, she mentions her server @ trogdor.cs.umd.edu and her github account. She shares the same user name on github as Twitter (smmacsc2018)

Searching her github account will reveal her ssh keys `privaat` and `openbare`

`sftp -i privaat sandymillsmills@trogdor.cs.umd.edu`
will give you access to key.txt, but through sftp only and with the correct sshkey perms (chmod 600).

`sftp> get key.txt`
