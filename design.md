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









