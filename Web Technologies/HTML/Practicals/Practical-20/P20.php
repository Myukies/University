<?php
$fname = trim($_REQUEST("first_name"));
$lname = trim($_REQUEST("last_name"));
$age = trim($_REQUEST("age"));
$hometown = trim($_REQUEST("home_town"));
$mobile = trim($_REQUEST("contact"));

echo'<h1>Retrieving Data from Server</h1>';
echo"<table border = '1'>
  <tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Age</th>
    <th>Hometown</th>
    <th>Mobile Number</th>
  </tr>";

echo'<tr>'.$fname.'</tr>';
echo'<td>'.$lname.'</tr>';
echo'<tr>'.$age.'</tr>';
echo'<tr>'.$hometown.'</tr>';
echo'<tr>'.$mobile.'</tr>';
echo"</table>";
?>
