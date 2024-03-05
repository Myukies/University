function fact() {
    var num = parseInt(document.getElementById("num").value);
    var fact = 1; 

    if (num < 0) {
        document.getElementById("result").textContent = "No factorial for invalid numbers";
    } else if (num == 0 || num == 1) {
        document.getElementById("result").textContent = 'Factorial: 1';
    } else {
        for (var i = 2; i <= num; i++) {
            fact *= i; 
        }
        document.getElementById("result").textContent = "Factorial: " + fact; 
    }
}
