$(function(){
	alert("Student json");
	$('#student').text("waiting for results");
	setInterval(refreshQueue,2000);
});
 function refreshQueue(){
	$.getJSON('/allstudents',function(d){
		$('#student').empty();
		$('#debug').text(d);
		for (var i=0;i<d.length; i++){
			$('<div/>')
				.append($('<span/>',{text:d[i][0] + " " + d[i][1]}))
				.append($('<br/>'))
				.appendTo('#student');
		}
	})
}