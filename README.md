student-sucess-prediction
🎓 AI Student Success Prediction System
An AI-powered system that predicts whether a university student is likely to Graduate, Stay Enrolled, or Drop Out using machine learning and provides intelligent explanations using Google Gemini API.

This project helps universities identify students at risk early so they can provide academic or financial support and improve student retention.

📌 Project Overview
Student dropout is a major challenge for universities worldwide. Many students leave their studies due to academic difficulties or financial problems.

This project uses machine learning and generative AI to analyze student data and predict academic outcomes. The system also generates human-readable explanations and recommendations to help university administrators support students effectively.

🚀 Features
📊 Predicts student outcome:

Graduate
Enrolled
Dropout
🤖 AI explanation using Google Gemini API

📈 Machine Learning model trained using XGBoost

🖥 Interactive dashboard built with Streamlit

🧠 Provides insights about academic and financial risk factors

🛠 Technologies Used
Python
Scikit-learn
XGBoost
Streamlit
Pandas
Joblib
Google Gemini API
📂 Project Structure
predictive_customer_outreach/
│
├── app/
│   └── streamlit_app.py        # Streamlit dashboard application
│
├── model/
│   ├── student_success_xgb_model.pkl
│   ├── label_encoder.pkl
│   └── feature_columns.pkl
│
├── data/
│   └── data.csv                # Dataset used for training
│
├── notebook/
│   └── student_success_prediction.ipynb   # Model training notebook
│
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files ignored by Git
└── README.md                   # Project documentation
⚙️ How the System Works
User enters student information in the dashboard
The trained machine learning model analyzes the input data
The model predicts the student's academic outcome
Gemini AI generates an explanation of the prediction
The system provides recommendations for university support
📊 Input Features Used
The model analyzes several academic and financial indicators:

Age at enrollment
Admission grade
Previous qualification grade
1st semester units enrolled
1st semester units approved
2nd semester units approved
Debtor status
Scholarship holder
Tuition fees up to date
Gender
These features help the model understand student academic performance and financial risk factors.

🧠 Machine Learning Model
The prediction model is trained using XGBoost, a powerful gradient boosting algorithm widely used for structured datasets.

The model is saved as a .pkl file and loaded into the Streamlit application for real-time predictions.

🤖 AI Explanation with Gemini
The system integrates Google Gemini API to generate:

Simple explanation of predictions
Key factors influencing student outcomes
Practical recommendations for universities
This makes the system more interpretable and useful for decision-makers.

▶️ Running the Project
1. Clone the repository
git clone https://github.com/vivekkumar326/ai-student-sucess-prediction
2. Navigate to the project
cd ai-student-success-prediction
3. Create virtual environment
python3 -m venv venv
source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Run the Streamlit dashboard
streamlit run app/streamlit_app.py
🎯 Project Impact
This system can help universities:

Detect students at risk of dropping out
Improve student retention
Provide early academic intervention
Support data-driven educational decisions
📌 Future Improvements
Add feature importance visualization
Implement SHAP explainability
Deploy the system as a cloud-based web application
Integrate with university student information systems
👨‍💻 Author
Vivek Kumar

Machine Learning Project – Student Success Prediction System
