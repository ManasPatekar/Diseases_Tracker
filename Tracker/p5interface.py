import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Prediction of Disease Outbreaks",
                   layout="wide",
                   page_icon="🧑‍⚕")

# Open the image
image_path = "F:/temp/man.jpg"
image = Image.open(image_path)

# Resize the image
new_width = 300  # You can adjust this value as needed
new_height = 100
resized_image = image.resize((new_width, new_height))

# Display the image
st.image(resized_image, use_container_width=True)

# Custom CSS styling for a professional look
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
    }
    .stButton button {
        background-color:rgb(71, 73, 209); /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color:rgb(59, 62, 204);
    }
    .sidebar .sidebar-content {
        width: 300px;
    }
    .stNumberInput>div>div>input {
        background-color: #f9f9f9; /* Light grey */
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open('model_files/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('model_files/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('model_files/parkinsons_model.sav', 'rb'))

#TOP Navigation menu
st.title("Prediction of Disease Outbreak")
selected=st.selectbox("Select for Prediction",["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"])

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('🩺 Diabetes Prediction using Machine Learning')
    st.write("### Enter the following details:")

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1, format='%d')

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0, max_value=300, step=1, format='%d')

    with col3:
        BloodPressure = st.number_input('Blood Pressure Value', min_value=0, max_value=200, step=1, format='%d')

    with col1:
        SkinThickness = st.number_input('Skin Thickness Value', min_value=0, max_value=100, step=1, format='%d')

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0, max_value=900, step=1, format='%d')

    with col3:
        BMI = st.number_input('BMI Value', min_value=0.0, max_value=70.0, step=0.1, format='%.1f')

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, max_value=2.5, step=0.01, format='%.2f')

    with col2:
        Age = st.number_input('Age of the Person', min_value=0, max_value=120, step=1, format='%d')

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Get Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            st.error(diab_diagnosis)
        else:
            diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('❤ Heart Disease Prediction using Machine Learning')
    st.write("### Enter the following details:")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=0, max_value=120, step=1, format='%d')

    with col2:
        sex = st.selectbox('Sex', options=['Male', 'Female'])

    with col3:
        cp = st.selectbox('Chest Pain Types', options=['Type 1', 'Type 2', 'Type 3', 'Type 4'])

    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=200, step=1, format='%d')

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, max_value=600, step=1, format='%d')

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=['True', 'False'])

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', options=['Normal', 'Abnormal'])

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250, step=1, format='%d')

    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=['Yes', 'No'])

    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, step=0.1, format='%.1f')

    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=['Upsloping', 'Flat', 'Downsloping'])

    with col3:
        ca = st.number_input('Major Vessels Colored by Flourosopy', min_value=0, max_value=4, step=1, format='%d')

    with col1:
        thal = st.selectbox('Thalassemia', options=['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Get Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        # Convert categorical variables to numerical (e.g., Male/Female to 0/1)
        user_input[1] = 1 if user_input[1] == 'Male' else 0
        user_input[2] = int(user_input[2][-1])
        user_input[5] = 1 if user_input[5] == 'True' else 0
        user_input[6] = 0 if user_input[6] == 'Normal' else 1
        user_input[8] = 1 if user_input[8] == 'Yes' else 0
        user_input[10] = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}[user_input[10]]
        user_input[12] = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}[user_input[12]]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            st.error(heart_diagnosis)
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    # Page title
    st.title("🧠 Parkinson's Disease Prediction using Machine Learning")
    st.write("### Enter the following details:")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, max_value=500.0, step=0.1, format='%.1f')

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, max_value=500.0, step=0.1, format='%.1f')

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, max_value=500.0, step=0.1, format='%.1f')

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, max_value=0.1, step=0.001, format='%.3f')

    with col1:
        RAP = st.number_input('MDVP:RAP', min_value=0.0, max_value=0.1, step=0.001, format='%.3f')

    with col2:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0, max_value=0.1, step=0.001, format='%.3f')

    with col3:
        DDP = st.number_input('Jitter:DDP', min_value=0.0, max_value=0.3, step=0.001, format='%.3f')

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, max_value=10.0, step=0.1, format='%.1f')

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    with col3:
        APQ = st.number_input('MDVP:APQ', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    with col4:
        DDA = st.number_input('Shimmer:DDA', min_value=0.0, max_value=0.3, step=0.001, format='%.3f')

    with col5:
        NHR = st.number_input('NHR', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    with col1:
        HNR = st.number_input('HNR', min_value=0.0, max_value=50.0, step=0.1, format='%.1f')

    with col2:
        RPDE = st.number_input('RPDE', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    with col3:
        DFA = st.number_input('DFA', min_value=0.0, max_value=2.0, step=0.01, format='%.2f')

    with col4:
        spread1 = st.number_input('spread1', min_value=-10.0, max_value=0.0, step=0.1, format='%.1f')

    with col5:
        spread2 = st.number_input('spread2', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    with col1:
        D2 = st.number_input('D2', min_value=0.0, max_value=10.0, step=0.1, format='%.1f')

    with col2:
        PPE = st.number_input('PPE', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')

    # Code for Prediction
    parkinsons_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Get Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
            st.error(parkinsons_diagnosis)
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
