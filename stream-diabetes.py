import pickle
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('MESIN PREDIKSI PENYAKIT DIABETES')

#membagi kolom
col1, col2 = st.columns(2)


with col1 :
    Pregnancies = st.text_input ('masukkan nilai Pregnancies')

with col2 :
    Glucose = st.text_input ('masukkan nilai Glucose')
    
with col1 :
    BloodPressure = st.text_input ('masukkan nilai BloodPressure')

with col2 :
    SkinThickness = st.text_input ('masukkan nilai SkinThickness')

with col1 :
    Insulin = st.text_input ('masukkan nilai Insulin')

with col2 :
    BMI = st.text_input ('masukkan nilai BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('masukkan nilai DiabetesPedigreeFunction')

with col2 :    
    Age = st.text_input ('masukkan nilai Age')


#kode untuk prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('TES DIABETES'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = "PASIEN MENGIDAP PENYAKIT DIABETES"
    else :
        diab_diagnosis = "PASIEN TIDAK MENGIDAP PENYAKIT DIABETES"
    
    st.success(diab_diagnosis)