<html> 
    <head> 
        <title>AOL...Because Some People Just Won't Let Go</title> 
		<style>
			body {
				margin: auto;
				text-align: center;
                                color: rgb(255, 255, 255);
				background-color: rgb(0,0,0);
			}
			.flag {
				font-size: xx-large;
			}
			.error {
				font-size: xx-large;
                                color:  red;
			}
                        img {
                            margin-left: auto;
                            margin-right: auto;
                        }
		</style>
	</head> 
  <body> 
  <h1>AOL...Because Some People Just Won't Let Go</h1>
<?php 
    $agent = $_SERVER['HTTP_USER_AGENT'];
    $matched = preg_match('/^Mozilla\/[4|5].0.*MSIE [0-9].[0-9]{1,2};.*AOL [0-9].[0-9];.*Windows [NT|95|98]{2}.*/', $agent);
    if ($matched)
    {
       ?>
       <p class="flag">The Flag is:  acsc18{DisableCallWaiting}</p>
       <?php
    }
    else
    {
       ?>
       <p class="error">Sorry, this content is for AOL members only</p>
       <img src="aol.png"/>
       <?php        
    }
?> 
   </body> 
</html>
