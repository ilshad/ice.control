/**
*
* Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
*
* Ajax based BlueBream prompt.
*
**/

var LOAD_HISTORY = '/@@getControlDetailsREPLHistory';

var REPLHistory = [];
var REPLCurrent = 0;

function loadHistory () {
    var context_url = $('form.repl div.hidden').text();

//    $.ajax({type: "POST",
//	    url: context_url + LOAD_HISTORY,
//	    dataType: "xml"})
//	    success: function (xml) {
//		console.log(context_url);
//		REPLHistory = [];
//		$('line', xml).each(function (i) {
//		    REPLHistory.push(this);
//		});
//	    }});
}

/*function fromHistory (top) {
    if (top) current += 1;
    else REPLCurrent -= 1;	
    if (REPLCurrent < 0)
	REPLCurrent = len(REPLHistory) + REPLCurrent;
    if (REPLCurrent > len(REPLHistory))
	REPLCurrent = REPLCurrent - len(REPLHistory);
    return REPLHistory[REPLCurrent];
}*/

function inputREPLKeydown (event) {

    var form = $(event.target).parent('form.repl')[0];
    var context_url = $('div.hidden', form).text();

    function showLine (output, place) {
	$('<div class="output"><span class="prompt">&gt;&gt;&gt;</span><pre> '
	  + output + '</pre>').appendTo(place);
	place.scrollTop = place.scrollHeight;
    }

    var rn = true;

    //console.log(event);

    switch (event.keyCode) {

	/* enter - send the line */
	case 13:
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
	break;

	/* tab indent */
	case 9:
	event.target.value += '    ';
	$(event.target).focus();
	rn = false;
	break;

	/* up to history */
	case 38:
/*	console.log(fromHistory(true));*/
	event.target.value = '222'; 
	break;
    }
    return rn;
}

$(function () {
    $('form.repl input.repl-input').focus();
    loadHistory();
});
