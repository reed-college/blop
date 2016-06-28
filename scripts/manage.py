from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import csv
import datetime

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
            loccode = models.Location(name=row['name'], general=row[
                                              'general'])
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
def add_fake_incidents():

    incidents = db.session.query(models.Incident).all()
    for incident in incidents:
        types = incident.types
        for t in types:
            incident.types.remove(t)
    models.Incident.query.delete()

    # insert function to add fake incidents
    location = models.Location.query.filter(models.Location.name ==
                                            "Foster").first()
    types = [models.Type.query.filter(models.Type.code == "UAA").first(),
             models.Type.query.filter(models.Type.code == "THEB").first(),
             models.Type.query.filter(models.Type.code == "HARA").first()]

    summary = "practice event in foster-unattended alc, bike theft, harassment"
    incident = models.Incident(
                            datetime=datetime.datetime(2016, 8, 13, 19, 00),
                            summary=summary,
                            types=types,
                            location=location
    )
    db.session.add(incident)
    db.session.commit()

    location = models.Location.query.filter(models.Location.name ==
                                            "Chittick").first()
    types = [models.Type.query.filter(models.Type.code == "BOM").first(),
             models.Type.query.filter(models.Type.code == "AODMJ").first()]

    summary = "practice event in chittick-bomb threat, marijuana AOD"
    incident = models.Incident(
                                datetime=datetime.datetime(2016, 4, 25, 6, 23),
                                summary=summary,
                                types=types,
                                location=location
    )
    print(incident.datetime, incident.types, incident.summary, incident.location)
    db.session.add(incident)
    db.session.commit()

    location = models.Location.query.filter(models.Location.name ==
                                            "Eliot Hall").first()
    types = [models.Type.query.filter(models.Type.code == "ALF").first(),
             models.Type.query.filter(models.Type.code == "DIS").first()]

    summary = "practice event in Eliot-fire alarm, disturbance"
    incident = models.Incident(
                                datetime=datetime.datetime(2016, 2, 14, 18, 5),
                                summary=summary,
                                types=types,
                                location=location
    )
    db.session.add(incident)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
