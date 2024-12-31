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
                                            or_(salesRecord.ProdGrpName == 'PCR',salesRecord.ProdGrpName == 'LTR'))))
df = pd.DataFrame(result)
index = ['lv1Code','lv1Name','lv2Code','lv2Name','RIM']
index_condense = ['lv2Name','RIM']
pdf_pcr_list = mp.change_df(df, index, index_condense)

with engine.connect() as con:
    result = con.execute(sql_lv2_RIM.where(
        and_(salesRecord.year == '2024',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'),
                                            or_(salesRecord.ProdGrpName == 'PCR',salesRecord.ProdGrpName == 'LTR'))))
df = pd.DataFrame(result)
index = ['RIM']
index_condense = ['RIM']
pdf_all_list = mp.change_df(df, index, index_condense)

st.header('인치별단가(PC/LT)')
# height=500,
with st.container(border=1):
    st.bar_chart(pdf_all_list[2]['총계'].round(0))
    # x_labels = list(pdf_all_list[2]['총계'].index)
    # x_labels[len(x_labels)-1] = 'Ave.'
    # values = list(pdf_all_list[2]['총계'].round(0))
    # x = np.arange(len(values))
    # # st.write(x_labels)
    # plt.bar(x,values)
    # plt.xticks(x, x_labels)
    # plt.yticks([],[])
    # font3 = {'family': 'Arial',
    #   'color':  'forestgreen',
    #   'style': 'italic',
    #   'size': 9}
    # for i in range(len(values)):
    #     plt.text(i-0.4, int(values[i])+100, int(values[i]), fontdict=font3)
    # st.pyplot(plt)



lv2_list = ['한국RE','북미','유럽','GEM','OE','중국본부']

# with st.expander("수량보기(천본)"):
for i in lv2_list:
    with st.expander(f'{i} 인치별 상세보기 (원/kg)'):
        st.bar_chart(pdf_pcr_list[2].loc[i]['총계'].round(0))
