from flask import Blueprint, render_template, send_from_directory, current_app, url_for, request, redirect
from flask_login import current_user, login_required
from apps.mission import varGroup, queries
from sqlalchemy import create_engine, select, delete, and_, insert, func, or_, update
from apps.mission.forms import UploadMissionForm, Question_answer, Roll_position
from pathlib import Path
from apps.app import db, csrf
import datetime
import json
from apps.mission.models import (mission as db_mission, roleAndrule, preciousAnswer, rollPosition,
target_week_role, target_day_activity, habbit_7th)
from apps.mission.queries import (sql_base, sql_base_answer, sql_base_roll, 
question, status , sql_collect_role, sql_activity_role_week, 
sql_activity_role_daily, sql_role_mission)

engine = create_engine(varGroup.mysql_url)

# est를 블루프린트화한다.
mission = Blueprint(
    "mission",
    __name__,
    template_folder="templates",
    static_folder="static",)
week1 = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat",7:"sun"}

def run_db():
    if current_user.is_authenticated:
        sql1 = sql_base.where(db_mission.email == current_user.email)
    else:
        sql1 = sql_base.where(db_mission.email == 'nerve751105@gmail.com')

    with engine.connect() as conn:
        result = conn.execute(sql1)
    return result

def run_db_RnM():
    sql1 = sql_role_mission.where(roleAndrule.email == current_user.email)
    with engine.connect() as conn:
        result = conn.execute(sql1)
    return result

def run_db_others(receive_email):
    sql1 = sql_base.where(db_mission.email == receive_email)

    with engine.connect() as conn:
        result = conn.execute(sql1)
    return result

def run_db_RnM_others(receive_email):
    sql1 = sql_role_mission.where(roleAndrule.email == receive_email)
    with engine.connect() as conn:
        result = conn.execute(sql1)
    return result

def run_db_answer():
    sql1 = sql_base_answer.where(preciousAnswer.email == current_user.email)
    with engine.connect() as conn:
        result = conn.execute(sql1)
    return result

def run_db_ability():
    sql1 = sql_base_roll.where(rollPosition.email == current_user.email)
    with engine.connect() as conn:
        result = conn.execute(sql1)
    return result

def findWeek(offset):
    # week1 = {1:"sun", 2:"Mon", 3:"Tue", 4:"Wed", 5:"Thu", 6:"Fri", 7:"Sat"}
    sum_year = []
    sum_week = []

    date_now = datetime.datetime.now() + datetime.timedelta(days=int(offset))
    date = date_now.isocalendar()
    yearw = date[0]
    datew = date[1]
    dayw = [date[2]][0]
    w = str(yearw)+'-W'+str(date[1])

    dates = []
    weekSet = []
    for i in [0,1,2,3,4,5,6]:
        day_of_thisweek = datetime.datetime.strptime(w + '-1', '%G-W%V-%u') + datetime.timedelta(days=i)
        calSet = {'year':day_of_thisweek.year, 'week' : w, 'month':day_of_thisweek.month,'date':day_of_thisweek.day, 'day':week1[i+1]}
        weekSet.append(calSet)
        dates.append(day_of_thisweek.day)
    for j in weekSet:
        if j['year'] in sum_year:
            pass
        else:
            sum_year.append(j['year'])
    if j['week'] in sum_week:
        pass
    else:
        sum_week.append(j['week'])
    # print(dates)
    summary = [sum_year,sum_week,weekSet,dates]
    return summary

