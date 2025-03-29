import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model
model = load("./models/stroke_prediction_model.joblib") 

# Custom Styling
st.markdown(
    """
    <style>
        .main { background-color: #f5f5f5; }
        .title { color: #1f77b4; text-align: center; font-size: 32px; font-weight: bold; margin-bottom: 5px; }
        .subtitle { text-align: center; font-size: 18px; color: #4a4a4a; margin-bottom: 20px; }
        .footer { text-align: center; font-size: 14px; color: #888888; margin-top: 40px; }
        .stButton>button { background-color: #1f77b4; color: white; border-radius: 10px; font-size: 16px; padding: 8px 20px; }
        .stColumns { display: flex; justify-content: space-between; padding: 15px 0; }  /* Increased padding */
        .stColumn { padding: 0 20px; }  /* Increased padding */
        .result-box {
            text-align: center; 
            font-size: 20px; 
            padding: 15px; 
            border-radius: 10px; 
            font-weight: bold;
        }
        .green-box { background-color: #d4edda; color: #155724; }
        .red-box { background-color: #f8d7da; color: #721c24; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title & Description
st.markdown('<p class="title">🧠 Stroke Risk Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Fill in your details below to check your stroke risk.</p>', unsafe_allow_html=True)

# Function to make predictions
def predict_stroke(input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    if prediction == 0:
        return "🟢 Low Risk (No Stroke)", "green-box"
    else:
        return "🔴 High Risk (Possible Stroke)", "red-box"

# Layout: Three columns with more spacing
col1, space1, col2, space2, col3 = st.columns([1, 0.4, 1, 0.4, 1])

with col1:
    st.markdown("### 🔢 Personal Info")
    age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
    ever_married = st.radio("Ever Married?", ["No", "Yes"])
    avg_glucose_level = st.number_input("Glucose Level", min_value=0.0, value=100.0, step=0.1)

with col2:
    st.markdown("### 💉 Health Factors")
    hypertension = st.toggle("Hypertension (High BP)", value=False)
    work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"])
    bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, value=25.0, step=0.1)

with col3:
    st.markdown("### 🏡 Lifestyle")
    heart_disease = st.toggle("Heart Disease", value=False)
    residence_type = st.radio("Residence Type", ["Urban", "Rural"])
    smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

# Convert toggle values to 0 or 1
hypertension = 1 if hypertension else 0
heart_disease = 1 if heart_disease else 0

# Prepare input data
input_data = {
    "age": age,
    "hypertension": hypertension,
    "heart_disease": heart_disease,
    "ever_married": ever_married,
    "work_type": work_type,
    "Residence_type": residence_type,
    "avg_glucose_level": avg_glucose_level,
    "bmi": bmi,
    "smoking_status": smoking_status
}

# Add space before button
st.write("")
st.write("")

# Center-align the button
col_center = st.columns([1, 3, 1])[1]
with col_center:
    if st.button("🔍 Predict Stroke Risk", use_container_width=True):
        result_text, box_class = predict_stroke(input_data)
        st.markdown(f'<div class="result-box {box_class}">{result_text}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">🔬 Powered by Machine Learning | Developed with ❤️ by <b>Prateek Kumar Prasad</b> using Streamlit</p>', unsafe_allow_html=True)

