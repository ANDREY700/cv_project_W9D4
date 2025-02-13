# ELBRUSE Bootcamp 
# 13-02-2025
# Week 9 Day 4 Project
# team: Dasha, Alina, Ilya, Andrey 

import streamlit as st
import pandas as pd


#st.title('Страница 01')
st.title('Оглавление')



col1, col2 = st.columns(spec=[0.1, 0.9])
with col1:
    st.image('images/Face_detection.PNG', width=50)
with col2:
    st.page_link("pages/page_03.py", label='* Детекция лиц с модулем ....')

col1, col2 = st.columns(spec=[0.1, 0.9])
with col1:
    st.image('images/aero.png', width=50)
with col2:
    st.page_link("pages/page_04.py", label='* Сегментация аэрокосмических снимков')

col1, col2 = st.columns(spec=[0.1, 0.9])
with col1:
    st.image('images/windTur01.PNG', width=50)
with col2:
    st.page_link("pages/page_05.py", label='* Детекция ветрогенераторов')
    st.page_link("pages/page_051.py", label='* Описание модели')

col1, col2 = st.columns(spec=[0.1, 0.9])
with col1:
    st.image('images/windTur_seg01.PNG', width=50)
with col2:
    st.page_link("pages/page_06.py", label='* Семантическая детекция ветрогенераторов')


