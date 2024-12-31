from datetime import datetime
from apps.app import db


class mission(db.Model):
    __tablename__ = "mission"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, index=True)
    statement = db.Column(db.String(5000))
    acts_principal = db.Column(db.Text)
    acts_subprincipal = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, default = datetime.now)

class preciousAnswer(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, index=True)
    answer_no1 = db.Column(db.Text)
    answer_no2 = db.Column(db.Text)
    answer_no3 = db.Column(db.Text)
    answer_no4 = db.Column(db.Text)
    answer_no5 = db.Column(db.Text)
    answer_no6 = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default = datetime.now)

class rollPosition(db.Model):
    __tablename__ = "position"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, index=True)
    roll = db.Column(db.Text)
    area_avility = db.Column(db.Text)
    area_concern = db.Column(db.Text)
    area_weakness = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default = datetime.now)

class roleAndrule(db.Model):
    __tablename__ = "roleplay"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True)
    role = db.Column(db.String(20))
    role_name = db.Column(db.String(500))
    principal = db.Column(db.String(2000))
    create_at = db.Column(db.DateTime, default = datetime.now)

class target_week_role(db.Model):
    __tablename__ = "roleweek"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True)
    role = db.Column(db.String(500))
    year = db.Column(db.String(4))
    week = db.Column(db.String(8))
    order = db.Column(db.String(4))
    activity = db.Column(db.String(2000))
    status = db.Column(db.String(20))
    create_at = db.Column(db.DateTime, default = datetime.now)

class target_day_activity(db.Model):
    __tablename__ = "dailyactivity"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True)
    year = db.Column(db.String(4))
    week = db.Column(db.String(8))
    date = db.Column(db.String(2))
    day = db.Column(db.String(3))
    time = db.Column(db.String(4))
    activity = db.Column(db.String(2000))
    status = db.Column(db.String(20))
    create_at = db.Column(db.DateTime, default = datetime.now)

class habbit_7th(db.Model):
    __tablename__ = "habbit7"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True)
    year = db.Column(db.String(4))
    week = db.Column(db.String(8))
    category = db.Column(db.String(20))
    activity = db.Column(db.String(2000))
    create_at = db.Column(db.DateTime, default = datetime.now)
