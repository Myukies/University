function CalculateInterest(){
    var principal = parseFloat(document.getElementById("principal").value);
    var years = parseFloat(document.getElementById("years").value);
    var rate = parseFloat(document.getElementById("rate").value);
    let year_s;
    
    var interest = (principal * rate * years)/100;
    var final_amt = principal + interest;

    document.getElementById("result").innerHTML = "Interest: " + interest.toFixed(2);

    if(years <= 1){
        year_s = 'year'
    }else{
        year_s = 'years'
    }

    document.getElementById("total").innerHTML = "The total amount paid after " + years + ' ' + year_s + " is " + final_amt;
}