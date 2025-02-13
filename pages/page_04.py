# ELBRUSE Bootcamp 
# 13-02-2025
# Week 9 Day 4 Project
# team: Dasha, Alina, Ilya, Andrey 



import streamlit as st
import pandas as pd
import torch 
import time
import requests
import datetime
from PIL import Image
from torchvision import transforms
import os
from io import BytesIO

def get_prediction(image, model):
    transform = transforms.Compose([
        transforms.Resize((224, 224)), # Изменение размера изображения
        transforms.ToTensor() # Преобразование в тензор
    ])
    input_tensor = transform(image)
    with torch.inference_mode():
        pred_class = torch.argmax(model(input_tensor.unsqueeze(0).to('cpu'))).item()
    return pred_class

def load_image_from_url(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Проверяем, что запрос успешен
    image = Image.open(BytesIO(response.content)).convert("RGB") # Указываем RGB
    return image


try:
    #st.write('Загрука файла модели спортивной фотографии')
    #with st.spinner("Загрузка... ", show_time=True):
    #    await asyncio.sleep(0.5)
    #    time.sleed(5)
    
    model_sport = torch.load('model_sport.pth', weights_only=False, map_location='cpu')
except:
    st.write('Ошибка загрузки файла модели спортивной фотографии')
else:
    try:
        
        model_blood = torch.load('model_eff3_blood.pth', weights_only=False, map_location='cpu')
    except:
        st.write('Ошибка загрузки файла модели клеток крови')
    else:
        try:
            blood_labels = pd.read_csv('data_labels_blood.csv')
            sport_labels = pd.read_csv('data_labels_sport.csv')
        except:
            st.write('Ошибка загрузки одного из файлов модели')
        else:       
        
            st.write('Статус загрузки моделей: ')
            st.write('* файл модели клеток крови загружен успешно')
            st.write('* файла модели спортивной фотографии загружен успешно')

            st.title('Модель классификации фотографии')

            st.write(' ')
            MODELS_SET = ['Модель классификации типа спорта', 'Модель классификации клетки крови']
            sel_model = st.selectbox('Выберите одну из моделей для работы', MODELS_SET) 
           # if st.button('Использовать', type='primary'):
            if sel_model == MODELS_SET[0]:
                model = model_sport
                labels = sport_labels
            else:
                model = model_blood
                labels = blood_labels


            st.write(' ')
            st.subheader('Вариант 1 : загрузка фотографии')
            file1 = st.file_uploader("Загрузить файл", type= ['jpg'])  
            if file1 is not None:
                try:
                    data01 = Image.open(file1)
                except:
                    st.write('Возникли проблемы с загрузкой файла!')
                else:
                    st.write('Файл загружен успешно')
                    st.image(data01, width=250)
                    st.write('Обработка файла:')
                    start = datetime.datetime.now()
                    #st.code('Время старта: ' + str(start))
                    result = get_prediction(data01, model)
                    #st.write(result)
                    #result = 5
                    #st.dataframe(labels)
                    #фиксируем и выводим время окончания работы кода
                    finish = datetime.datetime.now()
                    #st.code('Время окончания: ' + str(finish))

                    # вычитаем время старта из времени окончания
                    st.code('Время работы модели, секунд : ' + str((finish - start).total_seconds()))
                    st.code('Модель определила фото как класс "'+str(result) + '" и "' + labels.iloc[result, 0] + '"')

            
            st.write(' ')
            st.subheader('Вариант 2 : загрузка по ссылке')
            link1 = st.text_input('', 'https://cdn.britannica.com/87/237587-050-8A4B9F08/Shohei-Ohtani-Los-Angeles-Angels-pitcher-baseball-player-2022.jpg')  
            st.write('PS: проверка корректности введенной ссылки не производится!')
            if st.button('Запустить', type='primary'):
                try:
                    data01 = load_image_from_url(link1)
                    #data01 = requests.get(link1).content
                    #data01 = Image.open(img_data)
                except:
                    st.write('Возникли проблемы с загрузкой файла!')
                else:
                    st.write('Файл загружен успешно')
                    st.image(data01)
                    st.write('Обработка файла:')
                    start = datetime.datetime.now()
                    #st.code('Время старта: ' + str(start))
                    result = get_prediction(data01, model)
                    #st.write(result)
                    #result = 5
                    #st.dataframe(labels)
                    #фиксируем и выводим время окончания работы кода
                    finish = datetime.datetime.now()
                    #st.code('Время окончания: ' + str(finish))

                    # вычитаем время старта из времени окончания
                    st.code('Время работы модели, секунд : ' + str((finish - start).total_seconds()))
                    st.code('Модель определила фото как класс "'+str(result) + '" и "' + labels.iloc[result, 0] + '"')

            
                
                



            st.write(' ')
            st.subheader('Вариант 3 : обработка пакета файлов')
            st.write(' ')
            file3= st.file_uploader("Загрузить файл", type= ['jpg'], accept_multiple_files=True)  
            if file3 is not None:
                for file1 in file3:
                    try:
                        data01 = Image.open(file1)
                    except:
                        st.write('Возникли проблемы с загрузкой файла!')
                    else:
                        st.write('Файл загружен успешно')
                        st.image(data01, width=250)
                        st.write('Обработка файла:')
                        start = datetime.datetime.now()
                        #st.code('Время старта: ' + str(start))
                        result = get_prediction(data01, model)
                        #st.write(result)
                        #result = 5
                        #st.dataframe(labels)
                        #фиксируем и выводим время окончания работы кода
                        finish = datetime.datetime.now()
                        #st.code('Время окончания: ' + str(finish))

                        # вычитаем время старта из времени окончания
                        st.code('Время работы модели, секунд : ' + str((finish - start).total_seconds()))
                        st.code('Модель определила фото как класс "'+str(result) + '" и "' + labels.iloc[result, 0] + '"')


