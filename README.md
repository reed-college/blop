BLOP
====

The app's primary function is to display Reed College Community Safety Incident data in two forms: as a live-feed blotter and as clickable icons on a map of campus. 


INSTALLATION INSTRUCTIONS
=========================
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


Once you have the repo cloned and are working on your branch (`git branch` will tell you which branch you're on. `git checkout [branch]` will switch branches. don't change things locally on the master branch...), create your virtualenv however you do that. Instructions here assume you use(d) virtualenvwrapper.

run `pip install -r requirements.txt`

Then we need to set the PYTHONPATH environment variable, so that the path when you activate your virtual environment is the root folder of the blop directory. Using virtualenvwrapper, that means you have to set the variable in the 'postactivate' hook inside the folder that contains your virtualenvs. To find that folder, run `echo $WORKON_HOME` ... for me this is 
`~/.python_virtualenvs`. 

run `subl/nano/vim ~/[folder_containing_virtualenvs]/[blop_virtual_env_name]/bin/postactivate`
So for me it's: `subl ~/.python_virtualenvs/blop/bin/postactivate`
Type in that document `export PYTHONPATH=[path_to_blop_root_folder]`
So for me it's `export PYTHONPATH=~/SDS/blop`
Save and exit.
De-activate and re-activate your virtual environment, then run `echo $PYTHONPATH` and you should see the path to blop's root folder.

Next, you need to set up the database. You must have postgres running on your machine.
Run `psql`
In the shell run `create database blop;` and then `\l` - make sure `blop` is one of the listed databases. Next you need to create an enum type -- for the column in the database containing an enum (a list of acceptable strings). Run `CREATE TYPE general_enum as ENUM ('Off Campus', 'Outside On Campus', 'Residence Hall', 'Other Campus Building');`. Then run `\q` to quit.

Next, from the root folder of blop, run `python scripts/manage.py db upgrade`

Then to seed the database with types and locations, run `python scripts/manage.py loc_seed` (locations) and `python scripts/manage.py type_seed` (types)

To add practice incidents to the database for development purposes, run `python scripts/manage.py add_fake_incidents`


DATABASE SCHEMA
===============

Blop's database contains three tables. The table classes and columns can be viewed in `blop/models.py`. Two of these tables--locations and types--are relatively static; they contain the location names/codes and type descriptions/codes for different kinds of incidents on campus. Both Types and Locations include a unique ID primary key column. 

The `code` column in both tables contains the abbreviated codes used by Community Safety to classify incidents, and the `description` column in the Types table as well as the `name` column in the Location table contain plain English descriptions/names for the types/locations. For example, one row in the types table contains the code HARA and the description `Harassment`



INCIDENT SUBMISSIONS
====================

BLOTTER DISPLAY
===============

MAP DISPLAY
===========

SEARCH FUNCTION
===============

EDITING SUBMITTED EVENTS
========================

