import pickle
import streamlit as st


# loading the saved models

breast_cancer_model = pickle.load(open('/Users/divyanshpalia/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))


breast_cancer_model=pickle.load(open('/Users/divyanshpalia/Desktop/Multiple Disease Prediction System/saved models/breast_cancer_dataset.sav', 'rb'))

# sidebar for navigation
#shreya is sexy
#shreya is smart 
#shreya is gorgeous
#shryea is my wife
with st.sidebar:
    st.title('Breast Cancer Prediction System')
    selected=st.selectbox('Choose the disease :',('Breast Cancer Prediction','Breast Cancer Prediction'))
  
    
    

if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')

    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        diab_prediction = breast_cancer_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Breast Cancer : Benign'
        else:
          diab_diagnosis = 'Breast Cancer : Malignant'
        
    st.success(diab_diagnosis)






