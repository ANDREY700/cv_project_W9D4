# ELBRUSE Bootcamp 
# 13-02-2025
# Week 9 Day 4 Project
# team: Dasha, Alina, Ilya, Andrey u

import streamlit as st
import pandas as pd



#initialization ----------------------------


#Основная страница  ----------------------------
# боковая панель
page01 = st.Page("pages/page_01.py", title = 'Оглавление')
page02 = st.Page("pages/page_02.py", title = 'Описание поставленной задачи')
page03 = st.Page("pages/page_03.py", title = 'Детекция лиц')
page04 = st.Page("pages/page_04.py", title = 'Сегментация аэрокосмических снимков')
page05 = st.Page("pages/page_05.py", title = 'Детекция ветрогенераторов')
page06 = st.Page("pages/page_06.py", title = 'Семантическая детекция ветрогенераторов')

pg = st.navigation([page01, page02, page03, page04, page05, page06], expanded=True)
pg.run()


st.sidebar.title('Команда проекта: ')
st.sidebar.write('Даша Акулова')
st.sidebar.write('Алина Зарницина')
st.sidebar.write('Илья Тищенко')
st.sidebar.write('Андрей Абрамов')

    


    






