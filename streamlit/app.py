import streamlit as st


Review_page = st.Page("pages/sales.py", title="매출액/수량/단가", icon=":material/add_circle:")
Report_page = st.Page("pages/sales_report.py", title="계획대비", icon=":material/add_circle:")
HVP_page = st.Page("pages/HVP1.py", title="HVP1", icon=":material/add_circle:")
HVP_price = st.Page("pages/HVP_price.py", title="HVP price 비율(HVP vs nonHVP)", icon=":material/add_circle:")
RIM_price = st.Page("pages/RIM.py", title="인치별판매단가(PC/LT)", icon=":material/add_circle:")
RIM_price_TB = st.Page("pages/RIM_TB.py", title="인치별판매단가(TBR)", icon=":material/add_circle:")
test_page = st.Page("pages/test_page.py", title="테스트페이지")

pg = st.navigation([Review_page, Report_page, HVP_page, HVP_price,RIM_price,RIM_price_TB,test_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:",layout="wide")
pg.run()
