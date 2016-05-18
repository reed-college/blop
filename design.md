This is a two-part project:

First: we'll create something very akin to a web-based CSO blotter.  This will be a web view showing a log in which each entry briefly details an event the CSOs responded to on campus. There will be sorting and filtering capabilities of a relatively high-level sort: 

- Category of response (e.g. AOD, Injury, Student Locked out of Dorm Room)
- Occurrence, both in terms of time range (last 7 days) and time of day
  ("things which happened between 10pm and 5am")

Next, we'll work with Justine Wang, who has been building maps of the campus, and the Strabo team to put a web front-end on this "blotter", allowing the events to be showing across the campus with the same filtering as the blotter. A person should be able to click back and forth between an event on a map and the blotter description of it.


Questions
-Do the CSOs have a database of sorts with this information that we can copy from? (e.g. categories of incidents, coded locations, etc.) - is it stored digitally, can we use it?
-who is the intended audience? who will have access?
-What should the sorting feature look like? A drop-down menu?
-How should authentication be handled? Do you have to sign in to be able to see the blotter/map, or only to be able to add an incident? And should that be Reed login info, or a separate authentication system?
-How should campus be split up, esp. non-buildings (e.g. "Reed lake", "southeastern front lawn"), and should the locations on the map be specifically exactly where the event happened, or should they just show the region?
- Do we only need (1) incident, (2) location, (3) time/date stamp? Or will there be a space for "response/comments/etc." and what should that look like?
-assuming a "pins on a map" model: should the pins be color-coded by incident? should there be an indicator of "newness"?
-Any other features? If students/community members are an intended audience, should there be a feedback/comments feature?
-should this be one of those accessible-only-on-campus sites?



Sorting capabilities:
	-sort by incident
	-sort by date & time range

Database:
	-locations on campus
	-type of incident

Authentication: Reed Kerberos Login

Pages:
	-login page
	-map page
	-either individual pages for each event, or a 'bubble' that would appear when you click on the map, with info?
	-live-feed blotter page, most recent posts at the top, able to load older posts via a button at the bottom of the page
	-comments/questions/feedback submission page???

Navigation bar (visible on all pages):
	-Non-Admin: links to map page, live blotter page, (comments submission page)
	-Admin: Add link to event submission page, (comments page or link to export comments/feedback)