@mission.route("/week/<offset>", methods=["GET","POST"])
@login_required
def offsetdays(offset):
    form = UploadMissionForm()
    timeSet = ['com1','com2','com3','com4','com5','am07','am08','am09','am10','am11','am12','pm01','pm02','pm03','pm04','pm05','pm06','pm07','pm08','late']
    result = findWeek(offset)
    
    # 유저별로 정의된 role을 찾아온다.
    sql1 = sql_collect_role.where(roleAndrule.email == current_user.email)
    with engine.connect() as conn:
        result_role = conn.execute(sql1)
    role1 = list(result_role)
    role_f = []
    if role1 == []:
        role1 = ["공통"]
    else:
        for i in role1:
            role_f.append(i[0])
        if '공통' in role_f:
            pass
        else:
            role_f.append('공통')

    # 역할별 주단위 활동을 찾아오는 쿼리
    sql2 = sql_activity_role_week.where(and_(target_week_role.email == current_user.email,\
        target_week_role.role.in_(role_f),\
        target_week_role.week.in_(result[1])))
    # 일자별 활동을 찾아오는 쿼리
    sql3 = sql_activity_role_daily.where(and_(target_day_activity.email == current_user.email,\
        target_day_activity.week.in_(result[1])))

    # 7번째 습관을 찾아서 주단위 활동을 보내주내주는 쿼리
    sql4 = select(habbit_7th.id, habbit_7th.category, habbit_7th.activity\
    ).where(and_(habbit_7th.email == current_user.email,\
        habbit_7th.week.in_(result[1])
    ))

    with engine.connect() as conn:
        result_week = conn.execute(sql2)
        result_day = conn.execute(sql3)
        result_7th = conn.execute(sql4)

    week_act = list(result_week)
    day_act = list(result_day)
    act_7th = list(result_7th)

    # 심신을 단련하라에 해당하는 활동을 묶어서 보내는 역할
    act7th = ['신체적','정신/지적','영적','사회/감정적']
    m_7th = {}
    for i in act7th:
        l = []
        for j in act_7th:
            if i == j[1]:
                l = j
        if l == []:
            l = ['','','']
        m_7th[i] = l
    
    # 주단위 활동을 역할별로 묶어서 front로 보내주는 역할
    m = {}
    for i in role_f:
        k = 0
        l = []
        for j in week_act:
            if i == j[2]:
                k += 1
                p = list(j)
                p.append(k)
                l.append(p)
        if k < 4:
            for n in range(4-k):
                o = ['',current_user.email,i,result[0],result[1],k+n+1,'등록','',k+n+1]
                l.append(o)
        m[i] = l

    # 일자별 활동을 묶어서 front로 보내주는 역할
    for j in range(25-len(week_act)):
        week_act.append(['',current_user.email,'등록',result[0],result[1],'','','','미등록'])
    # print(result[3])
    aa_com = {}
    aa_hour = {}
    for orderi, i in enumerate(timeSet):
        aa2 = {}
        for orderj, j in enumerate(result[3]):
            aa2[j] = []
            for k in day_act:
                if k[4] == str(j) and k[6] == i:
                    aa2[j] = k
            if aa2[j] == []:
                aa2[j] = ['',current_user.email,result[0][0],result[1][0],j,week1[(orderj+1)],i,i+'(입력)','미등록']
        if orderi < 5:
            aa_com[i]=aa2
        else:
            aa_hour[i]=aa2


    return render_template("mission/index.html",form = form ,year = result[0], week = result[1],weekSet = result[2],
        week_act = m, overall = week_act, day_act_com = aa_com, day_act_hour = aa_hour ,role = role_f, act7th = m_7th, offset = offset)



