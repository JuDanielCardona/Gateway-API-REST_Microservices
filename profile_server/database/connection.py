from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://admin:12345@localhost:5432/profiles_db')

Session = sessionmaker(bind=engine)

def Connection():
    return Session()
