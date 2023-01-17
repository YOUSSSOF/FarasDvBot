from database.models import User, Sponser
from database.config import db


def post_user(tel_id, first_name, username):
    user = db.query(User).filter(User.tel_id == tel_id).first()
    if user:
        return
    new_user = User(
        tel_id=tel_id,
        first_name=first_name,
        username=username,
        points=0
    )
    db.add(new_user)
    db.commit()


def get_users():
    return db.query(User).all()


def get_user(id):
    return db.query(User).filter(User.tel_id == id).first()


def add_point(id):
    user = get_user(id)
    user.points += 1
    db.commit()


def decrease_points(id, num):
    user = get_user(id)
    user.points -= num
    db.commit()


def post_sponser(title, channel_url):
    sponser = db.query(Sponser).filter(
        Sponser.channel_url == channel_url).first()
    if sponser:
        return
    new_sponser = Sponser(
        tite=title,
        channel_url=channel_url
    )
    db.add(new_sponser)
    db.commit()


def get_sponsers():
    return db.query(Sponser).all()


def remove_sponser(id):
    sponser = db.query(Sponser).filter(Sponser.id == id).first()
    if not sponser:
        return
    db.delete(sponser)
    db.commit()
