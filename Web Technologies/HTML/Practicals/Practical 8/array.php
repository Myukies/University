<?php
// Creating an array
$colors = array("Red", "Green", "Blue", "Yellow");

// Accessing elements of the array
echo "First color: " . $colors[0] . "<br>";
echo "Second color: " . $colors[1] . "<br>";

// Adding elements to the array
$colors[] = "Orange";
$colors[] = "Purple";

// Looping through the array
echo "All colors: ";
foreach ($colors as $color) {
    echo $color . " ";
}
echo "<br>";

// Removing an element from the array
unset($colors[2]);

// Looping through the array after removing an element
echo "Colors after removing Blue: ";
foreach ($colors as $color) {
    echo $color . " ";
}
?>
