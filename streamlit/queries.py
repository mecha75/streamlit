from sqlalchemy import create_engine, select, delete, and_, insert, func, update, or_
from datetime import datetime
from models import salesRecord, salesGroupMaster, exRate

# 전체 (구분없이, 실적)
sql_lv1 = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(A)'
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(A)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name'
).order_by('lv1Code')

sql_lv2 = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    (salesGroupMaster.Group_lv2_code).label('lv2Code'),
    (salesGroupMaster.Group_lv2).label('lv2Name'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(A)'
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(A)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name', 'lv2Code', 'lv2Name'
).order_by('lv1Code','lv2Code')

sql_lv3 = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    (salesGroupMaster.Group_lv2_code).label('lv2Code'),
    (salesGroupMaster.Group_lv2).label('lv2Name'),
    (salesGroupMaster.Group_lv3_code).label('lv3Code'),
    (salesGroupMaster.Group_lv3).label('lv3Name'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(A)'
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(A)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name', 'lv2Code', 'lv2Name', 'lv3Code', 'lv3Name'
).order_by('lv1Code','lv2Code','lv3Code')

# HVP
sql_lv1_HVP = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    (salesRecord.HVP).label('HVP'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    and_(salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(A)'
        #  salesRecord.HVP == 'HVP'
    )
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(A)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name', 'HVP'
).order_by('lv1Code')

sql_lv2_HVP = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    (salesGroupMaster.Group_lv2_code).label('lv2Code'),
    (salesGroupMaster.Group_lv2).label('lv2Name'),
    (salesRecord.HVP).label('HVP'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    and_(salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(A)'
        #  salesRecord.HVP == 'HVP'
    )
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(A)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name', 'lv2Code', 'lv2Name','HVP'
).order_by('lv1Code')

sql_lv3_HVP = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    (salesGroupMaster.Group_lv2_code).label('lv2Code'),
    (salesGroupMaster.Group_lv2).label('lv2Name'),
    (salesGroupMaster.Group_lv3_code).label('lv3Code'),
    (salesGroupMaster.Group_lv3).label('lv3Name'),
    (salesRecord.HVP).label('HVP'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    and_(salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(A)'
        #  salesRecord.HVP == 'HVP'
    )
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(A)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name', 'lv2Code', 'lv2Name','lv3Code', 'lv3Name','HVP'
).order_by('lv1Code')

# 인치별
sql_lv2_RIM = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    (salesGroupMaster.Group_lv2_code).label('lv2Code'),
    (salesGroupMaster.Group_lv2).label('lv2Name'),
    (salesRecord.Rim).label('RIM'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    and_(salesRecord.SalesType == '타이어매출',
        salesRecord.version == '(A)'
        #  salesRecord.HVP == 'HVP'
    )
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(A)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name', 'lv2Code', 'lv2Name', 'RIM'
).order_by('lv1Code')

sql_RIM = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesRecord.Rim).label('RIM'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    and_(salesRecord.SalesType == '타이어매출'
        #  salesRecord.HVP == 'HVP'
    )
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(A)')
)).group_by(
    'YYYY', 'mm', 'RIM'
).order_by('lv1Code')

# 계획 전체 (구분없이, 실적)
sql_plan_lv1 = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(P)'
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(P)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name'
).order_by('lv1Code')

sql_plan_lv2 = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    (salesGroupMaster.Group_lv2_code).label('lv2Code'),
    (salesGroupMaster.Group_lv2).label('lv2Name'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(P)'
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(P)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name', 'lv2Code', 'lv2Name'
).order_by('lv1Code','lv2Code')

sql_plan_lv3 = select (
    (salesRecord.year).label('YYYY'),
    (salesRecord.mm).label('mm'),
    (salesGroupMaster.Group_lv1_code).label('lv1Code'),
    (salesGroupMaster.Group_lv1).label('lv1Name'),
    (salesGroupMaster.Group_lv2_code).label('lv2Code'),
    (salesGroupMaster.Group_lv2).label('lv2Name'),
    (salesGroupMaster.Group_lv3_code).label('lv3Code'),
    (salesGroupMaster.Group_lv3).label('lv3Name'),
    func.sum(salesRecord.Sales*exRate.rate/1000000).label('sales'),
    func.sum(salesRecord.EA/1000).label('kEA'),
    func.sum(salesRecord.Weight/1000).label('ton')
).outerjoin(salesGroupMaster, 
            and_(
                salesRecord.DistributeChannel==salesGroupMaster.DistributeChannel,
                salesRecord.SalesGroup==salesGroupMaster.SalesGroup,
                )
).where(
    salesRecord.SalesType == '타이어매출',
    salesRecord.version == '(P)'
).outerjoin(exRate,and_(
    salesRecord.year == exRate.year,
    salesRecord.mm == exRate.mm,
    salesRecord.curr == exRate.curr,
    exRate.version == func.concat(salesRecord.year,'-00-(P)')
)).group_by(
    'YYYY', 'mm', 'lv1Code', 'lv1Name', 'lv2Code', 'lv2Name', 'lv3Code', 'lv3Name'
).order_by('lv1Code','lv2Code','lv3Code')
