import streamlit as st

st.header("Семантическая Детекция ветрогенераторов")
st.header("ℹ️ YOLO11: Информация")

st.divider()
epochs = 160 
train_size = 219
val_size = 17
test_size = 0
st.header("📌 Основные параметры обучения")
st.write(f"📆 **Число эпох:** `{epochs}`")
st.write(f"🖼 **Обучающая выборка:** `{train_size}` изображений")
st.write(f"🖼 **Валидационная выборка:** `{val_size}` изображений")
#st.write(f"🖼 **Тестовая выборка:** `{test_size}` изображений")
st.markdown("📂 **Датасет:** частично доступен на [Roboflow](https://universe.roboflow.com/kyle-graupe-jobhn/wind-farms), обновлен и добавлены дополнительные фотографии")

st.divider()

st.header("📈 Метрики модели")

col1, col2 = st.columns(2)
with col1:
    st.subheader("📉 F1-score")
    st.image('images/BoxF1_curveA1.png')
with col2:
    st.subheader("📉 PR-кривая")
    st.image('images/BoxPR_curveA1.png')

st.subheader("📊 Precision & Recall")
col1, col2 = st.columns(2)
with col1:
    st.image('images/BoxP_curveA1.png', caption="📈 Precision")
with col2:
    st.image('images/BoxR_curveA1.png', caption="📉 Recall")

st.subheader("📊 Confusion Matrix")
col1, col2 = st.columns(2)
with col1:
    st.image('images/confusion_matrix_normalizedA1.png', caption="✅ Нормализованная версия")
with col2:
    st.image('images/confusion_matrixA1.png', caption="🔎 Базовая версия")

st.divider()

st.header("🖼 Примеры из обучения модели")
st.image('images/val_batch0_labelsA1.jpg', caption='✅ Истинные значения')
st.image('images/val_batch0_predA1.jpg', caption='🤖 Предсказанные значения')