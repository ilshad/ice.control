/**
*
* Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
*
* Ajax based BlueBream prompt.
*
**/

function inputREPLKeydown (event) {
    if (event.keyCode == 13) {

	var form = $(event.target).parent('form.repl')[0];
	var data = $(form).serialize();

	$.ajax({type: "POST",
		url: form.action,
		dataType: "xml",
		data: data,
		success: function (xml) {
		    alert("Success!");
		}});
    }
}

function inputREPLKeyup (event) {
//    console.log('key up...');
//    console.log(event);
}
