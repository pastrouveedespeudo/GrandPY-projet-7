liste = [[],[],[],[],[],[],[],[],[],[],[],[]]

liste2 = []

var c = document.getElementById("monCadre");

var a = c.innerText || c.textContent;
var b = a.length;
//console.log(a)

var c = 0;

for(var i = 0; i<=b;i++){
liste[c].push(a[i]);
if(a[i] === ","){
    c++;
    };
};
console.log(liste)
for(var i =0;i<=liste.length;i++){
  if(liste[i]!=""){
      liste2.push(liste[i]);
  }
};
console.log(liste2)
a = Number(liste2[liste2.length -3].slice(1,-1).join(''));
//b = Number(liste2[liste2.length -2].slice(2,-5).join(''));
b = Number(liste2[liste2.length -2].slice(1,-4).join(''));
//console.log(liste2)
console.log(a)
console.log(b)
//console.log(liste2.length -2)
