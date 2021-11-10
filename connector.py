import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import NullPool
import urllib, sys
sys.path.append("..")
import Lelo
global db

Base = declarative_base()
db = SQLAlchemy(Lelo.app)


engine = sqlalchemy.create_engine("mysql://mqtt:#F1-Lelo~ç@localhost/mqtt",  poolclass=NullPool)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# db.create_all()