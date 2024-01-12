function funkcija(){

    var f = document.getElementById("opcije");
    var x = document.getElementById("sve");
    console.log(x)
    

    if(f.style.visibility == "visible")
    {
      f.style.visibility = "hidden";
      x.style.background = "white";
      
      

    }
    
    else{
      f.style.visibility="visible";
      x.style.background = "silver";
      
    }

}

  
function zatvori(){
  var f = document.getElementById("opcije");
  var x = document.getElementById("sve");
  f.style.visibility="hidden";
  x.style.backgroundColor = "white";
  
  }