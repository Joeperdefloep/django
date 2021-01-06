var data = JSON.parse("{{data|escapejs}}")
var dataNode = document.getElementById('alldata')
dataNode.innerHTML = "{{data|escapejs}}"
dataNode = document.getElementById('neatdata')
for (var x in data){
    dataNode.innerHTML+=x+' : '+data[x]+'<br>';
}