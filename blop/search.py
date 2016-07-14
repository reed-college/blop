import datetime
from sqlalchemy import between, and_
from blop import models
from sqlalchemy.sql import select

def search(form_object):
    result,a,b,c,d=[],[],[],[],[]
    
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

    #StartDatetime=datetime.datetime(int(form_object['start_year']),
     #                               int(form_object['start_month']),
      #                              int(form_object['start_day']),
       #                             int(form_object['start_hour']),
        #                            int(form_object['start_minute']))
    #EndDatetime=datetime.datetime(int(form_object['end_year']),
     #                             int(form_object['end_month']),
      #                            int(form_object['end_day']),
       #                           int(form_object['end_hour']),
        #                          int(form_object['end_minute']))

    StartDate= datetime.datetime(int(form_object['start_year']),
                             int(form_object['start_month']),
                             int(form_object['start_day']),
                             0,0)

    EndDate= datetime.datetime(int(form_object['end_year']),
                             int(form_object['end_month']),
                             int(form_object['end_day']),
                             23,59)

    StartTime=datetime.datetime(2000,1,1,int(form_object['start_hour']),int(form_object['start_minute']))
    EndTime=datetime.datetime(2015,12,28,int(form_object['end_hour']),int(form_object['end_minute']))

    t1,t2=[],[]

    drange = models.Incident.query.filter(models.Incident.datetime>=StartDate, models.Incident.datetime<=EndDate).all()
    for i in drange:
        t1.append(i)
    print(t1)

    trange = models.Incident.query.filter(models.Incident.datetime>=StartTime, models.Incident.datetime<=EndTime).all()
    for i in trange:
        t2.append(i)
    print(t2)

    a.append(set(t1).intersection(t2))
    print(a)
    
    if form_object['locations']!='0':
    locs = models.Incident.query.filter(models.Incident.location.name == form_object['locations']).all()
    for l in locs:
        b.append(l)
        
    if form_object['incidents']!='0':
        c.append(models.Incident.query.filter(models.Incident.types.description==form_object['incidents']).all())
            
    if form_object['textbox']!='0':
        incident= models.Incident.query.all()
        text=form_object['textbox']
        for row in incident:
            if text in row.summary:
                d.append(row)

    result.append(list(set().intersection(a,b,c,d)))
    return result