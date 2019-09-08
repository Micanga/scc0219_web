var input = document.getElementById("first-string")
var body = document.querySelector("body");
var button = null;
var select = null;
var query = null;

appendSelect = function(){
	if(button != null){
		button.parentNode.removeChild(button);
	}
	if(select != null){
		select.parentNode.removeChild(select);
	}

	select = document.createElement("select");
	select.setAttribute('size','3');
	select.setAttribute('multiple','multiple');
	body.append(select);

	button = document.createElement("button");
	button.setAttribute('type','button');
	button.innerHTML = 'Vamos buscar, bem legal.';
	button.onclick = search;
	body.append(button);
}

input.addEventListener ('keypress', (event) => {
	const pressedKey = event.key;
	if(pressedKey == 'Enter'){
		
		query = input.value;
		//clearing 
		
		if(query != "") {
			var option;
			appendSelect();
			//generating random numbers
			var randoms = [];
			//var selectedWords = [];
			while(randoms.length < 10){
			    var r = Math.floor(Math.random()*478) + 1;
			    if(randoms.indexOf(r) === -1) randoms.push(r);
			}
			fetch('478palavras.json').then(function(response) {
	      		if (response.status !== 200) {
	        		console.log('Looks like there was a problem. Status Code: ' +
	          		response.status);
	        		return;
	      		}
				// Examine the text in the response
	      		response.json().then(function(words) {
	        		for(i = 0; i < 10; i++){
	        			//selectedWords.push(words[randoms[i]]);
	        			option = document.createElement("OPTION");
	        			option.text = words[randoms[i]]
	        			select.add(option)
	        		}
	      		});
	      	}).catch(function(err) {
	    		console.log('Fetch Error :-S', err);
	  		});
	  		
	    }
	}
});

search = function(){
	for(i = 0; i < select.length ; i++){
		if(select[i].selected){
			query = query + ' ' + select.value;
			select[i].selected = false;
		}
	}
	window.open("http://google.com/search?q="+query);
}