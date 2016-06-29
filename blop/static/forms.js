var divIds = 1
function subtype(divName, eventType){
	divIds++
	var newtype = document.createElement("div")
	newtype.setAttribute("id", divIds.toString())
	console.log(divIds)
	//newtype.setAttribute("id", [id name]) -> Sets an id for the new div
	switch(eventType)  { //We decided not to change the menu that appears based on the current selection, but the functionality to do so has been left here.
		//To change this based on the current selection, put the selection's value (NOT its name) into a "case" block, then change the options as desired.
		/*case '2': //Builds an AOD-specific menu
			newtype.innerHTML = "Details:" + '<select name="incident dropdown"><option value="5">Transport</option><option value="6">Amnesty</option><option value="7">Alcohol</option><option value="8">Marijuana</option></select><br>'
			break;
		case '1': //Builds an Medical-specific menu
			newtype.innerHTML = "Details:" + '<select name="incident dropdown"><option value="5">Transport</option><option value="6">Amnesty</option><option value="7">Alcohol</option><option value="8">Marijuana</option></select><br>'
			break;*/
		default:  //Builds the generic menu
			var newtypeid = newtype.getAttribute('id')
			console.log(newtypeid)
			// newtype.innerHTML = '<select name="incidents[]"><option value="0">Select an Incident Code</option>{% for type in types %}<option value={{ type.id }}>{{ type.code }}</option>{% endfor %}</select><br>'
			newtype.innerHTML = '<select name="incidents[]">' + document.getElementById("incidentdropdown").innerHTML + "</select>"  //Remember name=x[]
			break;
	}
	document.getElementById(divName).appendChild(newtype)
}

function removeElement()  {
	divNum = document.getElementById(divIds.toString());
	console.log(divNum);
	var d = document.getElementById('dynamicSubtype');
	divIds = divIds - 1;
	d.removeChild(divNum);
}

/*function populate(types)  {
	console.log(types)
	var dropDown = document.getElementById("incident type")
	for (var i = 0; i < types.length; i++)  {
		dropDown[dropDown.length] = new Option(types[i], types[i])
	}
}*/