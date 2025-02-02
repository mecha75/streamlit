from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

user1 = "superpower"
pw1 = "mecha75"
ip1 = "138.2.44.37:3306"
db1 = "flaskbook"
mysql_url = f"mysql+pymysql://{user1}:{pw1}@{ip1}/{db1}?charset=utf8"

class salesRecord(db.Model):
    __tablename__ = "sales_record"
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(12)) #, db.ForeignKey("version.version"))
    year = db.Column(db.String(4))
    mm = db.Column(db.String(2))
    yyyymm = db.Column(db.String(7))
    SalesType = db.Column(db.String(20))
    company = db.Column(db.String(4))
    companyName = db.Column(db.String(40))
    SalesGroup = db.Column(db.String(3))
    SalesGroupName = db.Column(db.String(100))
    DistributeChannel = db.Column(db.String(2))
    DistributeChannelName = db.Column(db.String(100))
    Usage = db.Column(db.String(20))
    Origin = db.Column(db.String(20))
    ProdPlant = db.Column(db.String(20))
    ProdGrp = db.Column(db.String(2))
    ProdGrpName = db.Column(db.String(40))
    Rim = db.Column(db.String(5))
    subGroup = db.Column(db.String(8))
    HVP = db.Column(db.String(20))
    HVP2 = db.Column(db.String(20))
    curr = db.Column(db.String(3))
    EA = db.Column(db.Numeric(precision=12, scale=2))
    Weight = db.Column(db.Numeric(precision=13, scale=2))
    Sales = db.Column(db.Numeric(precision=22, scale=2))
    CGS = db.Column(db.Numeric(precision=22, scale=2))
    CGM = db.Column(db.Numeric(precision=22, scale=2))
    Material = db.Column(db.Numeric(precision=22, scale=2))
    DirectLabor = db.Column(db.Numeric(precision=22, scale=2))
    IndirectLabor = db.Column(db.Numeric(precision=22, scale=2))
    DirectOH = db.Column(db.Numeric(precision=22, scale=2))
    IndirectOH = db.Column(db.Numeric(precision=22, scale=2))
    Freight = db.Column(db.Numeric(precision=22, scale=2))
    Insure_ex = db.Column(db.Numeric(precision=22, scale=2))
    CGS_other = db.Column(db.Numeric(precision=22, scale=2))
    CustomReturn = db.Column(db.Numeric(precision=22, scale=2))
    GP = db.Column(db.Numeric(precision=22, scale=2))
    SalesExpences = db.Column(db.Numeric(precision=22, scale=2))
    AdminExpences = db.Column(db.Numeric(precision=22, scale=2))
    OperatingProfit2 = db.Column(db.Numeric(precision=22, scale=2))
    create_at = db.Column(db.DateTime, default = datetime.now())

class salesGroupMaster(db.Model):
    __tablename__ = "sales_group"
    id = db.Column(db.Integer, primary_key=True)
    SalesGroup = db.Column(db.String(3))
    DistributeChannel = db.Column(db.String(2))
    Group_lv1 = db.Column(db.String(30))
    Group_lv2 = db.Column(db.String(30))
    Group_lv3 = db.Column(db.String(30))
    Group_lv4 = db.Column(db.String(30))
    curr_lv1 = db.Column(db.String(3))
    curr_lv2 = db.Column(db.String(3))
    curr_lv3 = db.Column(db.String(3))
    curr_lv4 = db.Column(db.String(3))
    Group_lv1_code = db.Column(db.String(3))
    Group_lv2_code = db.Column(db.String(6))
    Group_lv3_code = db.Column(db.String(9))
    Group_lv4_code = db.Column(db.String(12))
    create_at = db.Column(db.DateTime, default = datetime.now())


class exRate(db.Model):
    __tablename__ = "ex_rate"
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(12)) #, db.ForeignKey("version.version"))
    year = db.Column(db.String(4))
    mm = db.Column(db.String(2))
    curr = db.Column(db.String(3))
    rate = db.Column(db.Numeric(precision=22, scale=2))
    user_id = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, default = datetime.now)

