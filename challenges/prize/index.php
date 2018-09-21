<?php 
    if (!isset($_COOKIE['count']))
    {
        $count = strval(1);
        setcookie("count", $count);
        $checksum = base64_encode($count.":".md5(strval($count)));
        setcookie("checksum", $checksum);
    }
    else
    {
        $count = $_COOKIE['count'];
        $checksum = $_COOKIE['checksum'];
        $calculated_checksum = base64_encode($count.":".md5(strval($count)));
        if ($checksum == $calculated_checksum)
        {
            $count = ++$_COOKIE['count'];
            $checksum = base64_encode($count.":".md5(strval($count)));
            setcookie("count", $count);
            setcookie("checksum", $checksum);
            $validcheck = 1;
        }
        else
        {
           $validcheck = 0;
        }
    }
?>  

<html> 
    <head>

        <title>We Love to Give Stuff Away</title> 
		<style>
			body {
				margin: auto;
				text-align: center;
				background-color: rgb(255, 137, 0);
			}
			.flag {
				font-size: xx-large;
			}
			.error {
				font-size: xx-large;
                                color:  red;
			}
		</style>

	</head> 
  <body> 
  <h1>We Love to Give Stuff Away</h1>
  <p>We have got an amazing prize for our lucky 1,000,000 visitor</p>
<?php 
    if ($count == 1)
    {
        ?>
           <p> Unfortunately you are only visitor <?php echo $count; ?> so make sure you visit again soon </p>
        <?php
    }
    else
    {
       if ($validcheck == 1)
       {
            if ($count == 1000000)
            {
                ?>
                <p class="flag">Congrats lucky 1 million!  The flag is:  acsc18{WinnerWinnerChickenDinner}</p>
                <?php
            }
            else
            {
                ?>
                   <p> Unfortunately you are only visitor <?php echo $count; ?> so make sure you visit again soon </p>
                <?php
            }
        }
        else
        {
            ?>
            <p class="error">Cheater Cheater, Pumpkin Eater</p>
            <?php
        } 
    }
?> 
   </body> 
</html>
