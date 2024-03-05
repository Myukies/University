function check_text(){
    var input_text = document.getElementById("input").value.trim();
    
    if(input_text == ""){
        document.getElementById("result").textContent = "The textbox is empty! Please enter something.";
    }
    else{
        document.getElementById("result").textContent = "The textbox contains: " + input_text;
    }
}