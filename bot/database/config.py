from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db.sqlite", echo=False,
                       connect_args={"check_same_thread": False})
Base = declarative_base()
Session = sessionmaker(bind=engine)
db = Session()
