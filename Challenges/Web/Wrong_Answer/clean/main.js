var submitButton = document.getElementById("button");
var answer = document.getElementsByName("answer");
var rightAnswer = "";

submitButton.addEventListener("click", getTheFlag);

function newHint(){
	question.innerHTML = "You need help? Try that! " + randomText();
}

function getTheFlag(){
	if(rightAnswer == "excellent"){newHint();}
	else if((answer[0].checked || answer[1].checked) && rightAnswer==""){
		question.innerHTML = "Wrong answer. Try again.";
	}
	else{
		question.innerHTML = "Wrong answer. Try again.";
	}
}

function randomText(){
	var a = "PdaBhwceoWxzbfaeo8";
	a = a + "371271873ezdoxzqba90q8v71" + document.getElementById("good").value;
	var n = a.length;
	
	for(var i = n - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
    return shuffleText(a, -100);
	
}

function shuffleText(s, k) {
    var n = 26;
	if (k < 0) {
        return shuffleText(s, k + n);
    }

    return s.split('')
        .map(function (c) {
            if (c.match(/[a-z]/i)) {
                var code = c.charCodeAt();
                var shift = code >= 65 && code <= 90 ? 65 : code >= 97 && code <= 122 ? 97 : 0;
                return String.fromCharCode(((code - shift + k) % n) + shift);
            }
            return c;
        }).join('');
}