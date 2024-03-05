<?php
// Read from a file line by line
$filename = "example.txt";
$file = fopen($filename, "r") or die("Unable to open file!");
while (!feof($file)) {
    echo fgets($file) . "<br>";
}
fclose($file);
?>
