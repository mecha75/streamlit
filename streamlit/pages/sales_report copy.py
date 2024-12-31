import streamlit as st
import pandas as pd
import numpy as np
from flask_migrate import Migrate
from sqlalchemy import create_engine, select, delete, and_, insert, func, update, or_
from datetime import datetime
from models import salesRecord, salesGroupMaster, exRate, mysql_url
from queries import sql_lv1, sql_lv2, sql_lv3,sql_plan_lv1, sql_plan_lv2, sql_plan_lv3
import module_pdf as mp

engine = create_engine(mysql_url)
thisYear = '2024'
# str(datetime.today().year)
previousYear = '2023'
fromMonth = '01'
toMonth = '06'
noResult = ['계획이 입력되지 않았습니다.','계획이 입력되지 않았습니다.','계획이 입력되지 않았습니다.']
noResult_pre = ['전년동기 실적이 없습니다.','전년동기 실적이 없습니다.','전년동기 실적이 없습니다.']

# 당해년도 실적 추출해서 Pivot table 구성


# with engine.connect() as con:
#     result = con.execute(sql_lv2.where(and_(salesRecord.year == thisYear,salesRecord.version == '(A)',
#                                             or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
# df = pd.DataFrame(result)
# index = ['lv1Code','lv1Name','lv2Code','lv2Name']
# # index_condense = ['lv1Name','lv2Name']
# index_condense = ['lv2Name']
# pdf1_list2 = mp.change_df(df, index, index_condense)

# with engine.connect() as con:
#     result = con.execute(sql_lv3.where(and_(salesRecord.year == thisYear,salesRecord.version == '(A)',
#                                             or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
# df = pd.DataFrame(result)
# index = ['lv1Code','lv1Name','lv2Code','lv2Name','lv3Code','lv3Name']
# # index_condense = ['lv1Name','lv2Name','lv3Name']
# index_condense = ['lv3Name']
# pdf1_list3 = mp.change_df(df, index, index_condense)

# 전년도실적

# with engine.connect() as con:
#     result = con.execute(sql_lv2.where(and_(salesRecord.year == previousYear,salesRecord.version == '(A)',
#                                             or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
# df = pd.DataFrame(result)
# test = list(df)
# if test != []:      
#     index = ['lv1Code','lv1Name','lv2Code','lv2Name']
#     # index_condense = ['lv1Name','lv2Name']
#     index_condense = ['lv2Name']
#     pdf1_pre_list2 = mp.change_df(df, index, index_condense)
# else:
#     pdf1_pre_list2 = noResult_pre

# with engine.connect() as con:
#     result = con.execute(sql_lv3.where(and_(salesRecord.year == previousYear,salesRecord.version == '(A)',
#                                             or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
# df = pd.DataFrame(result)
# test = list(df)
# if test != []:
#     # st.write(df)      
#     index = ['lv1Code','lv1Name','lv2Code','lv2Name','lv3Code','lv3Name']
#     # index_condense = ['lv1Name','lv2Name','lv3Name']
#     index_condense = ['lv3Name']
#     pdf1_pre_list3 = mp.change_df(df, index, index_condense)
# else:
#     pdf1_pre_list3 = noResult_pre

# 당해년도 계획 추출





# with engine.connect() as con:
#     result = con.execute(sql_plan_lv2.where(and_(salesRecord.year == thisYear,salesRecord.version == '(P)',
#                                             or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
# df = pd.DataFrame(result)
# test = list(df)
# if test != []:    
#     index = ['lv1Code','lv1Name','lv2Code','lv2Name']
#     # index_condense = ['lv1Name','lv2Name']
#     index_condense = ['lv2Name']
#     pdf1_plan_list2 = mp.change_df(df, index, index_condense)
# else:
#     pdf1_plan_list2 = noResult

# with engine.connect() as con:
#     result = con.execute(sql_plan_lv3.where(and_(salesRecord.year == thisYear,salesRecord.version == '(P)',
#                                             or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
# df = pd.DataFrame(result)
# test = list(df)
# if test != []:    
#     index = ['lv1Code','lv1Name','lv2Code','lv2Name','lv3Code','lv3Name']
#     # index_condense = ['lv1Name','lv2Name','lv3Name']
#     index_condense = ['lv3Name']
#     pdf1_plan_list3 = mp.change_df(df, index, index_condense)
# else:
#     pdf1_plan_list3 = noResult

@st.cache_data
def call_this_lv1():
    with engine.connect() as con:
        result = con.execute(sql_lv1.where(and_(salesRecord.year == thisYear,salesRecord.version == '(A)',
                                                or_(salesRecord.DistributeChannel=='10',salesRecord.DistributeChannel=='20'))))
    df = pd.DataFrame(result)
    index = ['lv1Code','lv1Name']
    index_condense = ['lv1Name']
    pdf1_list = mp.change_df(df, index, index_condense)
    return pdf1_list

