📉 Customer Churn Prediction App

A simple and interactive Streamlit web application that predicts whether a customer will churn based on their details.
This app uses a pre-trained machine learning model (churn_model.pkl) to generate predictions.

🚀 Features

✔️ User-friendly sidebar input form

✔️ Supports categorical + numerical inputs

✔️ Automatically preprocesses user inputs

✔️ Displays churn prediction with probability

✔️ Ready for deployment on Streamlit Cloud

📁 Project Structure
📂 customer-churn-app
│── app.py
│── churn_model.pkl
│── README.md
│── requirements.txt
│── (Optional) label_encoders/

🧠 How the App Works

The user enters customer details in the sidebar (gender, contract type, monthly charges, etc.)

Inputs are converted into model-friendly numeric format.

The model predicts:

1 → Customer will churn

0 → Customer will not churn

The app shows:

Predicted class

Probability of churn

▶️ Running the App Locally
1. Install Dependencies

Open a terminal and run:

pip install -r requirements.txt


If you don’t have a requirements file, create one with:

streamlit
pandas
numpy
scikit-learn
joblib

2. Run the Streamlit App
streamlit run app.py


The app will open in your browser at:

http://localhost:8501

🌐 Deploying to Streamlit Cloud
Step 1 — Push your project to GitHub

Your GitHub folder must contain:

app.py  
requirements.txt  
churn_model.pkl  
README.md  

Step 2 — Deploy

Go to: https://share.streamlit.io

Click New App

Select your GitHub repo

Select main branch

Select your file: app.py

Click Deploy

Done! 🎉
Your app will get a public URL you can share with anyone.

📷 Screenshots

## 📸 Application Screenshot

![App Screenshot](https://github.com/prathimabi30/Customer-Churn-Prediction-App/blob/main/screenshot.png?raw=true)


🛠 Technologies Used

Python

Streamlit

Scikit-learn

Pandas / NumPy

Joblib
