from app import db
from models.setting.subject import Subject


def get_all_by_user_id(user_id: int):
    return Subject.query.filter(Subject.user_id == user_id, Subject.visable == '1')


def get_all_by_category_id_and_user_id(id: int, user_id: int):
    return Subject.query.filter(Subject.category_id == id, Subject.user_id == user_id, Subject.visable == '1')


def add(subject: Subject):
    db.session.add(subject)
    db.session.commit()


def record_amount_increment_one(id, user_id):
    subject = Subject.query.filter(
        Subject.id == id, Subject.user_id == user_id).first()
    subject.record_sum = subject.record_sum+1
    db.session.commit()
