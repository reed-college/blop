from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import csv

from blop.app import app, db

from blop import models

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def seed():
	"Add seed data to the database."

	models.SpecificLocation.query.delete()
	models.GeneralLocation.query.delete()
	models.Type.query.delete()

	with open('general_locations.csv', 'r') as csvfile:
		genlocreader = csv.DictReader(csvfile, delimiter=',')
		for row in genlocreader:
			genlocs = models.GeneralLocation(id=row['id'], name=row['name'], oncampus=row['oncampus'])
			db.session.add(genlocs)

	
	with open('location_codes.csv', 'r') as csvfile:
		loccodereader = csv.DictReader(csvfile, delimiter=',')
		for row in loccodereader:
			loccode = models.SpecificLocation(id=row['id'], name=row['name'], general_location_id=row['general_location_id'])
			db.session.add(loccode)

	
	with open('incident_types.csv', 'r') as csvfile:
		typereader = csv.DictReader(csvfile, delimiter=',')
		for row in typereader:
			typecode = models.Type(id=row['id'], code=row['code'], description=row['description'])
			db.session.add(typecode)



	db.session.commit()
	




if __name__ == '__main__':
	manager.run()