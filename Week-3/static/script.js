function sumUp(value) {
  var xhttp;
  var value = document.getElementById('txt1').value
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("result").innerHTML = this.responseText;
    }
  };
  if (value.length == 0) {
    xhttp.open("GET", "data?number=Lack%20of%20Parameter", true);
  } else {
    xhttp.open("GET", "data?number="+value, true);
  }
  xhttp.send();
}



