SET-UP INSTRUCTIONS
-clone the repo (`git clone https://github.com/reed-college/blop`) and cd into it
-check your remote (`git remote -v`)
-make the reed-college/blop repo the upstream (`git remote add upstream https://github.com/reed-college/blop.git`) (check remote again, make sure upstream is right)
-create a new branch (so when you push to github it pushes to your branch and not to master, that way we can all verify before committing it to master): `git checkout -b [branch name]` (probably best to just use your name)
-push your branch to github `(git push upstream [name])`
- a few other commands:
	to pull in changes from the master branch to yours: `git fetch upstream`
	to merge those changes with your branch: `git merge upstream`
	to delete your branch locally: `git branch -d [name]`
	then to delete it on github: `git push upstream :[name]`
so when you make changes you want to commit and send to github, do this:
	stage all changes: `git add .`
	commit all changes: `git commit -am "some message"`
	push to master: `git push upstream [name]`

To check if you have things needing to be committed/added, run `git status`


Once you have the repo cloned and are working on your branch (`git branch` will tell you which branch you're on. `git checkout [branch]` will switch branches. don't change things locally on the master branch...), create your virtualenv however you do that.

run `pip install -r requirements.txt`

Then we need to set the PYTHONPATH environment variable, so that the path when you activate your virtualenvironment is the root folder of the blop directory. Using virtualenvwrapper, that means you have to set the variable in the 'postactivate' hook inside the folder that contains your virtualenvs. To find that folder, run `echo $WORKON_HOME` ... for me this is 
`~/.python_virtualenvs`. 

run `subl/nano/vim ~/[folder_containing_virtualenvs]/[blop_virtual_env_name]/bin/postactivate`
So for me it's: `subl ~/.python_virtualenvs/blop/bin/postactivate`
Type in that document `export PYTHONPATH=[path_to_blop_root_folder]`
So for me it's `export PYTHONPATH=~/SDS/blop`
Save and exit.
De-activate and re-activate your virtual environment, then run `echo $PYTHONPATH` and you should see the path to blop's root folder.

Next, you need to set up the database. You must have postgres running on your machine.
Run `psql`
In the shell (is this a shell? idk) run `create database blop;` and then `\l` - make sure `blop` is one of the listed databases. Next you need to create an enum type -- for the column in the database containing an enum (a list of acceptable strings). Run `CREATE TYPE general_enum as ENUM ('Off Campus', 'Outside On Campus', 'Residence Hall', 'Other Campus Building');`. Then run `\q` to quit.

Next, from the root folder of blop, run `python scripts/manage.py db upgrade`

Then to seed the database with types and locations, run `python scripts/manage.py loc_seed` (locations) and `python scripts/manage.py type_seed` (types)

Aaaaand we should be good to go!


To add practice incidents to the database for development purposes, run `python scripts/manage.py add_fake_incidents`


_________________________________________________________________________



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













