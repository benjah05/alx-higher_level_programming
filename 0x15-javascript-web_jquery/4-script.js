#!/usr/bin/node
#toggle classes
$("document").ready(function() {
	if ("DIV#toggle_header").click(function() {
		$("header").toggleClass("green red");
	});
});
