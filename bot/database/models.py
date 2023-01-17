from sqlalchemy import Column, String, Integer
from database.config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tel_id = Column(Integer)
    first_name = Column(String)
    username = Column(String)
    points = Column(Integer)

    def __init__(self, tel_id, first_name, username, points):
        self.tel_id = tel_id
        self.first_name = first_name
        self.username = username
        self.points = points


class Sponser(Base):
    __tablename__ = 'sponsers'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    channel_url = Column(String)

    def __init__(self, tite, channel_url) -> None:
        self.title = tite
        self.channel_url = channel_url
