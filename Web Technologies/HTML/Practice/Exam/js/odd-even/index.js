function OddEven(){
    var num = document.getElementById("input_number").value;

    if(num%2==0){
        document.getElementById("result").textContent = num + ' is even!';
    }else{
        document.getElementById("result").textContent = num + ' is odd!';
    }
}