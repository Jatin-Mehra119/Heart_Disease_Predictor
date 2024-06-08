import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load(r"C:\Users\Admin\Desktop\Jatin\Cardio_health_Risk\Cardio_healthRiskPred.pkl")

# Function to predict heart disease
def predict_heart_disease(input_data):
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
def main():
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
        else:
            st.write("Prediction: Heart Disease Absent")
    st.write("The Model is Trained By Jatin Mehra. For more info Email me: jatinmehra119@gmail.com")

if __name__ == "__main__":
    main()