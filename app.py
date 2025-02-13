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

page03 = st.Page("pages/page_03.py", title = '1. Детекция лиц')
page031 = st.Page("pages/page_031.py", title = '- Описание модели')

page04 = st.Page("pages/page_04.py", title = '2. Сегментация аэрокосмических снимков')
page041 = st.Page("pages/page_041.py", title = '- Описание модели')

page05 = st.Page("pages/page_05.py", title = '3. Детекция ветрогенераторов')
page051 = st.Page("pages/page_051.py", title = ' - Описание модели')

page06 = st.Page("pages/page_06.py", title = '4. Семантическая детекция ветрогенераторов')
page061 = st.Page("pages/page_061.py", title = '- Описание модели')

pg = st.navigation([page01, page02, 
                    page03, page031, 
                    page04, page041, 
                    page05, 
                    page051,
                    page06,
                    page061
                    ], expanded=True)
pg.run()


st.sidebar.title('Команда проекта: ')
st.sidebar.write('Даша Акулова')
st.sidebar.write('Алина Зарницина')
st.sidebar.write('Илья Тищенко')
st.sidebar.write('Андрей Абрамов')

    


    






