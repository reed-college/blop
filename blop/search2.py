import datetime
from sqlalchemy import between, and_
from blop import models
from sqlalchemy.sql import select, desc
from blop.app import db

def search(form_object):
    
    if form_object['ampm_start']=='am':    
        if form_object['start_hour']=='12':
            form_object['start_hour']='00'

    if form_object['ampm_start']=='pm' and form_object['start_hour']!='12':
        form_object['start_hour']= int(form_object['start_hour'])+12    

    if form_object['ampm_end']=='am':
        if form_object['end_hour']=='12':
            form_object['end_hour']='00'

    if form_object['ampm_end']=='pm' and form_object['end_hour']!='12':
        form_object['end_hour']= int(form_object['end_hour'])+12

    StartDate= datetime.datetime(int(form_object['start_year']),
                             int(form_object['start_month']),
                             int(form_object['start_day']),
                             0,0)

    EndDate= datetime.datetime(int(form_object['end_year']),
                             int(form_object['end_month']),
                             int(form_object['end_day']),
                             23,59)

    StartTime=datetime.datetime(2000,1,1,int(form_object['start_hour']),
                                int(form_object['start_minute']))

    EndTime=datetime.datetime(2015,12,28,int(form_object['end_hour']),
                              int(form_object['end_minute']))

    c = []
    datequery = db.session.query(models.Incident).order_by(desc(models.Incident.datetime)).all()
    for d in datequery:
        if d.datetime.date()>=StartDate.date():
            if d.datetime.date() <= EndDate.date():
                c.append(d)

    d = []
    query = db.session.query(models.Incident).order_by(desc(models.Incident.datetime)).all()
    for t in query:
        if t.datetime.time()>=StartTime.time():
            if t.datetime.time() <= EndTime.time():
                d.append(t)

    result = [val for val in c if val in d] 

    if form_object['locations']!='0':
        loc = form_object.getlist('locations',type=str)
        a = []
        for l in loc:
            for t in query:
                if l==t.location.name:
                    a.append(t)
        result=list(set(result).intersection(a))

    if form_object['incidents']!='0':
        types = form_object.getlist('incidents',type=str)
        b=[]
        if form_object['and_or']=='or':
            for t in query:
                inctypes = t.types
                for i in inctypes:
                    for each in types:
                        if i.description == each:
                            b.append(t)
        else:
            for t in query:
                if set(types)==set(t.types):
                    b.append(t)
        result=list(set(result).intersection(b))

    print(result)