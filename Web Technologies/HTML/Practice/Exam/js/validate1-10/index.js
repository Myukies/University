function CheckNum(){
    var num = parseInt(document.getElementById("input").value);

    if(num > 0 && num < 10){
        document.getElementById("result").textContent = "Valid Number";
    }else{
        document.getElementById("result").textContent = "Invalid Number";
    }
}