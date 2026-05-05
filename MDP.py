import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('saved model/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved model/heart_model.sav', 'rb'))
parkinson_disease_model = pickle.load(open('saved model/parkinson_model.sav', 'rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System' ,
                           ['Diabetes Prediction System' , 'Heart Disease Prediction System' , 'Parkinsons Prediction System'] ,icons=["activity", "heart","person"],
                            default_index=0)
    #index shows which page to open first in this case diabetes but if index 1 then heart disease will be there

#when diabetes selected
if (selected == 'Diabetes Prediction System'):
    #Page Title
    st.title('Diabetes Prediction System')

    #GETTING INPUT DATA FROM USER
    #COLUMNS FOR INPUT FIELD
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Pregnancies Value')
    with col2:
        Glucose = st.text_input('Glucose Value')
    with col3:
        BloodPressure = st.text_input('BloodPressure Value')
    with col1:
        SkinThickness = st.text_input('SkinThickness Value')
    with col2:
        Insulin = st.text_input('Insulin Value')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of Person')

# PREDICTION THROUGH VALUE
    diab_diagnosis = ''
    # creating a button for prediciton
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin , BMI , DiabetesPedigreeFunction , Age]])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is Diabetic'
            else:
                diab_diagnosis = 'The person is NOT Diabetic'

        except:
            diab_diagnosis = '⚠️ Please enter valid numeric values in all fields'

    st.success(diab_diagnosis)

#when heart disease selected
if selected == 'Heart Disease Prediction System':
    st.title('Heart Disease Prediction System')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age of person', min_value=1)
    with col2:
        sex = st.selectbox('Gender', [0, 1])  # 0 = Female, 1 = Male
    with col3:
        cp = st.selectbox('Chest pain type', [0, 1, 2, 3])
    with col1:
        trestbps = st.number_input('Resting Blood Pressure Value')
    with col2:
        chol = st.number_input('Serum Cholesterol (mg/dl)')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
    with col1:
        restecg = st.selectbox('Rest ECG (0,1,2)', [0, 1, 2])
    with col2:
        thalach = st.number_input('Maximum heart rate achieved')
    with col3:
        exang = st.selectbox('Exercise induced angina', [0, 1])
    with col1:
        oldpeak = st.number_input('Old Peak Value')
    with col2:
        slope = st.selectbox('Slope (0,1,2)', [0, 1, 2])
    with col3:
        ca = st.selectbox('Number of major vessels (cable value) (0-3)', [0, 1, 2, 3])
    with col1:
        thal = st.selectbox('Thalam (1,2,3)', [1, 2, 3])

    heart_diagnosis = ''
    # creating a button for prediciton
    if st.button('Heart Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[ age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has Heart Disease'
            else:
                heart_diagnosis = 'The person does NOT have Heart Disease'

        except:
            heart_diagnosis = '⚠️ Please enter valid numeric values in all fields'

    st.success(heart_diagnosis)

# Parkinson's Prediction System
if selected == 'Parkinsons Prediction System':
    st.title("Parkinson's Disease Prediction System")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        Jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        RAP = st.text_input('MDVP:RAP')

    with col1:
        PPQ = st.text_input('MDVP:PPQ')
    with col2:
        DDP = st.text_input('Jitter:DDP')
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        APQ = st.text_input('MDVP:APQ')
    with col2:
        DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    # Prediction Button
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [[
                float(fo), float(fhi), float(flo),
                float(Jitter_percent), float(Jitter_abs), float(RAP),
                float(PPQ), float(DDP), float(Shimmer),
                float(Shimmer_dB), float(APQ3), float(APQ5),
                float(APQ), float(DDA), float(NHR),
                float(HNR), float(RPDE), float(DFA),
                float(spread1), float(spread2), float(D2),
                float(PPE)
            ]]

            parkinson_prediction = parkinson_disease_model.predict(input_data)

            if parkinson_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's Disease"
            else:
                parkinsons_diagnosis = "The person does NOT have Parkinson's Disease"

        except:
            parkinsons_diagnosis = '⚠️ Please enter valid numeric values in all fields'

    st.success(parkinsons_diagnosis)