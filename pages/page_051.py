import streamlit as st

st.header("Детекция ветрогенераторов")
st.title("ℹ️ YOLO11: Информация")

st.divider()
epochs = 100 
train_size = 2643
val_size = 247 
test_size = 130
st.header("📌 Основные параметры обучения")
st.write(f"📆 **Число эпох:** `{epochs}`")
st.write(f"🖼 **Обучающая выборка:** `{train_size}` изображений")
st.write(f"🖼 **Валидационная выборка:** `{val_size}` изображений")
st.write(f"🖼 **Тестовая выборка:** `{test_size}` изображений")
st.markdown("📂 **Датасет:** доступен на [Roboflow](https://universe.roboflow.com/kyle-graupe-jobhn/wind-farms)")

st.divider()

st.header("📈 Метрики модели")

col1, col2 = st.columns(2)
with col1:
    st.subheader("📉 F1-score")
    st.image('images/F1_curve_I.png')
with col2:
    st.subheader("📉 PR-кривая")
    st.image('images/PR_curve_I.png')

st.subheader("📊 Precision & Recall")
col1, col2 = st.columns(2)
with col1:
    st.image('images/P_curve_I.png', caption="📈 Precision")
with col2:
    st.image('images/R_curve_I.png', caption="📉 Recall")

st.subheader("📊 Confusion Matrix")
col1, col2 = st.columns(2)
with col1:
    st.image('images/confusion_matrix_normalized_I.png', caption="✅ Нормализованная версия")
with col2:
    st.image('images/confusion_matrix_I.png', caption="🔎 Базовая версия")

st.divider()

st.header("🖼 Примеры из обучения модели")
st.image('images/val_batch0_labels_I.jpg', caption='✅ Истинные значения')
st.image('images/val_batch0_pred_I.jpg', caption='🤖 Предсказанные значения')