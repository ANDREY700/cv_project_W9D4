# ELBRUSE Bootcamp 
# 13-02-2025
# Week 9 Day 4 Project
# team: Dasha, Alina, Ilya, Andrey 

import streamlit as st
import pandas as pd



st.title('Оглавление')


col1, col2, col3 = st.columns(spec=[0.2, 0.6, 0.2])
with col1:
    st.image('images/Face_detection.PNG', width=100)
with col2:
    st.page_link("pages/page_03.py", label='* Детекция лиц с модулем ....')
with col3:
    st.page_link("pages/page_031.py", label='Описание модели')

col1, col2, col3 = st.columns(spec=[0.2, 0.6, 0.2])
with col1:
    st.image('images/aero03.PNG', width=100)
with col2:
    st.page_link("pages/page_04.py", label='* Сегментация аэрокосмических снимков (UNET)')
    st.page_link("pages/page_042.py", label='* Сегментация аэрокосмических снимков (YOLO)')
with col3:
    st.page_link("pages/page_041.py", label='Описание модели')
    st.page_link("pages/page_043.py", label='Описание модели')

col1, col2, col3 = st.columns(spec=[0.2, 0.6, 0.2])
with col1:
    st.image('images/wind04.PNG', width=100)
with col2:
    st.page_link("pages/page_05.py", label='* Детекция ветрогенераторов (YOLO)')
    st.page_link("pages/page_052.py", label='* Детекция ветрогенераторов (...)')
with col3:
    st.page_link("pages/page_051.py", label='Описание модели')
    st.page_link("pages/page_053.py", label='Описание модели')


col1, col2, col3 = st.columns(spec=[0.2, 0.6, 0.2])
with col1:
    st.image('images/wind03.PNG', width=100)
with col2:
    st.page_link("pages/page_06.py", label='* Семантическая детекция ветрогенераторов (YOLO)')
with col3:
    st.page_link("pages/page_061.py", label='Описание модели')

