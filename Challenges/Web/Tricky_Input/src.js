var divs = document.getElementsByTagName("div");

function lock(e){
	e.target.disabled = true;
}

function release(e){
	e.target.children[0].disabled = false;
}

document.getElementsByTagName("button")[0].onclick = function(){
    if(sha256(document.getElementsByTagName("input")[0].value) === "e85135e0bbd21cb76bbd8504d4f0d31dac39e392d03ef50acd588421c2a5d37f"){
  var s = "084072073067084070123115111114114121095102111114095116104101095105110099111110118101110105101110099101125";
    alert(s.deobfuscate());
  }
};

for(var i = 0; i < divs.length; i++){
  var div = divs[i];
  div.children[0].onfocus = function(e){lock(e);};
  div.onmouseover = function(e){lock(e);};
  div.onmouseleave = function(e){release(e);};
}

/*String.prototype.obfuscate = function () { 
  var bytes = [];
  for (var i = 0; i < this.length; i++) { 
    var charCode = this.charCodeAt(i); // pad the string to 3 digits 
    charCode = String("000" + charCode).slice(-3); bytes.push(charCode); 
  } 
  return bytes.join(''); 
}*/

String.prototype.deobfuscate = function () { 
  var string = ""; var chunks = this.match(/.{1,3}/g); 
  for (var i = 0; i < chunks.length; i++) { 
    string += String.fromCharCode(parseInt(chunks[i], 10)); 
  } 
  return string; 
}
