
import streamlit as st
import os, importlib

st.sidebar.info('出现 DuplicateWidgetID 报错后，按 [R] 或点击右上角设置 Rerun')

challenge_list = [file.split('.py')[0] for file in os.listdir() 
                if file.startswith('day')]

challenge_day = st.sidebar.selectbox('Challenge', challenge_list)

app = importlib.import_module(challenge_day)
importlib.reload(app)