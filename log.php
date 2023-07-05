<?php
session_start();
include('connection.php');

if (isset($_POST['submit']))
{	
$username=$_POST['email']; 
$password=$_POST['password']; 

	$sel="SELECT * FROM reg WHERE email='$username' and password='$password'";
	$result = mysqli_query($con,$sel) or die(mysql_error());
	$rows = mysqli_num_rows($result);
	$row=mysqli_fetch_array($result);
	
	if($rows>0)
	{	
		$_SESSION['user']=$row['id'];
		header("location:upload.php");
		
	}
	else{
		header("location: signin.php");
	}
}
	
?>
 
 



