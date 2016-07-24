from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import csv
import datetime
import random

from blop.app import app, db

from blop import models

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def loc_seed():

    with open('location_codes.csv', 'r') as csvfile:
        loccodereader = csv.DictReader(csvfile, delimiter=',')
        for row in loccodereader:
            loccode = models.Location(name=row['name'])
            db.session.add(loccode)
            db.session.commit()


@manager.command
def type_seed():

    models.Type.query.delete()

    with open('incident_types.csv', 'r') as csvfile:
        typereader = csv.DictReader(csvfile, delimiter=',')
        for row in typereader:
            typecode = models.Type(code=row['code'],
                                   description=row['description'])
            db.session.add(typecode)
            db.session.commit()


@manager.command
def add_fake_incidents(): # adds 100 fake incidents to the database for dev

# the loop here deletes everything currently in the incident table
# first the db is queried
   # incidents = db.session.query(models.Incident).all()
  #  for incident in incidents: # sets up that this applies for each row
    #    types = incident.types # queries the type column speficically
   #     for t in types: # for loop deletes everything in the types column
  #          incident.types.remove(t)
 #   models.Incident.query.delete() #deletes the incident
# the types column has to be emptied because the many-to-many relationship is
# complicated and won't easily allow us to delete things from the incidents
# table if they would leave 'orphans' in the type mapping table


    # the following creates 100 random incidents
    with open("wordlist.txt") as f: #this creates a list of words that will be
        word_list = [] # used to create random summaries later.
        for line in f:
            word_list.append(line.strip())

    for _ in range(1500): #sets up the following to happen 100 times
        Typequery = db.session.query(models.Type) #queries Type table
        rowCount = int(Typequery.count()) # counts rows in type table
        typeOne = Typequery.offset(int(rowCount*random.random())).first()
    # the above and below select a random row from the type table
        typeTwo = Typequery.offset(int(rowCount*random.random())).first()

        if typeOne == typeTwo: #this makes it so the two types aren't the same
            typeTwo = Typequery.offset(int(rowCount*random.random())).first()

        Locquery = db.session.query(models.Location) #same as for typequery
        rowCount = int(Locquery.count())
        location = Locquery.offset(int(rowCount*random.random())).first()

    # the next part of this creates a random string of common words for the summary
        summarylist = []
        for _ in range(10):
            a = random.choice(word_list) #selects a word from the list above
            summarylist.append(a) #appends that word to the list of summary words

        summary = ' '.join(word for word in summarylist) #turns list into string

    # the following lines generate random date and time values and create
    # a datetime object
        year = random.randint(2000, 2015)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        dt = datetime.datetime(year, month, day, hour, minute)


    # finally! The incident is created using our randomly generated variables.
        incident = models.Incident(
                                   datetime=dt,
                                   summary=summary,
                                   types=[typeOne, typeTwo],
                                   location=location
        )
        db.session.add(incident) #then it's added to the db and committed.
        db.session.commit()

 
if __name__ == '__main__':
    manager.run()