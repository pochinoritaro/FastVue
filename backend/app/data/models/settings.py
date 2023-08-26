from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Test.db', echo=True)

session = scoped_session(
					sessionmaker(
							autocommit = False,
							autoflush = True,
							bind = engine
						)
					)

Base = declarative_base()
Base.query = session.query_property()
