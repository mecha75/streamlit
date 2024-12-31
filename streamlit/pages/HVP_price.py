import streamlit as st
import pandas as pd
import numpy as np
from flask_migrate import Migrate
from sqlalchemy import create_engine, select, delete, and_, insert, func, update, or_
from datetime import datetime
from models import salesRecord, salesGroupMaster, exRate, mysql_url
from queries import sql_lv1_HVP,sql_lv2_HVP,sql_lv3_HVP
import module_pdf as mp
# import matplotlib as mpl
import matplotlib.pyplot as plt

engine = create_engine(mysql_url)

@st.cache_data
# 대 그룹 레벨
def call_hvp_lv1():
    with engine.connect() as con:
        result = con.execute(sql_lv1_HVP.where(and_(salesRecord.year == '2024',salesRecord.HVP=='HVP',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    index = ['lv1Code','lv1Name']
    index_condense = ['lv1Name']
    pdf1_list = mp.change_df(df, index, index_condense)
    return pdf1_list

@st.cache_data
def call_non_lv1():
    with engine.connect() as con:
        result = con.execute(sql_lv1_HVP.where(and_(salesRecord.year == '2024',salesRecord.HVP=='NON-HVP',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    index = ['lv1Code','lv1Name']
    index_condense = ['lv1Name']
    pdf2_list = mp.change_df(df, index, index_condense)
    return pdf2_list


@st.cache_data
def call_hvp_lv2():
    # 본부레벨
    with engine.connect() as con:
        result = con.execute(sql_lv2_HVP.where(and_(salesRecord.year == '2024',salesRecord.HVP=='HVP',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    index = ['lv1Code','lv1Name','lv2Code','lv2Name']
    index_condense = ['lv2Name']
    pdf2_1_list = mp.change_df(df, index, index_condense)
    return pdf2_1_list

@st.cache_data
def call_non_lv2():
    with engine.connect() as con:
        result = con.execute(sql_lv2_HVP.where(and_(salesRecord.year == '2024',salesRecord.HVP=='NON-HVP',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    index = ['lv1Code','lv1Name','lv2Code','lv2Name']
    index_condense = ['lv2Name']
    pdf2_2_list = mp.change_df(df, index, index_condense)
    return pdf2_2_list

@st.cache_data
def call_hvp_lv3():
    # 조직레벨
    with engine.connect() as con:
        result = con.execute(sql_lv3_HVP.where(and_(salesRecord.year == '2024',salesRecord.HVP=='HVP',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    index = ['lv1Code','lv1Name','lv2Code','lv2Name','lv3Code','lv3Name']
    index_condense = ['lv3Name']
    pdf3_1_list = mp.change_df(df, index, index_condense)
    return pdf3_1_list

@st.cache_data
def call_non_lv3():
    with engine.connect() as con:
        result = con.execute(sql_lv3_HVP.where(and_(salesRecord.year == '2024',salesRecord.HVP=='NON-HVP',or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    index = ['lv1Code','lv1Name','lv2Code','lv2Name','lv3Code','lv3Name']
    index_condense = ['lv3Name']
    pdf3_2_list = mp.change_df(df, index, index_condense)
    return pdf3_2_list

def mod_graph2(graph2):
    graph_f = graph2.loc[['북미','유럽']].T.round(1)
    labels = ['N-America','Europe']
    list_label = list(graph_f['북미'])
    list_label2 = list(graph_f['유럽'])
    list(graph_f.index)
    fig2 = plt.figure()
    plt.plot(list_label,'b--',marker='o', label=labels[0])
    plt.plot(list_label2,'r--',marker='o', label=labels[1])
    plt.legend()
    plt.ylim([15,40])
    for i in range(len(list_label)):
        plt.text(i-0.2, int(list_label[i])+1.5, str(list_label[i])+'%')
        plt.text(i-0.2, int(list_label2[i])+1.5, str(list_label2[i])+'%')
    return fig2

def mod_graph1(graph3,region,labels,min_max):
    pdf3_rate = (pdf3_1_list[1]/pdf3_2_list[1]*100)
    graph3 = pdf3_rate.reset_index().drop(columns=['lv1Name','lv2Name','총계'],errors='ignore').set_index(keys=['lv3Name'], drop=True)
    graph_f = graph3.loc[region].T.round(1)
    list(graph_f.index)
    fig1 = plt.figure()
    # colors = ['r--','g--','b--','','','']
    for i in range(len(region)):
        pass
    plt.plot(graph_f,'--',marker='o', label=labels)
    plt.legend()
    plt.ylim(min_max)
    for j in range(len(region)):
        list_label = list(graph_f[region[j]])
        for i in range(len(list_label)):
            plt.text(i-0.2, int(list_label[i])+1.5, str(list_label[i])+'%')
    return fig1

pdf1_list = call_hvp_lv1()
pdf2_list = call_non_lv1()
pdf2_1_list = call_hvp_lv2()
pdf2_2_list = call_non_lv2()
pdf3_1_list = call_hvp_lv3()
pdf3_2_list = call_non_lv3()
pdf2_rate = (pdf2_1_list[2]/pdf2_2_list[2]*100)
graph2 = pdf2_rate.reset_index().drop(columns=['lv1Name','총계'],errors='ignore').set_index(keys=['lv2Name'], drop=True)
pdf3_rate = (pdf3_1_list[2]/pdf3_2_list[2]*100)
graph3 = pdf3_rate.reset_index().drop(columns=['lv1Name','lv2Name','총계'],errors='ignore').set_index(keys=['lv3Name'], drop=True)
group_list = [['서울경기지역','영남지역','충호남지역'],['KUSA','CANADA','중남미'],['독일','KH-U.K.','FRANCE'],['한국OE','북미OE','유럽OE','기타OE'],['중국OE','중국RE']]

rate_hvp = pdf3_1_list[2].reset_index().loc[:,['lv3Name','총계']].set_index(keys=['lv3Name'],drop=True).T.round(0)
rate_nonHvp = pdf3_2_list[2].reset_index().loc[:,['lv3Name','총계']].set_index(keys=['lv3Name'],drop=True).T.round(0)

st.header('HVP 단가 현황 HVP vs. nonHVP (원/Kg)')
li1 = []
for i in range(len(group_list)):
    li2 = {}
    col_m = st.columns(len(group_list[i]))
    for j, col_n in enumerate(col_m):
        with col_n:
            li2['지역'] = group_list[i][j]
            li2['rate_hvp'] = list(rate_hvp[li2['지역']])[0]
            li2['rate_non'] = list(rate_nonHvp[li2['지역']])[0]
            li2['percent'] = '+' + str(round((int(li2['rate_hvp'])/int(li2['rate_non'])-1)*100,1)) + '%'
            li2['series'] = {'HVP':li2['rate_hvp'], 'non':li2['rate_non']}
            with st.container(border=1):
                st.write(li2['지역'])
                st.write('HVP :',li2['rate_hvp'],', 일반 :',li2['rate_non'],',',li2['percent'])
                st.bar_chart(li2['series'])
            li1.append(li2)
            li2 = {}

tab1, tab2, tab3 = st.tabs(["임원레벨", "본부레벨", "대분류"])
with tab1:
    with st.container(border=1):
        st.write("1.HVP단가율(vs Non-HVP):임원레벨")
        st.write(pdf3_rate.round(1).astype('str')+'%')

        with st.expander("단가보기(원/Kg)"):
            
            col1, col2 = st.columns(2)

            with col1:
                with st.container(border=1):
                    st.write('▶HVP')
                    st.write(pdf3_1_list[2].round(0))
            
            with col2:
                with st.container(border=1):
                    st.write('▶Non-HVP')
                    st.write(pdf3_2_list[2].round(0))

with tab2:
    with st.container(border=1):
        st.write("2.HVP단가율(vs Non-HVP):본부레벨")
        st.write(pdf2_rate.round(1).astype('str')+'%')
        with st.expander("수량보기(천본)"):
            
            col1, col2 = st.columns(2)

            with col1:
                with st.container(border=1):
                    st.write('▶HVP')
                    st.write(pdf2_1_list[2].round(0))
            
            with col2:
                with st.container(border=1):
                    st.write('▶Non-HVP')
                    st.write(pdf2_2_list[2].round(0))

with tab3:
    with st.container(border=1):
        st.write("3.HVP단가율(vs Non-HVP):대분류")
        st.write((pdf1_list[2]/pdf2_list[2]*100).round(1).astype('str')+'%')
        with st.expander("수량보기(천본)"):
            
            col1, col2 = st.columns(2)

            with col1:
                with st.container(border=1):
                    st.write('▶HVP')
                    st.write(pdf1_list[2].round(0))
            
            with col2:
                with st.container(border=1):
                    st.write('▶Non-HVP')
                    st.write(pdf2_list[2].round(0))

        



