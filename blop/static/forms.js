var typeIds = 1;
var locationIds = 1;
function addType(divName, eventType){
	/* 
	So, these first few lines are to give each new menu that we create a
	unique id.  That way, we can find and delete them later.  "typeIds" saves
	a number than indicates how many boxes we have made, and what the last
	one's id is.

	When we call the function, we increment typeIds to create a new id.  Then,
	we set its id to equal our new id value, then log it for dev purposes.
	 */
	typeIds++;
	var newtype = document.createElement("div");
	newtype.setAttribute("id", typeIds.toString() + "type");
	console.log(typeIds);
	switch(eventType)  { //We decided not to change the menu that appears based on the current selection, but the functionality to do so has been left here.
		//To change this based on the current selection, put the selection's value (NOT its name) into a "case" block, then change the options as desired.
		/*case '2': //Builds an AOD-specific menu
			newtype.innerHTML = "Details:" + '<select name="incident dropdown"><option value="5">Transport</option><option value="6">Amnesty</option><option value="7">Alcohol</option><option value="8">Marijuana</option></select><br>'
			break;
		case '1': //Builds an Medical-specific menu
			newtype.innerHTML = "Details:" + '<select name="incident dropdown"><option value="5">Transport</option><option value="6">Amnesty</option><option value="7">Alcohol</option><option value="8">Marijuana</option></select><br>'
			break;*/
		default:  //Builds the generic menu
			/*
			So, this is a litte bit hard to explain.  What we are doing here
			is literally changing the HTML text of our original document
			using this "innerHTML" thing.  What this does is that it just
			shoves whatever we set it equal to into the HTML of our new thing.
			This means that our database entries now show up in the dynamically
			created dropdowns.  Yay!

			Do note that, to my understanding, this is interpreted after Jinja
			does its sweep, so typing in Jinja commands here will not work.
			Our trick here is copying the Jinja code that has already been
			interpreted, and so it is being passed through after it has been
			turned into plain-old-HTML.

			This is confusing.  Stare at this for a while, and come find me if
			this makes no sense.
			*/
			var newtypeid = newtype.getAttribute('id');
			console.log(newtypeid);
			newtype.innerHTML = '<select name="incidents">' + document.getElementById("incidents").innerHTML + "</select>";  //Remember name=x[]
			break;
	}
	// We are done, put it at the end of our block!
	document.getElementById(divName).appendChild(newtype);
}

function removeType(){
	// Find the last dropdown we created (remember how we kept track of typeIds?)
	divNum = document.getElementById(typeIds.toString() + "type");
	console.log(divNum);
	var d = document.getElementById('dynamicType');
	// Decrement the id numbers, then delete the old thing.
	typeIds = typeIds - 1;
	d.removeChild(divNum);
}

function addLocation(){
	locationIds++;
	var newloc = document.createElement("div");
	newloc.setAttribute("id", "location_" + locationIds.toString())//locationIds.toString() + "location");
	var newlocid = newloc.getAttribute('id');
	newloc.innerHTML = '<select name="dynamicLocation">' + document.getElementById("dynamicLocation").innerHTML + "</select>";
	document.getElementById("location").appendChild(newloc);
}

function removeLocation(){
	divNum = document.getElementById("location_" + locationIds.toString());
	console.log(divNum);
	var d = document.getElementById("location");
	locationIds = locationIds - 1;
	d.removeChild(divNum);
}