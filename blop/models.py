from blop.app import db


class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15))
    description = db.Column(db.String(100))

    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __repr__(self):
        return '<Incident Type {}>'.format(self.code)


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    general = db.Column(db.Enum("Off Campus", "Outside On Campus",
                                "Residence Hall", "Other Campus Building",
                                name="general_enum"))
    incidents = db.relationship('Incident', backref='location',
                                lazy='dynamic')

    def __init__(self, name, general):
        self.name = name
        self.general = general

    def __repr__(self):
        return '<Specific Location {}>'.format(self.name)


class Incident(db.Model):
    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    summary = db.Column(db.String(500))
    types = db.relationship('Type', secondary='mapping',
                            cascade='all',
                            backref=db.backref('incident',
                                               cascade="all",
                                               lazy='dynamic'))
    location_id = db.Column(db.Integer, db.ForeignKey(
                                    'locations.id'))

    def __init__(self, datetime, summary, types, location):
        self.datetime = datetime
        self.summary = summary
        self.location = location
        self.types = types

    def __repr__(self):
        return '<incident {}>'.format(self.datetime)

mapping = db.Table('mapping',
                   db.Column('type_id', db.Integer, db.ForeignKey('types.id',
                             ondelete='cascade')),
                   db.Column('incident_id', db.Integer,
                             db.ForeignKey('incidents.id', ondelete='cascade'))
                   )
