import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("Cardio_healthRiskPred.pkl")

# Function to predict heart disease
def predict_heart_disease(input_data):
    prediction = model.predict(input_data)
    return prediction[0]

# Function to provide health tips for those already having heart disease
def provide_health_advice(user_data):
    advice = [
        "Consult with a healthcare professional about managing your condition.",
        "Adopt a low-cholesterol diet and exercise regularly to manage cholesterol levels.",
        "Manage your blood sugar levels through diet, exercise, and medication if necessary.",
        "Monitor your blood pressure and consider lifestyle changes or medication to lower it.",
        "Regular check-ups are important to monitor and manage your condition."
    ]
    return advice

# Function to provide health tips for preventing heart disease
def provide_health_tips(user_data):
    tips = []
    if user_data['Age'][0] > 50:
        tips.append("Maintain a healthy diet and exercise regularly to manage your weight and blood pressure.")
    if user_data['Sex'][0] == "Male":
        tips.append("Regular check-ups are important, as men are at higher risk of heart disease.")
    if user_data['BP'][0] > 130:
        tips.append("Monitor your blood pressure and consider lifestyle changes or medication to lower it.")
    if user_data['Cholesterol'][0] > 200:
        tips.append("Adopt a low-cholesterol diet and exercise regularly to manage cholesterol levels.")
    if user_data['FBS over 120'][0] == 1:
        tips.append("Manage your blood sugar levels through diet, exercise, and medication if necessary.")
    if user_data['Max HR'][0] < 100:
        tips.append("Engage in regular physical activity to improve your heart rate.")
    if user_data['Exercise angina'][0] == 1:
        tips.append("Consult with a healthcare professional about managing angina symptoms during exercise.")
    
    return tips

st.title("Heart Disease Predictor")

st.write("Welcome to the Heart Disease Predictor!")
st.write("This app provides predictions on the presence or absence of heart disease based on input parameters.")

st.write("Disclaimer: The predictions made by this model are for informational purposes only and should not be considered as medical advice. Always consult a qualified medical professional for accurate diagnosis and treatment.")

st.write("Please note that our model is trained with individuals aged between 28 and 85. Predictions for individuals outside this age range may not be accurate.")

# User input fields
age = st.slider("Age", min_value=28, max_value=100, step=1)
sex = st.selectbox("Sex", ["Female", "Male"])
chest_pain_type = st.selectbox("Chest pain type", [1, 2, 3, 4])
bp = st.number_input("Blood Pressure", value=120, step=1)
cholesterol = st.number_input("Cholesterol", value=200, step=1)
fbs_over_120 = st.selectbox("Fasting blood sugar > 120 mg/dl", ["False", "True"])
ekg_results = st.selectbox("EKG results", [0, 1, 2])
max_hr = st.number_input("Maximum heart rate achieved", value=150, step=1)
exercise_angina = st.selectbox("Exercise-induced angina", ["No", "Yes"])
st_depression = st.number_input("ST depression induced by exercise relative to rest", min_value=0, max_value=5)
slope_of_st = st.selectbox("Slope of the peak exercise ST segment", [1, 2, 3])
num_vessels_fluro = st.selectbox("Number of major vessels colored by fluoroscopy", [0, 1, 2, 3])
thallium = st.selectbox("Thallium stress test result", [3, 6, 7])

# Convert user input to DataFrame
user_input = pd.DataFrame({
    'Age': [age],
    'Sex': [sex],
    'Chest pain type': [chest_pain_type],
    'BP': [bp],
    'Cholesterol': [cholesterol],
    'FBS over 120': [1 if fbs_over_120 == "True" else 0],
    'EKG results': [ekg_results],
    'Max HR': [max_hr],
    'Exercise angina': [1 if exercise_angina == "Yes" else 0],
    'ST depression': [st_depression],
    'Slope of ST': [slope_of_st],
    'Number of vessels fluro': [num_vessels_fluro],
    'Thallium': [thallium]
})

if st.button("Predict"):
    prediction = predict_heart_disease(user_input)
    if prediction == "Presence":
        st.write("Prediction: Heart Disease Present")
        st.write("Health Advice:")
        health_advice = provide_health_advice(user_input)
        for advice in health_advice:
            st.write(f"- {advice}")
    else:
        st.write("Prediction: Heart Disease Absent")
        st.write("Health Tips to Avoid Future Heart Disease:")
        health_tips = provide_health_tips(user_input)
        for tip in health_tips:
            st.write(f"- {tip}")

st.write("The Model is Trained By Jatin Mehra. For more info Email me: jatinmehra119@gmail.com")