@st.cache_data
def call_pre_lv1():
    with engine.connect() as con:
        result = con.execute(sql_lv1.where(and_(salesRecord.year == previousYear,salesRecord.version == '(A)',
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
def call_plan_lv1():
    with engine.connect() as con:
        result = con.execute(sql_plan_lv1.where(and_(salesRecord.year == thisYear,salesRecord.version == '(P)',
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


pdf1_list = call_this_lv1()
pdf1_pre_list = call_pre_lv1()
pdf1_plan_list = call_plan_lv1()

st.header('판매실적\:Report')

# # with st.container(border=1):
# #     col1, col2, col3 = st.columns(3)
# #     with col1:
# #         with st.container(border=1):
# #             st.write('▶ 매출액 (단위:백만원)')
# #             st.bar_chart(pdf1_list[0].iloc[-1:,0:-1].reset_index(drop=True).T)
# #     with col2:
# #         with st.container(border=1):
# #             st.write('▶ 판매수량 (단위:천본)')
# #             st.bar_chart(pdf1_list[1].iloc[-1:,0:-1].reset_index(drop=True).T)
# #     with col3:
# #         with st.container(border=1):
# #             st.write('▶ 판매단가 (단위:원/KG)')
# #             st.line_chart(pdf1_list[2].iloc[-1:,0:-1].reset_index(drop=True).T)

tab1, tab2, tab3 = st.tabs(["대분류", "본부레벨",  "임원레벨"])
with tab1:
    st.write("1.대분류판매실적(단위:백만원)")
    show_list = pd.DataFrame([pdf1_pre_list[0]['06'],pdf1_plan_list[0]['06'],pdf1_list[0]['05'],pdf1_list[0]['06']],
                             index=['전년(A)','계획(P)','전월(A)','실적(A)']).T
    show_list['전월比'] = show_list['실적(A)'] - show_list['전월(A)']
    show_list['계획比'] = show_list['실적(A)'] - show_list['계획(P)']
    show_list['동기比'] = show_list['실적(A)'] - show_list['전년(A)']
    show_list_tot = pd.DataFrame([pdf1_pre_list[0]['총계'],pdf1_pre_list[0]['총계'],pdf1_list[0]['총계']],
                             index=['동기누계','누계계획','누계실적']).T
    show_list_tot['누계계획比'] = show_list_tot['누계실적'] - show_list_tot['누계계획']
    show_list_tot['누계동기比'] = show_list_tot['누계실적'] - show_list_tot['동기누계']
    show_result = show_list.join(show_list_tot, how='left')
    # multi_cols = [['6월','6월','6월','6월','6월','6월','6월','누계','누계','누계','누계','누계'],
    #                        ['전년(A)','계획(P)','전월(A)','실적(A)','전월比','계획比','동기比','동기누계','누계계획','누계실적','누계계획比','누계동기比']]
    multi_cols = ['당월\n전년(A)','계획(P)','전월(A)','실적(A)','전월比','계획比','동기比','동기누계','누계계획','누계실적','누계계획比','누계동기比']
    idx1 = list(show_result.index)
    idx1[len(list(idx1))-1] = '계'
    show_result.index = idx1
    show_result.columns = multi_cols
    st.write(show_result)
    st.write('당월\n전년(A)')
    st.table(show_result)
    # vshow = show_result.T
    # vshow.index=multi_cols

    # idx = [['IDX1','IDX1','IDX2','IDX2'],['row1','row2','row3','row4']]
    # col = [['COL1','COL1','COL2','COL2'],['val1','val2','val3','val4']]
    # data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] 
    # df = pd.DataFrame(data,idx,col)
    # st.write(df.to_html(), unsafe_allow_html=True)


    # st.write(vshow.reset_index())
    st.write(pdf1_list[0])


    # with st.expander("수량, 원단위 보기"):
    #     col1, col2, col3 = st.columns(3)
    #     with col1:
    #         st.write('실적')
    #         st.write(pdf1_list[1].round(0))
    #     with col2:
    #         st.write('계획')
    #         st.write(pdf1_plan_list[1].round(0))
    #     with col3:
    #         st.write('전년')
    #         st.write(pdf1_pre_list[1].round(0))

    # with st.expander("수량, 원단위 보기"):
    #     col1, col2, col3 = st.columns(3)
    #     with col1:
    #         st.write('실적')
    #         st.write(pdf1_list[2].round(0))
    #     with col2:
    #         st.write('계획')
    #         st.write(pdf1_plan_list[2].round(0))
    #     with col3:
    #         st.write('전년')
    #         st.write(pdf1_pre_list[2].round(0))

        # st.write("2.대분류판매실적(단위:천본)")
        # st.write(pdf1_list[1].round(0))
        # st.write("3.원단위매출액(단위:원/KG)")
        # st.write(pdf1_list[2].round(0))
    # pass
#     with st.container(border=1):
#         st.write("1.매출액(단위:백만원)")
#         st.write(pdf1_list3[0])
#         with st.expander("수량, 원단위 보기"):
#             st.write("2.판매수량(단위:천본)")
#             st.write(pdf1_list3[1].round(0))
#             st.write("3.원단위매출액(단위:원/KG)")
#             st.write(pdf1_list3[2].round(0))

with tab2:
    pass
    # with st.container(border=1):
    #     st.write("1.매출액(단위:백만원)")
    #     st.write(pdf1_list2[0])
    #     with st.expander("수량, 원단위 보기"):
    #         st.write("2.판매수량(단위:천본)")
    #         st.write(pdf1_list2[1])
    #         st.write("3.원단위매출액(단위:원/KG)")
    #         st.write(pdf1_list2[2].round(0))


with tab3:
    pass
    # with st.container(border=1):
    #     st.write("1.대분류판매실적(단위:백만원)")
    #     st.write(pdf1_list[0])
    #     with st.expander("수량, 원단위 보기"):
    #         st.write("2.대분류판매실적(단위:천본)")
    #         st.write(pdf1_list[1].round(0))
    #         st.write("3.원단위매출액(단위:원/KG)")
    #         st.write(pdf1_list[2].round(0))

# with st.container(border=1):
#     st.write("1.대분류판매실적(단위:백만원)")
#     st.write(pdf1_list[0])
#     with st.expander("수량, 원단위 보기"):
#         st.write("2.대분류판매실적(단위:천본)")
#         st.write(pdf1_list[1].round(0))
#         st.write("3.원단위매출액(단위:원/KG)")
#         st.write(pdf1_list[2].round(0))