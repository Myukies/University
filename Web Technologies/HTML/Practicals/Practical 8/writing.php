<?php
// Write to a file
$filename = "example.txt";
$file = fopen($filename, "w") or die("Unable to open file!");
$txt = "Hello, world!\n";
fwrite($file, $txt);
fclose($file);
echo "Data written to $filename successfully!";
?>
