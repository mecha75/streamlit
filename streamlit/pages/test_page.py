import streamlit as st

master_date = {
'fromMonth':'01',
'toMonth':'07',
'beforeMonth':'06',
'thisYear':'2024',
'preYear':'2023'
}

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
        master_date['thisYear'] = option_year
        master_date['fromMonth'] = option_startMonth
        master_date['toMonth'] = option_month
        master_date['beforeMonth'] = option_preMonth

st.write('선택하신 년도:', master_date['thisYear'], '   전년도:', master_date['preYear'],'   비교시작월:', master_date['fromMonth'],'   선택월:', master_date['toMonth'],'   전월:', master_date['beforeMonth'] )
st.write('선택하신 데이터(날짜)가 맞는지 확인하십시요.')


if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()