# dt 애플리케이션을 사용하여 앤드 포인트를 작성한다.
@mission.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        offset = 0
        form = UploadMissionForm()
        timeSet = ['com1','com2','com3','com4','com5','am07','am08','am09','am10','am11','am12','pm01','pm02','pm03','pm04','pm05','pm06','pm07','pm08','late']
        result = findWeek(offset)
        
        # 유저별로 정의된 role을 찾아온다.
        sql1 = sql_collect_role.where(roleAndrule.email == current_user.email)
        with engine.connect() as conn:
            result_role = conn.execute(sql1)
        role1 = list(result_role)
        role_f = []
        if role1 == []:
            role1 = ["공통"]
        else:
            for i in role1:
                role_f.append(i[0])
            if '공통' in role_f:
                pass
            else:
                role_f.append('공통')

        # 역할별 주단위 활동을 찾아오는 쿼리
        sql2 = sql_activity_role_week.where(and_(target_week_role.email == current_user.email,\
            target_week_role.role.in_(role_f),\
            target_week_role.week.in_(result[1])))
        # 일자별 활동을 찾아오는 쿼리
        sql3 = sql_activity_role_daily.where(and_(target_day_activity.email == current_user.email,\
            target_day_activity.week.in_(result[1])))

        # 7번째 습관을 찾아서 주단위 활동을 보내주내주는 쿼리
        sql4 = select(habbit_7th.id, habbit_7th.category, habbit_7th.activity\
        ).where(and_(habbit_7th.email == current_user.email,\
            habbit_7th.week.in_(result[1])
        ))

        with engine.connect() as conn:
            result_week = conn.execute(sql2)
            result_day = conn.execute(sql3)
            result_7th = conn.execute(sql4)

        week_act = list(result_week)
        day_act = list(result_day)
        act_7th = list(result_7th)

        # 심신을 단련하라에 해당하는 활동을 묶어서 보내는 역할
        act7th = ['신체적','정신/지적','영적','사회/감정적']
        m_7th = {}
        for i in act7th:
            l = []
            for j in act_7th:
                if i == j[1]:
                    l = j
            if l == []:
                l = ['','','']
            m_7th[i] = l
        
        # 주단위 활동을 역할별로 묶어서 front로 보내주는 역할
        m = {}
        for i in role_f:
            k = 0
            l = []
            for j in week_act:
                if i == j[2]:
                    k += 1
                    p = list(j)
                    p.append(k)
                    l.append(p)
            if k < 4:
                for n in range(4-k):
                    o = ['',current_user.email,i,result[0],result[1],k+n+1,'등록','',k+n+1]
                    l.append(o)
            m[i] = l

        # 일자별 활동을 묶어서 front로 보내주는 역할
        for j in range(25-len(week_act)):
            week_act.append(['',current_user.email,'등록',result[0],result[1],'','','','미등록'])
        # print(result[3])
        aa_com = {}
        aa_hour = {}
        for orderi, i in enumerate(timeSet):
            aa2 = {}
            for orderj, j in enumerate(result[3]):
                aa2[j] = []
                for k in day_act:
                    if k[4] == str(j) and k[6] == i:
                        aa2[j] = k
                if aa2[j] == []:
                    aa2[j] = ['',current_user.email,result[0][0],result[1][0],j,week1[(orderj+1)],i,i+'(입력)','미등록']
            if orderi < 5:
                aa_com[i]=aa2
            else:
                aa_hour[i]=aa2


        return render_template("mission/index.html",form = form ,year = result[0], week = result[1],weekSet = result[2],
            week_act = m, overall = week_act, day_act_com = aa_com, day_act_hour = aa_hour ,role = role_f, act7th = m_7th, offset = offset)
    else:
        return render_template("mission/index2.html")

@csrf.exempt
@mission.route("/insertDailyAcivity", methods=["POST"])
def insertDay():
    input_target = request.get_json()
    # print(input_target)#['id'])
    id1 = str(input_target['id'])
    email1 = str(input_target['email'])
    year1 = input_target['year']
    week1 = input_target['week']
    date1 = input_target['date']
    day1 = input_target['day']
    time1 = input_target['time']
    activity1 = input_target['activity']
    return_Id = []
    if id1 == '':
        sql1 = insert(target_day_activity).values(email = email1, year = year1, week = week1, date = date1, day = day1, time = time1, activity = activity1)
        with engine.connect() as conn:
            result_week = conn.execute(sql1)
            conn.commit()        
        id_return = (select(target_day_activity.id, target_day_activity.activity).
        where(target_day_activity.email == email1, 
        target_day_activity.year == year1, 
        target_day_activity.week == week1, 
        target_day_activity.date == date1, 
        target_day_activity.day == day1, 
        target_day_activity.time == time1)
        )
        
        with engine.connect() as conn:
            result = conn.execute(id_return)
        if result is not None:
            for i in result:
                return_Id.append(i[0])
                return_Id.append(i[1])
        # print(return_Id)

    else:
        sql1 = update(target_day_activity).where(target_day_activity.id == id1).values(activity = activity1)
        return_Id = [id1,activity1]
        with engine.connect() as conn:
            result_week = conn.execute(sql1)
            conn.commit()
    send_file = json.dumps(return_Id,indent=4)
    return send_file


