<?php

session_start();

//global variables

define( 'DB_NAME', 'couriertracker' );
define( 'DB_USER', 'oraonyemaobi' );
define( 'DB_PASSWORD', 'oraonyemaobi131471' );
define( 'DB_HOST', 'localhost' );

function checkLogin($username, $password) {	
    
}
if($_REQUEST['username'] != '' && $_REQUEST['password'] != '') {
	$username = $_REQUEST['username'];
	$password =  $_REQUEST['password'];
	checkLogin($username, $password);
}
//checkLogin($_POST['username'], $_POST['password']);

?>