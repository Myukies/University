<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    
    // Process the data (e.g., store in a database)
    // Here, we are just printing the values
    echo "Name: $name <br>";
    echo "Email: $email";
}
?>