# 주차목표 입력
@mission.route("/writeweeklyaction", methods=["POST"])
def writePlan():
    if request.form['id1'] == '':
        sql1 = insert(target_week_role).values(email=request.form['email1'],
        role=request.form['selection'],
        year=request.form['year1'],
        week=request.form['week1'],
        order=request.form['order1'],
        activity=request.form['activity1'])
    else:
        sql1 = update(target_week_role).where(target_week_role.id == request.form['id1']).values(activity = request.form['activity1'])
    # print(sql1)
    with engine.connect() as conn:
        conn.execute(sql1)
        conn.commit()
    return redirect(url_for("mission.index"))

# 끊임없이 쇄신하라 부분 입력
@mission.route("/healthplan", methods=["POST"])
def healthPlan():
    # print(request.form)
    if request.form['id1'] == '':
        sql1 = insert(habbit_7th).values(email=request.form['email1'],
        year=request.form['year1'],
        week=request.form['week1'],
        category=request.form['cate1'],
        activity=request.form['activity1'])
    else:
        sql1 = update(habbit_7th).where(habbit_7th.id == request.form['id1']).values(activity = request.form['activity1'])
    # print(sql1)
    with engine.connect() as conn:
        conn.execute(sql1)
        conn.commit()
    return redirect(url_for("mission.index"))


# dt 애플리케이션을 사용하여 앤드 포인트를 작성한다.
@mission.route("/viewMySelf", methods=["GET"])
def viewMySelf():
    result = list(run_db())
    result_R = run_db_RnM()
    result_RnM = list(result_R)
    if result_RnM == []:
        result_RnM = [('role1','공통','미션이 등록되지 않았습니다.')]
    if result == []:
        user_mission = [['','미션이 등록되지 않았습니다.','역할별 미션이 등록되지 않았습니다.','부칙이 등록되지 않았습니다.']]
    else:
        user_mission = result
    return render_template("mission/viewself.html",mission = user_mission, RnM = result_RnM)

#타인의 미션 살펴보기
@mission.route("/users/<user_email>", methods=["GET"])
@login_required
def referenceOthers(user_email):
    result = list(run_db_others(user_email))
    result_R = run_db_RnM_others(user_email)
    result_RnM = list(result_R)
    email2 = user_email.split('@')
    if result_RnM == []:
        result_RnM = [('role1','공통','미션이 등록되지 않았습니다.')]
    if result == []:
        user_mission = [['','미션이 등록되지 않았습니다.','역할별 미션이 등록되지 않았습니다.','부칙이 등록되지 않았습니다.']]
    else:
        user_mission = result
    return render_template("mission/showothers.html",mission = user_mission, email = email2[0], RnM = result_RnM)


# 역할 및 역량 조회
@mission.route("/rollAndAbility", methods=["GET"])
@login_required
def rollAndAbility():
    result = run_db_ability()
    myRoll = list(result)
    if myRoll == []:
        myRoll = [['','미응답','미응답','미응답','미응답']]
    return render_template("mission/rollAndAbility.html", answer = myRoll)


# 소중한것 찾기 결과물 보기
@mission.route("/explorePrecious", methods=["GET"])
@login_required
def precious():
    result = run_db_answer()
    myPrecious = list(result)
    if myPrecious == []:
        myPrecious = [['','미응답','미응답','미응답','미응답','미응답','미응답']]
    return render_template("mission/precious.html", question = question, answer = myPrecious)


