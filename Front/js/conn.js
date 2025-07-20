function datetostr() {
    var d = new Date();
    document.getElementById("currentDate").innerHTML = d.toLocaleDateString()  + " " + d.toLocaleTimeString();
}