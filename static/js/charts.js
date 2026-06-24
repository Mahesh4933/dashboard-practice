function createChart(id,type,labels,data,title){

new Chart(document.getElementById(id),{

type:type,

data:{
labels:labels,

datasets:[{

label:title,

data:data,

borderWidth:2

}]

},

options:{
responsive:true
}

});

}