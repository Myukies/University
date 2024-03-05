function SumOf_N(){
    var input = parseInt(document.getElementById("input").value);
    var sum = 0;

    for(var i = 1; i <= input; i++){
        sum = sum + i;
    }

    document.getElementById("result").textContent = "The sum of all numbers till " + input + " is " + sum;
}