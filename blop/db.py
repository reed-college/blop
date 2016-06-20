
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from .config import app_config

db_url = app_config['database']['url']
debug = app_config.getboolean('app', 'debug')
engine = sqlalchemy.create_engine(db_url, echo=debug)


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
