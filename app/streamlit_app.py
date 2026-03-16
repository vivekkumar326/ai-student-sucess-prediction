import streamlit as st
import pandas as pd
import joblib
import os
import google.generativeai as genai

# -----------------------------------
# Configure Gemini API
# -----------------------------------

GEMINI_API_KEY = "AIzaSyDx-0UhW5YQU62phxm9EQyDdlbZRo4Ta4s"

genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------------
# Load Model Files
# -----------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model", "student_success_xgb_model.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "model", "label_encoder.pkl"))
features = joblib.load(os.path.join(BASE_DIR, "model", "feature_columns.pkl"))

# -----------------------------------
# Gemini Explanation Function
# -----------------------------------

def explain_prediction(student_data, prediction):

    prompt = f"""
You are an AI academic advisor helping a university understand student performance.

A machine learning model predicted the student's academic outcome.

Prediction: {prediction}

Student Data:
{student_data}

Please provide:

1. A simple explanation of why this prediction may have occurred.
2. Key academic or financial factors influencing this outcome.
3. Practical recommendations the university can take to support the student.

Use clear and simple language suitable for a university dashboard.
"""

    try:
        response = gemini_model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI explanation unavailable: {e}"


# -----------------------------------
# Streamlit UI
# -----------------------------------

st.title("🎓 AI Student Success Prediction Dashboard")

st.write(
    "This AI system predicts whether a student will **Graduate, Stay Enrolled, or Drop Out** based on academic and financial indicators."
)

st.sidebar.header("Student Information")

age = st.sidebar.slider("Age at Enrollment", 16, 40, 20)

admission_grade = st.sidebar.number_input(
    "Admission Grade", min_value=0.0, max_value=200.0, value=120.0
)

previous_grade = st.sidebar.number_input(
    "Previous Qualification Grade", min_value=0.0, max_value=200.0, value=120.0
)

units1_enrolled = st.sidebar.number_input("1st Semester Units Enrolled", 0, 20, 6)

units1_approved = st.sidebar.number_input("1st Semester Units Approved", 0, 20, 5)

units2_approved = st.sidebar.number_input("2nd Semester Units Approved", 0, 20, 5)

debtor = st.sidebar.selectbox("Debtor", ["No", "Yes"])
debtor = 1 if debtor == "Yes" else 0

scholarship = st.sidebar.selectbox("Scholarship Holder", ["No", "Yes"])
scholarship = 1 if scholarship == "Yes" else 0

tuition = st.sidebar.selectbox("Tuition Fees Up To Date", ["No", "Yes"])
tuition = 1 if tuition == "Yes" else 0

gender = st.sidebar.selectbox("Gender", ["Female", "Male"])
gender = 1 if gender == "Male" else 0


# -----------------------------------
# Prepare Input Data
# -----------------------------------

input_data = {
    "Age at enrollment": age,
    "Admission grade": admission_grade,
    "Previous qualification (grade)": previous_grade,
    "Curricular units 1st sem (enrolled)": units1_enrolled,
    "Curricular units 1st sem (approved)": units1_approved,
    "Curricular units 2nd sem (approved)": units2_approved,
    "Debtor": debtor,
    "Scholarship holder": scholarship,
    "Tuition fees up to date": tuition,
    "Gender": gender
}

data = {feature: 0 for feature in features}

for key in input_data:
    if key in data:
        data[key] = input_data[key]

df = pd.DataFrame([data])


# -----------------------------------
# Prediction
# -----------------------------------

if st.button("Predict Student Outcome"):

    prediction = model.predict(df)[0]
    result = encoder.inverse_transform([prediction])[0]

    st.subheader("Prediction Result")

    if result == "Dropout":
        st.error("⚠️ High Risk: Student may DROP OUT")

    elif result == "Enrolled":
        st.warning("📚 Student likely to remain ENROLLED")

    else:
        st.success("🎓 Student likely to GRADUATE")

    # Gemini Explanation
    st.subheader("🤖 AI Explanation")

    explanation = explain_prediction(input_data, result)

    st.markdown(explanation)