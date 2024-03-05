<?php
// Function to calculate factorial
function factorial($n) {
    if ($n == 0) {
        return 1;
    } else {
        return $n * factorial($n - 1);
    }
}

// Function to generate Fibonacci series
function fibonacci($n) {
    $fib = array(0, 1);
    for ($i = 2; $i < $n; $i++) {
        $fib[$i] = $fib[$i - 1] + $fib[$i - 2];
    }
    return $fib;
}

// Function to check if a number is prime
function isPrime($num) {
    if ($num <= 1) {
        return false;
    }
    for ($i = 2; $i <= sqrt($num); $i++) {
        if ($num % $i == 0) {
            return false;
        }
    }
    return true;
}

// Function to calculate reverse of a number
function reverseNumber($num) {
    $reverse = 0;
    while ($num > 0) {
        $reverse = $reverse * 10 + $num % 10;
        $num = (int)($num / 10);
    }
    return $reverse;
}

// Test functions
echo "Factorial of 5: " . factorial(5) . "<br>";
echo "Fibonacci Series: " . implode(", ", fibonacci(10)) . "<br>";
echo "Prime Numbers up to 20: ";
for ($i = 0; $i <= 20; $i++) {
    if (isPrime($i)) {
        echo $i . " ";
    }
}
echo "<br>";
echo "Reverse of 12345: " . reverseNumber(12345);
?>
