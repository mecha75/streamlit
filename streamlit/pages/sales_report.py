import streamlit as st
import pandas as pd
import numpy as np
from flask_migrate import Migrate
from sqlalchemy import create_engine, select, delete, and_, insert, func, update, or_
from datetime import datetime
from models import salesRecord, salesGroupMaster, exRate, mysql_url
from queries import sql_lv1, sql_lv2, sql_lv3,sql_plan_lv1, sql_plan_lv2, sql_plan_lv3
import module_pdf as mp
master_date = {
'fromMonth':'01',
'toMonth':'07',
'beforeMonth':'06',
'thisYear':'2024',
'preYear':'2023'
}

with st.expander('기준월변경'):
    with st.form('Set a date'):
        option_year = st.selectbox(
            '당해년도?',(
                '2024'
            )
        )
        option_startMonth = st.selectbox(
            '비교시작월?',(
                '01','02','03','04','05','06','07','08','09','10','11','12'
            )
        )
        option_month = st.selectbox(
            '현재월?',(
                '01','02','03','04','05','06','07','08','09','10','11','12'
            )
        )
        option_preMonth = st.selectbox(
            '이전월?',(
                '01','02','03','04','05','06','07','08','09','10','11','12'
            )
        )
        submitted  = st.form_submit_button("기준월 수정")
        if submitted:
            st.cache_data.clear()
            master_date['thisYear'] = option_year
            master_date['fromMonth'] = option_startMonth
            master_date['toMonth'] = option_month
            master_date['beforeMonth'] = option_preMonth
            master_date['preYear'] = str(int(option_year)-1)
    # if st.button("Clear cache data!"):
    # # Clear values from *all* all in-memory and on-disk data caches:
    # # i.e. clear values from both square and cube
    #     st.cache_data.clear()

engine = create_engine(mysql_url)
# thisYear = str(datetime.today().year)
# thisYear_preMonth = str(datetime.today().year)
# previousYear = str(datetime.today().year-1)
# baseMonth = datetime.today().month
# if baseMonth < 10:   
#     toMonth = '0'+str(datetime.today().month-1)
#     beforeMonth = '0'+str(datetime.today().month-2)
#     if baseMonth == 1:
#         toMonth = '12'
#         beforeMonth = '11'
#         thisYear = str(datetime.today().year-1)
#         thisYear_preMonth = str(datetime.today().year-1)
#         previousYear = str(datetime.today().year-2)
#     elif baseMonth == 2:
#         toMonth = '1'
#         beforeMonth = '12'
#         thisYear = str(datetime.today().year)
#         thisYear_preMonth = str(datetime.today().year-1)
#         previousYear = str(datetime.today().year-1)
# else:
#     toMonth = str(datetime.today().month-1)
#     beforeMonth = str(datetime.today().month-2)
#     thisYear = str(datetime.today().year)

fromMonth = master_date['fromMonth']
toMonth = master_date['toMonth']
beforeMonth = master_date['beforeMonth']
thisYear = master_date['thisYear']
previousYear = master_date['preYear']
noResult = ['계획이 입력되지 않았습니다.','계획이 입력되지 않았습니다.','계획이 입력되지 않았습니다.']
noResult_pre = ['전년동기 실적이 없습니다.','전년동기 실적이 없습니다.','전년동기 실적이 없습니다.']

# st.write(master_date)

