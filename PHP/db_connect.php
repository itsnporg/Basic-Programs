<?php 
 // Login Details 
 $dbhost = 'localhost'; 
 $dbuser = 'admin'; 
 $dbpass = 'password'; 
// Connecting to DB
 $conn = mysqli_connect($dbhost, $dbuser, $dbpass); 
  

// Checking Connection
 if(! $conn )  
 { 
  die('Could not connect: ' . mysqli_error()); 
 } 
 else 
 { 
  echo 'Connected successfully'; 
 } 
  
 mysqli_close($conn); 
		  
?>
