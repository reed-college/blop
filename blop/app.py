from flask import Flask, render_template, request, redirect, url_for
from blop import db
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.sql import desc

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = db.db_url

db = SQLAlchemy(app)

from blop import models

POSTS_PER_PAGE = 20

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    types = db.session.query(models.Type).order_by(models.Type.code).all()
    locations = db.session.query(models.Location).order_by(models.Location.name).all()
    return render_template('submit.html', types=types, locations=locations)


@app.route('/blotter')
@app.route('/blotter/<int:page>')
def blotter(page=1):
    incidents = models.Incident.query.order_by('datetime desc').paginate(page, POSTS_PER_PAGE, False)
    return render_template('blotter.html', title='Live Feed', incidents=incidents)

@app.route('/')
@app.route('/map')
def maps():
    return render_template('map.html')


@app.route('/search/')
def search():
    types = db.session.query(models.Type).order_by(models.Type.description).all()
    locations = db.session.query(models.Location).order_by(models.Location.name).all()
    return render_template('search.html', types=types, locations=locations)


@app.route('/processform', methods=['GET', 'POST'])
def processform():

    types = []
    codelist = request.form.getlist('incidents', type=int)
    for c in codelist:
        typ = db.session.query(models.Type).filter(models.Type.id == c).first()
        types.append(typ)

    loc = int(request.form['location'])
    location = db.session.query(models.Location).filter(models.Location.id == loc).first()

    month = int(request.form['month dropdown'])
    day = int(request.form['day dropdown'])
    year = int(request.form['year dropdown'])
    hour = int(request.form['hour dropdown'])
    ampm = int(request.form['AM/PM dropdown'])
    if ampm == 1:
        if hour != 12:
            hour = hour + 12
    else:
        if hour == 12:
            hour = 00
    minute = int(request.form['minute dropdown'])

    dt = datetime.datetime(year, month, day, hour, minute)

    incident_summary = str(request.form['summary field'])

    incident = models.Incident(
                               datetime=dt,
                               summary=incident_summary,
                               location_id=location.id,
                               types=types
                               )

    db.session.add(incident)
    db.session.commit()

    return redirect(url_for('blotter'))

@app.route('/blottersearch', methods=['GET', 'POST'])
def blottersearch():
    
    starthour = int(request.form['start_hour'])
    if request.form['ampm_start']=='am':    
        if starthour == 12:
            starthour = 00

    if request.form['ampm_start']=='pm' and starthour != 00:
        starthour = starthour + 12    

    endhour = int(request.form['end_hour'])
    if request.form['ampm_end'] == 'am':
        if endhour == 12:
            endhour == 00

    if request.form['ampm_end'] == 'pm' and endhour != 00:
        endhour = endhour + 12

    startyear = int(request.form['start_year'])
    startmonth = int(request.form['start_month'])
    startday = int(request.form['start_day'])

    endyear = int(request.form['end_year'])
    endmonth = int(request.form['end_month'])
    endday = int(request.form['end_day'])  

    today = datetime.datetime.today()

    if startyear == 0000:
        startyear = today.year - 1
    if startmonth == 0:
        startmonth = today.month
    if startday == 0:
        startday = today.day
    if endyear == 0000:
        endyear = today.year
    if endmonth == 0:
        endmonth = today.month
    if endday == 0:
        endday = today.day

    startdate= datetime.datetime(startyear,
                             startmonth,
                             startday,
                             0,0)

    enddate= datetime.datetime(endyear,
                             endmonth,
                             endday,
                             23,59)

    starttime=datetime.datetime(2000,1,1,starthour,
                                int(request.form['start_minute']))

    endtime=datetime.datetime(2015,12,28,endhour,
                              int(request.form['end_minute']))

    datefilter = []
    query = db.session.query(models.Incident).order_by(desc(models.Incident.datetime)).all()
    for q in query:
        if q.datetime.date()>=startdate.date():
            if q.datetime.date() <= enddate.date():
                datefilter.append(q)

    timefilter = []
    for q in query:
        if q.datetime.time()>=starttime.time():
            if q.datetime.time() <= endtime.time():
                timefilter.append(q)

    result = [val for val in datefilter if val in timefilter]

    if request.form['location']!='0':
        locs = request.form.getlist('location',type=int)
        locationfilter = []
        for l in locs:
            for q in query:
                if l == q.location_id:
                    locationfilter.append(q)
        result=list(set(result).intersection(locationfilter))


    if request.form['incidents']!='0':
        types = request.form.getlist('incidents',type=int)
        typefilter=[]
        if request.form['and_or'] == 'or':
            for q in query:
                inctypes = q.types
                for i in inctypes:
                    for t in types:
                        if i.id == t:
                            typefilter.append(q)
        else:
            for q in query:
                ttypes = []
                for r in q.types:
                    tid = r.id
                    ttypes.append(tid)
                if set(types)==set(ttypes):
                    typefilter.append(q)
                    ttypes = []


        result=list(set(result).intersection(typefilter))

    if request.form['search textarea']!='':
        slist = request.form['search textarea'].split()
        sstring = "|".join(slist)
        summaryfilter = db.session.query(models.Incident).filter(db.func.to_tsvector(models.Incident.summary).match(sstring)).all()
        result=list(set(result).intersection(summaryfilter))
    result = sorted(result, key= lambda incident: incident.datetime, reverse = True)
    return render_template('blottersearch.html', result = result)

if __name__ == '__main__':
    app.run()