@st.cache_data
def call_lv1(chk_year, ver):
    with engine.connect() as con:
        result = con.execute(sql_lv1.where(and_(salesRecord.year == chk_year,salesRecord.version == ver,salesRecord.mm<=toMonth,
                                                or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    test = list(df)
    if test != []:  
        index = ['lv1Code','lv1Name']
        index_condense = ['lv1Name']
        pdf1_pre_list = mp.change_df(df, index, index_condense)
    else:
        pdf1_pre_list = noResult_pre
    return pdf1_pre_list

@st.cache_data
def call_plan_lv1(chk_year, ver):
    with engine.connect() as con:
        result = con.execute(sql_plan_lv1.where(and_(salesRecord.year == chk_year,salesRecord.version == ver, salesRecord.mm<=toMonth,
                                                    or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    test = list(df)
    if test != []:    
        index = ['lv1Code','lv1Name']
        index_condense = ['lv1Name']
        pdf1_plan_list = mp.change_df(df, index, index_condense)
    else:
        pdf1_plan_list = noResult
    return pdf1_plan_list

@st.cache_data
def call_lv2(chk_year, ver):
    with engine.connect() as con:
        result = con.execute(sql_lv2.where(and_(salesRecord.year == chk_year,salesRecord.version == ver, salesRecord.mm<=toMonth,
                                                or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    test = list(df)
    if test != []:  
        index = ['lv1Code','lv1Name','lv2Code','lv2Name']
        index_condense = ['lv2Name']
        pdf1_pre_list = mp.change_df(df, index, index_condense)
    else:
        pdf1_pre_list = noResult_pre
    return pdf1_pre_list

@st.cache_data
def call_plan_lv2(chk_year, ver):
    with engine.connect() as con:
        result = con.execute(sql_plan_lv2.where(and_(salesRecord.year == chk_year,salesRecord.version == ver, salesRecord.mm<=toMonth,
                                                    or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    test = list(df)
    if test != []:    
        index = ['lv1Code','lv1Name','lv2Code','lv2Name']
        index_condense = ['lv2Name']
        pdf1_plan_list = mp.change_df(df, index, index_condense)
    else:
        pdf1_plan_list = noResult
    return pdf1_plan_list


@st.cache_data
def call_lv3(chk_year, ver):
    with engine.connect() as con:
        result = con.execute(sql_lv3.where(and_(salesRecord.year == chk_year,salesRecord.version == ver, salesRecord.mm<=toMonth,
                                                or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    test = list(df)
    if test != []:  
        index = ['lv1Code','lv1Name','lv2Code','lv2Name','lv3Code','lv3Name']
        index_condense = ['lv3Name']
        pdf1_pre_list = mp.change_df(df, index, index_condense)
    else:
        pdf1_pre_list = noResult_pre
    return pdf1_pre_list

@st.cache_data
def call_plan_lv3(chk_year, ver):
    with engine.connect() as con:
        result = con.execute(sql_plan_lv3.where(and_(salesRecord.year == chk_year,salesRecord.version == ver, salesRecord.mm<=toMonth,
                                                    or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    test = list(df)
    if test != []:    
        index = ['lv1Code','lv1Name','lv2Code','lv2Name','lv3Code','lv3Name']
        index_condense = ['lv3Name']
        pdf1_plan_list = mp.change_df(df, index, index_condense)
    else:
        pdf1_plan_list = noResult
    return pdf1_plan_list


pdf1_list = call_lv1(thisYear,'(A)')
pdf1_pre_list = call_lv1(previousYear,'(A)')
pdf1_plan_list = call_plan_lv1(thisYear,'(P)')
df_lv1 = mp.overview_sales(pdf1_pre_list, pdf1_plan_list, pdf1_list, toMonth, beforeMonth)

# st.write(pdf1_plan_list[0])

pdf1_list = call_lv2(thisYear,'(A)')
pdf1_pre_list = call_lv2(previousYear,'(A)')
pdf1_plan_list = call_plan_lv2(thisYear,'(P)')
df_lv2 = mp.overview_sales(pdf1_pre_list, pdf1_plan_list, pdf1_list, toMonth, beforeMonth)

pdf1_list = call_lv3(thisYear,'(A)')
pdf1_pre_list = call_lv3(previousYear,'(A)')
pdf1_plan_list = call_plan_lv3(thisYear,'(P)')
df_lv3 = mp.overview_sales(pdf1_pre_list, pdf1_plan_list, pdf1_list, toMonth, beforeMonth)



st.header(f'{toMonth}월 판매실적\:Report')

tab1, tab2, tab3 = st.tabs(["대분류", "본부레벨",  "임원레벨"])
with tab1:
    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 매출액 (단위:백만원)')
            st.write(df_lv1[0][0])
        with col2:
            st.write(f'▶{toMonth}월누계 매출액 (단위:백만원)')
            st.write(df_lv1[0][1])

    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 판매수량 (단위:천본)')
            st.write(df_lv1[1][0])
        with col2:
            st.write(f'▶{toMonth}월누계 판매수량 (단위:천본)')
            st.write(df_lv1[1][1])

    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 판매단가 (단위:원/kg)')
            st.write(df_lv1[2][0].round(0))
        with col2:
            st.write(f'▶{toMonth}월누계 판매단가 (단위:원/kg)')
            st.write(df_lv1[2][1].round(0))
 
with tab2:
    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 매출액 (단위:백만원)')
            st.write(df_lv2[0][0])
        with col2:
            st.write(f'▶{toMonth}월누계 매출액 (단위:백만원)')
            st.write(df_lv2[0][1])

    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 판매수량 (단위:천본)')
            st.write(df_lv2[1][0])
        with col2:
            st.write(f'▶{toMonth}월누계 판매수량 (단위:천본)')
            st.write(df_lv2[1][1])

    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 판매단가 (단위:원/kg)')
            st.write(df_lv2[2][0].round(0))
        with col2:
            st.write(f'▶{toMonth}월누계 판매단가 (단위:원/kg)')
            st.write(df_lv2[2][1].round(0))


with tab3:
    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 매출액 (단위:백만원)')
            st.write(df_lv3[0][0])
        with col2:
            st.write(f'▶{toMonth}월누계 매출액 (단위:백만원)')
            st.write(df_lv3[0][1])

    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 판매수량 (단위:천본)')
            st.write(df_lv3[1][0])
        with col2:
            st.write(f'▶{toMonth}월누계 판매수량 (단위:천본)')
            st.write(df_lv3[1][1])

    with st.container(border=1):
        col1, col2= st.columns([1,1])
        with col1:
            st.write(f'▶{toMonth}월 판매단가 (단위:원/kg)')
            st.write(df_lv3[2][0].round(0))
        with col2:
            st.write(f'▶{toMonth}월누계 판매단가 (단위:원/kg)')
            st.write(df_lv3[2][1].round(0))


