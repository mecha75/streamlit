import streamlit as st
import pandas as pd
import numpy as np
from flask_migrate import Migrate
from sqlalchemy import create_engine, select, delete, and_, insert, func, update, or_
from datetime import datetime
from models import salesRecord, salesGroupMaster, exRate, mysql_url
from queries import sql_lv1, sql_lv2, sql_lv3
import module_pdf as mp

engine = create_engine(mysql_url)

with engine.connect() as con:
    result = con.execute(sql_lv1.where(and_(salesRecord.year == '2024',salesRecord.version == '(A)',
                                            or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
df = pd.DataFrame(result)
index = ['lv1Code','lv1Name']
index_condense = ['lv1Name']
pdf1_list = mp.change_df(df, index, index_condense)


with engine.connect() as con:
    result = con.execute(sql_lv2.where(and_(salesRecord.year == '2024',salesRecord.version == '(A)',
                                            or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
df = pd.DataFrame(result)
index = ['lv1Code','lv1Name','lv2Code','lv2Name']
# index_condense = ['lv1Name','lv2Name']
index_condense = ['lv2Name']
pdf1_list2 = mp.change_df(df, index, index_condense)

with engine.connect() as con:
    result = con.execute(sql_lv3.where(and_(salesRecord.year == '2024',salesRecord.version == '(A)',
                                            or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
df = pd.DataFrame(result)
index = ['lv1Code','lv1Name','lv2Code','lv2Name','lv3Code','lv3Name']
# index_condense = ['lv1Name','lv2Name','lv3Name']
index_condense = ['lv3Name']
pdf1_list3 = mp.change_df(df, index, index_condense)

st.header('판매실적\:overview')

with st.container(border=1):
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=1):
            st.write('▶ 매출액 (단위:백만원)')
            st.bar_chart(pdf1_list[0].iloc[-1:,0:-1].reset_index(drop=True).T)
    with col2:
        with st.container(border=1):
            st.write('▶ 판매수량 (단위:천본)')
            st.bar_chart(pdf1_list[1].iloc[-1:,0:-1].reset_index(drop=True).T)
    with col3:
        with st.container(border=1):
            st.write('▶ 판매단가 (단위:원/KG)')
            st.line_chart(pdf1_list[2].iloc[-1:,0:-1].reset_index(drop=True).T)

tab1, tab2, tab3 = st.tabs(["임원레벨", "본부레벨", "대분류"])
with tab1:
    with st.container(border=1):
        st.write("1.매출액(단위:백만원)")
        st.write(pdf1_list3[0])
        with st.expander("수량, 원단위 보기"):
            st.write("2.판매수량(단위:천본)")
            st.write(pdf1_list3[1].round(0))
            st.write("3.원단위매출액(단위:원/KG)")
            st.write(pdf1_list3[2].round(0))

with tab2:
    with st.container(border=1):
        st.write("1.매출액(단위:백만원)")
        st.write(pdf1_list2[0])
        with st.expander("수량, 원단위 보기"):
            st.write("2.판매수량(단위:천본)")
            st.write(pdf1_list2[1])
            st.write("3.원단위매출액(단위:원/KG)")
            st.write(pdf1_list2[2].round(0))


with tab3:
    with st.container(border=1):
        st.write("1.대분류판매실적(단위:백만원)")
        st.write(pdf1_list[0])
        with st.expander("수량, 원단위 보기"):
            st.write("2.대분류판매실적(단위:천본)")
            st.write(pdf1_list[1].round(0))
            st.write("3.원단위매출액(단위:원/KG)")
            st.write(pdf1_list[2].round(0))

