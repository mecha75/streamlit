from sqlalchemy import select, delete, and_, insert, update, func, join, literal_column, outerjoin, or_
from apps.mission.models import mission as db_mission, preciousAnswer, rollPosition, roleAndrule, target_week_role, target_day_activity

sql_base = select(
    (db_mission.email).label('email'),
    (db_mission.statement).label('Mission'),
    (db_mission.acts_principal).label('Roll'),
    (db_mission.acts_subprincipal).label('submission')
)

sql_base_answer = select(
    (preciousAnswer.email).label('email'),
    (preciousAnswer.answer_no1).label('No1'),
    (preciousAnswer.answer_no2).label('No2'),
    (preciousAnswer.answer_no3).label('No3'),
    (preciousAnswer.answer_no4).label('No4'),
    (preciousAnswer.answer_no5).label('No5'),
    (preciousAnswer.answer_no6).label('No6')
)

sql_base_roll = select(
    (rollPosition.email).label('email'),
    (rollPosition.roll).label('roll'),
    (rollPosition.area_avility).label('avility'),
    (rollPosition.area_concern).label('expectation'),
    (rollPosition.area_weakness).label('weakness')     
)

question = [
    'No.1 당신은 시한부 판정을 받아 최대 3개월을 살 수 있습니다. 그기간에 무엇을 하시겠습니까?',
    'No.2 시한부 기간이 1년으로 바꾼다면 그때는 무엇을 하시겠습니까?',
    'No.3 출근길에 교통사고로 하반신 마비가 되었습니다. 앞으로 무엇을 하며 살고 싶습니까? 무엇을 잘하실 수 있습니까?',
    'No.4 내일 회사에서 짤리면 앞으로 무엇을 하면서 살 수 있을 것 같습니까?, 10년 뒤에 당신은 무엇을 하고 있을 것 같습니까?',
    'No.5 당신은 무엇을 잘하십니까?', 
    'No.6 당신이 잘하고 싶은 것은 무엇입니까?', 
]

status =[
    'enroll','complete','sucessfully complete', 'fail', 'suspend'
]

sql_collect_role = select(
    (roleAndrule.role_name).label('role')
).group_by('role_name')

sql_role_mission = select(
    (roleAndrule.role).label('role'),
    (roleAndrule.role_name).label('Definition'),
    (roleAndrule.principal).label('rule')
)


sql_activity_role_week = select(
    (target_week_role.id).label('id'),
    (target_week_role.email).label('email'),
    (target_week_role.role).label('role'),
    (target_week_role.year).label('year'),
    (target_week_role.week).label('week'),
    (target_week_role.order).label('order'),
    (target_week_role.activity).label('activity'),
    (target_week_role.status).label('status')
)

sql_activity_role_daily = select(
    (target_day_activity.id).label('id'),
    (target_day_activity.email).label('email'),
    (target_day_activity.year).label('year'),
    (target_day_activity.week).label('week'),
    (target_day_activity.date).label('date'),
    (target_day_activity.day).label('day'),
    (target_day_activity.time).label('time'),
    (target_day_activity.activity).label('activity'),
    (target_day_activity.status).label('status')
).order_by(target_day_activity.time,target_day_activity.date)