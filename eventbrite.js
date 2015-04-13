console.log('eventbrite.js loaded');

var token = "FHO43SJ3VXJC6S3P2TRR";						//token for API access
var URL = "https://www.eventbriteapi.com/v3/events/search/?format=json&start_date.keyword=this_week&categories=103%2C104%2C105&venue.country=US&token=" + token;	//may be scaled for dynamic generation based on user input
var MAPLOC = "https://www.googledrive.com/host/0B_Qh0MNg09l0QUdXbkMySW1zYms/"		//location of map shape file

var state_nums = {};									//events per state
var total_pages = 0;									//pages in result
var total_events = 0;									//num of events returned
var curr_max_events = 1;								//maximum state events after every page of results

var h = 768;
var w = 1024;											//dimensions of map
var padding = 250;

var cx = 0;
var cy = 0;												//centroid of states + tooltip coordinates

var projection = d3.geo.albersUsa()
                       .translate([w/2, (h-padding)/2])	//projection info for map
					   .scale([1000]);
var path = d3.geo.path()
				.projection(projection);				//drawing information for map

var svg_progress = d3.select("body")					//svg to draw progress bar
					.append("svg")
					.attr({
						width:w,
						height:Math.floor(h/15)
					});
				
var svg = d3.select("body")								//attaching svg element to body to draw map on
			.append("svg")
			.attr({
				width:w,
				height:h
			});

d3.selection.prototype.moveToFront = function() {		//moves selected item to front on display
  return this.each(function(){
    this.parentNode.appendChild(this);
  });
};

var scaleUp = function(d) {								//scales up state by a factor of 2
	var centroid = path.centroid(d);
	cx = centroid[0];
	cy = centroid[1];
	return "translate(" + -cx + "," + -cy + ") scale(2)";
};

var scaleDown = function(d) {							//scales down state to original size
	var centroid = path.centroid(d);
	cx = centroid[0];
	cy = centroid[1];
	//console.log(cx + "," + cy);
	return "scale(1) translate(0,0)";
};

var showTooltip = function(name) {
	
//Update the tooltip position and value
	d3.select("#tooltip")
	.style("left", cx + "px")
	.style("top", cy + "px")
	.select("#value")
	.text(function(d){
		return name + ": " + state_nums[name] + " events out of " + total_events + "."
	});

//Show the tooltip
	d3.select("#tooltip").classed("hidden", false);

}

var drawAndInteract = function(json) {					//draw map and add mouseover interactivity
	svg_progress.append("rect")							//draw progress bar
				.attr({
					fill: "rgb(0,0,0)",
					width: 0,
					height: Math.floor(h/15)
				});
	svg.selectAll("path")								//draw and format states
           .data(json.features)
           .enter()
           .append("path")
           .attr("d", path)
		   .attr("fill", "rgb(0,0,0)")
		   .attr("stroke", "white")
		   .attr("stroke-width", 1)
		   .on("mouseover", function(d) {
				d3.select(this)
					.moveToFront()
					.attr("stroke", "red")
					.transition()
					.delay(500)
					.duration(250)
					.ease("elastic")
					.attr("transform", scaleUp)
					.each("start", showTooltip(d.properties.name));
			})
			.on("mouseout", function(d) {
				var clr = Math.floor(255*state_nums[d.properties.name]/curr_max_events);
				d3.select(this)
					.attr("stroke", "white")
					.transition()
					.duration(500)
					.attr("fill", "rgb(" +Math.floor(0.3*clr) + "," + clr + "," + Math.floor(0.5*clr) +")")
					.ease("elastic")
					.attr("transform", scaleDown);
				d3.select("#tooltip").classed("hidden", true);		//hide tooltip
			})
};

var choropleth = function(events) {						//tally events by state for choropleth
	var i = 0;
	for (i;i<events.length;i++) {							//iterate over event entries
		//console.log(events[i]);
		if (events[i].venue.address.region in state_nums) {	//add to state-wise count of events
			state_nums[events[i].venue.address.region] += 1;
			if (state_nums[events[i].venue.address.region] > curr_max_events) {
				curr_max_events = state_nums[events[i].venue.address.region];		//maximum events any state has
			}
		}
		else {
			state_nums[events[i].venue.address.region] = 1;
		}
	}
	//console.log(state_nums);
};

var getResults = function(current_page) {					//recursively obtain results from multiple pages
	d3.json(URL + "&page=" + current_page, function(results){
		if (current_page == 1) {							//set recursion limits by storing number of pages in result
			total_pages = results.pagination.page_count;
			total_events = results.pagination.object_count;
		}
		else if (current_page == total_pages) {				//recursion end condition
			return;
		}
		choropleth(results.events);						//add page results to tally of events by state
		current_page++;										//increment to next page
		updateStuff(current_page);
		getResults(current_page);							//let it rip
	});
}

var updateStuff = function (current_page) {
	var new_color = Math.floor((current_page/total_pages)*256);
	svg_progress.select("rect")							//update progress bar
				.transition()
				.duration(1000)
				.ease("elastic")
				.attr({
					width:Math.floor((current_page/total_pages)*w),
					fill: "rgb(" + new_color + "," + new_color + "," + new_color + ")"
				});
	svg.selectAll("path")								// update state colours
		.each(function(d) {
			new_color = Math.floor(255*state_nums[d.properties.name]/curr_max_events);
			d3.select(this)
				.attr("fill", "rgb(" +Math.floor(0.3*new_color) + "," + new_color + "," + Math.floor(0.5*new_color) +")");
		});
}

d3.json(MAPLOC, function(json) {							//loading map data from json file
	console.log('map data loaded');
	drawAndInteract(json);									//draw map
	
	for (var i=0; i<json.features.length; i++) {						//initialize state-wise event numbers to 0
		state_nums[json.features[i].properties.name] = 0;
	};
	//console.log(state_nums);
						

	getResults(1);														//get results starting from first page
		
});