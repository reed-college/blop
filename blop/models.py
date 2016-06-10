from flask_sqlalchemy import SQLAlchemy
from blop.app import app, db

class Admin(db.Model):
	__tablename__ = 'admin'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(25))
	password = db.Column(db.String(25))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return '<user {}>'.format(self.username)

class Type(db.Model):
	__tablename__ = 'types'

	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(15))
	description = db.Column(db.String(100))

	def __init__(self, id, code, description):
		self.id = id
		self.code = code
		self.description = description

	def __repr__(self):
		return '<Incident Type {}>'.format(self.description)

class GeneralLocation(db.Model):
	__tablename__ = 'general_locations'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	specloc = db.relationship('SpecificLocation', backref='general_location', lazy='dynamic')
	incidents = db.relationship('Incident', backref='general_location', lazy='dynamic')

	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __repr__(self):
		return '<General Location {}>'.format(self.name)

class SpecificLocation(db.Model):
	__tablename__ = 'specific_locations'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	general_location_id = db.Column(db.Integer, db.ForeignKey('general_locations.id'))
	incidents = db.relationship('Incident', backref='specific_location', lazy='dynamic')

	def __init__(self, id, name, general_location_id):
		self.id = id
		self.name = name
		self.general_location_id = general_location_id

	def __repr__(self):
		return '<Specific Location {}>'.format(self.name)

class Incident(db.Model):
	__tablename__ = 'incidents'

	id = db.Column(db.Integer, primary_key = True)
	date = db.Column(db.Date)
	time = db.Column(db.Time)
	summary = db.Column(db.String(500))
	type_mapping = db.relationship('Type', secondary='mapping', backref=db.backref('incident', lazy='dynamic'))
	general_location_id = db.Column(db.Integer, db.ForeignKey('general_locations.id'))
	specific_location_id = db.Column(db.Integer, db.ForeignKey('specific_locations.id'))

	def __init__(self, id, date, time, summary, type_id, general_location_id, specific_location_id):
		self.id = id
		self.date = date
		self.time = time
		self.summary = summary
		self.general_location_id = general_location_id
		self.specific_location_id = specific_location_id

	def __repr__(self):
		return '<incident {}>'.format(self.id)

mapping = db.Table('mapping', 
	db.Column('type_id', db.Integer, db.ForeignKey('types.id')),
	db.Column('incident_id', db.Integer, db.ForeignKey('incidents.id'))
)

if __name__ == '__main__':
    manager.run()
