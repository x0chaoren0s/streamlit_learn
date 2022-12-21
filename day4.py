import streamlit as st

sb = st.sidebar.selectbox('下拉菜单', ['选择1','选择2'])

if sb=='选择1':
    st.write('下拉菜单选择了【选择1】')
else:
    st.write('下拉菜单选择了【选择2】')

st.write('222')

st.sidebar.select_slider('滑动选择条',['选择a','选择b'])

st.metric('指标1', 66.6, 2)
st.metric('指标2', 666.6, 2, delta_color='inverse')
st.metric('指标3', 666.6, '2%', delta_color='inverse')