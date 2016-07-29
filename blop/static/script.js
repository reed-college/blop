function add_counter(index, location) {
  var text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  var bbox = location.getBBox();

  // attempt to center the text within its bounding box
  text.setAttribute("transform", "translate(" + (bbox.x + bbox.width / 2) + " " + (bbox.y + bbox.height / 2) + ")")

  // undone: use the real value here instead
  text.textContent = index;

  // insert the node into the document
  location.parentNode.insertBefore(text, this.nextSibling);
};

// updates the info pane div for the current selection when the user
// clicks on the location
function add_onclick(index, location) {
  $(location).on("click", function() {
    // undone: find other, better ways of doing this
    $("#blop-info-pane").html("<h2>Current selection: " + index + "</h2>");
  });
};

// document ready handler; we will arrange for this function to be called
// when the page is ready
function dom_content_loaded() {
  /*
  The anonymous function passed as the second argument is also known as
  a callback or event handler.  It can reference the add_counter and
  add_onclick functions because it creates what is called a closure:
  The function, even though it executes at some point in the future
  (when the "load" event fires), will retain access to the variables that
  were in scope when the function was declared (here).
  */
  $("object#blop-svg").on("load", function() {
    // get the list of path elements into a local variable
    var locations = $(this.contentDocument).find("#reed_buildings > path");

    // use jQuery's .each() to call our functions against each location
    locations.each(add_counter);
    locations.each(add_onclick);
  });
};

/*
Arrange for our handler to run when all the DOM content has loaded.
This is written last but it is actually the first thing our script tag
will do, now that everything we need has been declared (but not executed).

If our script(s) were to start running immediately, they might refer to
DOM objects which don't yet exist and crash.

Another technique to do this is to put your script tags at the end of the
<body> tag, but I prefer this method.

I could also have written the following statement in the jQuery style:
  $(document).ready(dom_content_loaded);
but am using the "native" style for illustration purposes:
*/
document.addEventListener("DOMContentLoaded", dom_content_loaded);