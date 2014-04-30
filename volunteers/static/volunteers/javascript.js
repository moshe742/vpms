$('document').ready(function() {
	$('#id_expertise option[value=4]').click(function() {
		$('#expertise_other').removeClass('hidden');
	});
});

function user_arrived(user_id, arrived) {
	$.ajax({
		url: "http://localhost:8000/volunteers/welcome/",
		cache: false,
		data: {'volunteer_id': user_id},
		dataType: 'text',
		type: 'GET',
		success: function() {
			location.reload();
		},
		error: function(xhr, status, error) {
			alert(xhr, status, error);
		}
	});
}

function liners(d) {
	var el = d3.select(this);
	var words = d.name.split(' ');
	if (words.length == 1) {
		el.attr('y', 5);
	} else {
		el.attr('y', function(d) { return -5 * words.length; });
	}
	for (i=0; i<words.length; i++) {
		var tspan = el.append('tspan');
		if (i == 0) {
			tspan.text(words[i]);
		} else {
			tspan.attr('x', '0')
					.attr('dy', '20')
					.text(words[i]);
		}
	}
}

function arrival(user_id, arrived, arrived_volunteer) {
	if (arrived) {
		clearTimeout(time_out);
		if (arrived_volunteer) {
			time_out = setTimeout(function() {user_arrived(user_id, arrived)}, 1000);
		}
	} else {
		time_out = setTimeout(function() {user_arrived(user_id, arrived)}, 7000);
	}
}

function collapse(d) {
	if (d.level == 'project') {
		if (d.children) {
			d._children = d.children;
			d.children = null;
		} else {
			d.children = d._children;
			d._children = null;
		}
/*	} else if (d.level == 'hasadna') {
		if (d.children) {
			d._children = d.children;
			d.children = null;
		} else {
			d.children = d._children;
			d._children = null;
		}
*/	}
	return d.id;
}

function tick() {
	link.attr("x1", function(d) { return d.source.x; })
		.attr("y1", function(d) { return d.source.y; })
		.attr("x2", function(d) { return d.target.x; })
		.attr("y2", function(d) { return d.target.y; });

	node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
}

function color(d) {
	var color_name;
	if (d.arrived & d.level == 'volunteer') {
		color_name = 'arrived'; //d.color
	} else if (!d.arrived & d.level == 'volunteer') {
		color_name = 'not-arrived'; //d.color
	} else {
		color_name = 'add'; //"#fd8d3c";
	}
	return d._children ? "condensed" : d.children ? "expended" : color_name;
}
