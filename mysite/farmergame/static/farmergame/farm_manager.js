function buy_animals() {
    alert("buying animals")
    /*xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML =
                this.responseText;
        } else {
            document.getElementById('demo').innerHTML = "Poep!"
        }
    };
    xhttp.open("GET", "{{ url 'farmergame:trade_animals'  }}", true);
    xhttp.send();*/
    document.getElementById('demo').innerText = "poep!"
}