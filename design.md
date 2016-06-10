SET-UP INSTRUCTIONS
-clone the repo (git clone https://github.com/reed-college/blop)
-check your remote (git remote -v)
-make the reed-college/blop repo the upstream (git remote add upstream https:github.com/reed-college/blop.git) (check remote again, make sure upstream is right)
-create a new branch (so when you push to github it pushes to your branch and not to master, that way we can all verify before committing it to master): git checkout -b [branch name] (probably best to just use your name)
-push your branch to github (git push upstream [name])
- a few other commands:
	to pull in changes from the master branch to yours: git fetch upstream
	to merge those changes with your branch: git merge upstream
	to delete your branch locally: git branch -d [name]
	then to delete it on github: git push upstream :[name]
so when you make changes you want to commit and send to github, do this:
	stage all changes: git add .
	commit all changes: git commit -am "some message"
	push to master: git push upstream [name]











To-Do:
General:
	--set up base.html (app/templates/base.html)
	--set up error page (app/templates/404.html) 

Auth:
	--create a login form (blop/app/auth/forms.py)
	--add a single entry to db (user: admin, password: ??? (pick something and tell us))
	--create a route and view function (blop/app/auth/views.py)
	--set up authorization (pick a package to use for login, install & add to requirements.txt; set up config, etc.)
	--add authorization requirement to view submission form/page, as well as have 'submit incident' in the navigation bar
	-- set up 'login' page (blop/app/templates/auth/login.html)

Blotter:
	--create a submission form
	--add db classes/models to
	--create a route and view function for submission page
		--in order to get the form to respond (e.g. I select 'AOD' and another field appears with different kinds of AODs like marijuana, alcohol, cocaine, etc.) you'll probably have to work with javascript to make it respond correctly.
	--set up the form submission template
		--this needs to have an authorization requirement (@login_required)
	--set up the blotter view & template

Map:
	--section off the map into regions
		--regions should roughly correspond to ARMS codes provided by Nano
	--create shapes to represent different types of incidents
		--probably top 4-6 types and an 'other' to catch the rest
	--create db models
	--add map and incident shapes to static folder?
	--figure out how to call and display the map and shapes with numbers
	--set up view function to display data for a default amount of time
		-a count of events of x type, on a shape, in a region on the map
	--figure out how to make a pop-out window happen, then construct the views so that clicking on a symbol causes a pop-out window to display the blotter page of those events

Search:
	***We may decide to incorporate search functionality into the individual blotter and map pages; for now, I'm imagining a separate search page with an option to display results as a blotter or a map***
	--modify/create db schema to allow for searchability
	--create search form
	--set up views function
	--set up search page html 


-------------------------------------------------------------------------------

This is a two-part project:

First: we'll create something very akin to a web-based CSO blotter.  This will be a web view showing a log in which each entry briefly details an event the CSOs responded to on campus. There will be sorting and filtering capabilities of a relatively high-level sort: 

- Category of response (e.g. AOD, Injury, Student Locked out of Dorm Room)
- Occurrence, both in terms of time range (last 7 days) and time of day
  ("things which happened between 10pm and 5am")

Next, we'll work with Justine Wang, who has been building maps of the campus, and the Strabo team to put a web front-end on this "blotter", allowing the events to be showing across the campus with the same filtering as the blotter. A person should be able to click back and forth between an event on a map and the blotter description of it.

Pages:
	-map page
	-live-feed blotter page, most recent posts at the top, able to load older posts via a button at the bottom of the page
	-analytics page


Navigation bar (visible on all pages) links:
	-Map 
	-live blotter
	-CSO feedback survey
	-community safety website
	-other emergency links
	-data analytics
	-(admin only) incident submissions

Authentication
	-non-admin should be publicly visible! this helps with cleary reporting requirements
	-reed Kerberos login, specific people given admin privileges

Database Fields
	-location: campus will be divided into regions. Each building will be its own region, and other campus areas will be separated out and given a label. The CSOs have a list of locations they already use for generating ARMS reports and are willing to add more specific sub-categories locations (e.g. "east canyon", "reed lake", "central canyon", "island", "west canyon" as opposed to just "canyon")
	-time: each entry will include a field for "time of incident/report"
	-incident type: the CSOs have a list of incident types and sub-types (e.g. type: medical sub-types: AOD, transport, etc.)
	-synopsis: ARMS reports have a synopsis field that gives a little bit of generalized detail "e.g. student in MacNaughton was locked out of room; CSO let them in."

	*this could be done manually by a student worker who reads through the ARMS reports and fills out a form for each report, which is similar to the current manual process, BUT it may be possible for the CSOs to export a .csv or .xls from the ARMS database with the information organized by fields (that would match ours), which would allow us to put in a bulk upload feature, or even to have the whole process happen automatically (i.e. ARMS automatically exports a spreadsheet and saves it somewhere, then our app automatically checks that place and creates relevant incident entries)*

Map
	The map will be separated into sections that match the codes provided by the CSO ARMS database. When an incident is entered, a pin appears in that region. They won't be specific exact locations, but that's not a huge concern. Pins will be color-coded by type of incident, and maybe shape-coded to indicate how recently they were placed (e.g. the ten most recent incidents or incidents in the last 30 days are shaped like a star). The viewer will be able to click on a pin and EITHER be redirected to a page with the blotter description OR have a bubble pop up with said description.
	Importantly, not all events are coded for location! Sexual Assaults and certain medical reports are coded only as on/off-campus and in/not in a residence hall. We will probably have a separate sidebar of some sort that shows these pins.


Analytics
	This could be a fun (& very useful!) thing to add to the app if we have time; a live-updating analysis & visualization of the data. Would need to talk about specifics with the CSOs

Sorting capabilities:
	-sort by incident
	-sort by date & time range
	-nesting, sub-categories (medical->aod/nonaod->transport/nontransport; location)
		Should be able to select "medical" incident type and have another field pop up where you can choose, i.e. "AOD" "Non-AOD" or "All", etc.
	-Cleary report incidents (this is a field we can add/copy over - "was this reported for the Cleary Act")
	-looking at x type of incident overlayed with academic calendar (when do SA reports tend to happen most, etc.)?


Non-Coding things to do:
	talk to Dyana re: Cleary reporting
	talk to Nano, to confirm the above/make changes if necessary
	Email CSOs requesting location & incident codes
	Email CSOs and CUS re: figuring out how to export data from the ARMS database


The following gives the structure for the app. You can see this if you `brew install tree` and then go into the root folder `/blop` and type `tree`

blop
├── LICENSE
├── README.md
├── app
│   ├── __init__.py
│   ├── analytics
│   ├── auth
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── blotter
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── map
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── search
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── static
│   └── templates
│       ├── 404.html
│       ├── analytics
│       ├── auth
│       │   └── signin.html
│       ├── base.html
│       ├── blotter
│       │   ├── blotter.html
│       │   └── submit.html
│       ├── map
│       │   └── map.html
│       └── search
│           └── search.html
├── config.py
├── design.md
└── requirements.txt










