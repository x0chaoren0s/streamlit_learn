import streamlit as st

st.header('test st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

def click_fun():
    print('pressed btn!')

st.button('btn', on_click=click_fun)
