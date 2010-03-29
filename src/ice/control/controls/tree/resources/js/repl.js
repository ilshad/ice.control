/**
*
* Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
*
* Ajax based BlueBream prompt.
*
**/

function inputREPLKeydown (event) {
    
    function showLine (output, place) {
	$('<pre class="output">' + output + '</pre>').appendTo(place);
    }

    if (event.keyCode == 13) {

	var form = $(event.target).parent('form.repl')[0];
	var data = $(form).serialize();
	var display = $('.repl-output', form);

	showLine(event.target.value, display);
	
	$.ajax({type: "POST",
		url: form.action,
		dataType: "xml",
		data: data,
		success: function (xml) {
		    var result = $('result', xml).text();
		    $('output > line', xml).each(function (i) {
			showLine($(this).text(), display)
		    });
		}});
	
	event.target.value = '';
    }
}
