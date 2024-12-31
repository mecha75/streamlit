import streamlit as st
import pandas as pd
import numpy as np
from flask_migrate import Migrate
from sqlalchemy import create_engine, select, delete, and_, insert, func, update, or_
from datetime import datetime
from models import salesRecord, salesGroupMaster, exRate, mysql_url
from queries import sql_lv2_RIM, sql_RIM
import module_pdf as mp
import matplotlib.pyplot as plt

engine = create_engine(mysql_url)

with engine.connect() as con:
    result = con.execute(sql_lv2_RIM.where(
        and_(salesRecord.year == '2024',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'),
                                            or_(salesRecord.ProdGrpName == 'TBR',salesRecord.ProdGrpName == 'TBR(S)'))))
df = pd.DataFrame(result)
index = ['lv1Code','lv1Name','lv2Code','lv2Name','RIM']
index_condense = ['lv2Name','RIM']
pdf_pcr_list = mp.change_df(df, index, index_condense)

with engine.connect() as con:
    result = con.execute(sql_lv2_RIM.where(
        and_(salesRecord.year == '2024',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'),
                                            or_(salesRecord.ProdGrpName == 'TBR',salesRecord.ProdGrpName == 'TBR(S)'))))
df = pd.DataFrame(result)
index = ['RIM']
index_condense = ['RIM']
pdf_all_list = mp.change_df(df, index, index_condense)

st.header('인치별단가(PC/LT)')
# height=500,
with st.container(border=1):
    st.bar_chart(pdf_all_list[2]['총계'].round(0))

lv2_list = ['한국RE','북미','유럽','GEM','OE','중국본부']

# with st.expander("수량보기(천본)"):
for i in lv2_list:
    with st.expander(f'{i} 인치별 상세보기 (원/kg)'):
        st.bar_chart(pdf_pcr_list[2].loc[i]['총계'].round(0))
