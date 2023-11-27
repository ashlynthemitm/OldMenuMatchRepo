<?php
$name = $_POST['name'];
$visitor_email= $_POST['email'];
$subject = $_POST['subject'];
$message = $_POST['message'];

$email_from = 'otoyobo1@student.gsu.edu';

$emai_subject = 'MenuMatch Form Submission';

$email_body = "User Name: $name.\n".
                "User Email: $visitor_email.\n".
                    "Subject: $subject.\n".
                    "User Message: $message .\n";

$to = 'otoyobo1@student.gsu.edu';

$headers = "From: $email_from \r\n";

$headers .= "Reply-to: $visitor_email \r\n";

mail($to, $email_subject, $email_body, $headers);

header("Location: contact.html");
?>