# 테스트 화면
@mission.route("/write_mission", methods=["GET","POST"])
@login_required
def writeMission():
    # form을 instance화 한다.
    form = UploadMissionForm()
    result = run_db()
    result_R = run_db_RnM()
    user_mission = list(result)
    result_RnM = list(result_R)
    # print(result_RnM)
    if user_mission == []:
        check1 = 0
        name_button = '등록'
        user_mission = ['','','']
    else:
        check1 = 1
        name_button = '수정'
        if request.method == 'GET':
            form.mission_statement.data = user_mission[0][1]
            form.roll_statement.data = user_mission[0][2]
            form.extra_statement.data = user_mission[0][3]

    if result_RnM == []:
        max_r = 1
        result_RnM2 = [('role1','공통','')]
    else:
        chech_r = []
        for r in result_RnM:
            chech_r.append(int(r[0][4]))
        max_r = max(chech_r)
        result_RnM2 = result_RnM



    # form이 제대로 작성되었는지 체크
    if form.validate_on_submit():
        statement = db_mission(
            email = current_user.email,
            statement = form.mission_statement.data,
            # acts_principal = form.roll_statement.data,
            acts_subprincipal = form.extra_statement.data,
        )
        data_obj = json.loads(request.form['roleTotal'])
        # print(data_obj, type(data_obj))
        if check1 == 0:
            db.session.add(statement)
        else:
            user = db.session.query(db_mission).filter_by(email=current_user.email).first()
            user.statement = form.mission_statement.data
            # user.acts_principal = form.roll_statement.data
            user.acts_subprincipal = form.extra_statement.data
            db.session.add(user)
        db.session.commit()
        # 지워진 RNR 지우는 작업하는 부분
        for r2 in result_RnM:
            try:
                print(data_obj[r2[0]])
            except:
                mission_role= db.session.query(roleAndrule).filter_by(email=current_user.email).filter_by(role=r2[0]).delete()
                db.session.commit()
                
        # 받아온 RNR 업데이트 하는 부분
        for do in data_obj:
            new_obj = True
                # 지워진 RNR 지우는 작업하는 부분
            for r2 in result_RnM:
                if do == r2[0]:
                    # print(do, r2[0])
                    new_obj = False
                    # 여기서 업데이트 함  
                    mission_role= db.session.query(roleAndrule).filter_by(email=current_user.email).filter_by(role=do).first()
                    mission_role.role_name = data_obj[do][0]
                    mission_role.principal = data_obj[do][1]
                    db.session.add(mission_role)
                    db.session.commit()
                    break
            if new_obj:
                # 여기서 신규추가
                mission_role = roleAndrule(
                    email = current_user.email,
                    role = do,
                    role_name = data_obj[do][0],
                    principal = data_obj[do][1]
                )
                db.session.add(mission_role)
                db.session.commit()

        return redirect(url_for("mission.writeMission"))
    return render_template("mission/write_mission.html",
        form = form, nbutton = name_button, max_r = max_r, RnM = result_RnM2)

# # mission statement를 입력하는 화면
# @mission.route("/write_mission", methods=["GET","POST"])
# @login_required
# def writeMission():
#     # form을 instance화 한다.
#     form = UploadMissionForm()
#     result = run_db()
#     user_mission = list(result)
#     if user_mission == []:
#         check1 = 0
#         name_button = '등록'
#         user_mission = ['','','']
#     else:
#         check1 = 1
#         name_button = '수정'
#         if request.method == 'GET':
#             form.mission_statement.data = user_mission[0][1]
#             form.roll_statement.data = user_mission[0][2]
#             form.extra_statement.data = user_mission[0][3]


#     # form이 제대로 작성되었는지 체크
#     if form.validate_on_submit():
#         statement = db_mission(
#             email = current_user.email,
#             statement = form.mission_statement.data,
#             acts_principal = form.roll_statement.data,
#             acts_subprincipal = form.extra_statement.data,
#         )
#         print(form.mission_statement.data)
#         if check1 == 0:
#             db.session.add(statement)
#         else:
#             user = db.session.query(db_mission).filter_by(email=current_user.email).first()
#             user.statement = form.mission_statement.data
#             user.acts_principal = form.roll_statement.data
#             user.acts_subprincipal = form.extra_statement.data
#             db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("mission.index"))
#     return render_template("mission/write_mission.html",form = form, nbutton = name_button)

# 소중한 것 찾기를 위한 질의 응답시간
@mission.route("/findPrecious", methods=["GET","POST"])
@login_required
def findprecious():
    # form을 instance화 한다.
    form = Question_answer()
    result = run_db_answer()
    user_precious = list(result)
    if user_precious == []:
        check1 = 0
        name_button = '등록'
        user_precious = ['','','','','','']
    else:
        check1 = 1
        name_button = '수정'
        if request.method == 'GET':
            form.NO1.data = user_precious[0][1]
            form.NO2.data = user_precious[0][2]
            form.NO3.data = user_precious[0][3]
            form.NO4.data = user_precious[0][4]
            form.NO5.data = user_precious[0][5]
            form.NO6.data = user_precious[0][6]

    # form이 제대로 작성되었는지 체크
    if form.validate_on_submit():
        answer1 = db.session.query(preciousAnswer).filter_by(email=current_user.email).first()
        # print(answer1,"여깁니다.")
        statement = preciousAnswer(
            email = current_user.email,
            answer_no1 = form.NO1.data,
            answer_no2 = form.NO2.data,
            answer_no3 = form.NO3.data,
            answer_no4 = form.NO4.data,
            answer_no5 = form.NO5.data,
            answer_no6 = form.NO6.data,           
        )
        if answer1 is None:
            db.session.add(statement)
        else:
            answer1.answer_no1 = form.NO1.data
            answer1.answer_no2 = form.NO2.data
            answer1.answer_no3 = form.NO3.data
            answer1.answer_no4 = form.NO4.data
            answer1.answer_no5 = form.NO5.data
            answer1.answer_no6 = form.NO6.data
            db.session.add(answer1)
        db.session.commit()
        return redirect(url_for("mission.precious"))
    return render_template("mission/answer_question.html",form = form, nbutton = name_button, question = question)

# 역할 정의, 역량 정의
@mission.route("/defineRoll", methods=["GET","POST"])
@login_required
def defineRollAndAbility():
    # form을 instance화 한다.
    form = Roll_position()
    result = run_db_ability()
    user_ability = list(result)
    if user_ability == []:
        check1 = 0
        name_button = '등록'
        user_ability = ['','','','','']
    else:
        check1 = 1
        name_button = '수정'
        if request.method == 'GET':
            form.roll.data = user_ability[0][1]
            form.area_avility.data = user_ability[0][2]
            form.area_concern.data = user_ability[0][3]
            form.area_weakness.data = user_ability[0][4]

    # form이 제대로 작성되었는지 체크
    if form.validate_on_submit():
        answer1 = db.session.query(rollPosition).filter_by(email=current_user.email).first()
        # print(answer1,"여깁니다.")
        statement = rollPosition(
            email = current_user.email,
            roll = form.roll.data,
            area_avility = form.area_avility.data,
            area_concern = form.area_concern.data,
            area_weakness = form.area_weakness.data,         
        )
        if answer1 is None:
            db.session.add(statement)
        else:
            answer1.roll = form.roll.data
            answer1.area_avility = form.area_avility.data
            answer1.area_concern = form.area_concern.data
            answer1.area_weakness = form.area_weakness.data
            db.session.add(answer1)
        db.session.commit()
        return redirect(url_for("mission.rollAndAbility"))
    return render_template("mission/rollAndAbility_input.html",form = form, nbutton = name_button, question = question)

# daily actvity를 DB에 입력한다.


