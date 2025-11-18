import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("churn_model.pkl")
model_features = model.feature_names_in_

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide",
)

# -------------------------------
# Title
# -------------------------------
st.markdown("""
<h1 style='text-align:center; color:#4A90E2;'>
    📉 Customer Churn Prediction App
</h1>
<p style='text-align:center; font-size:18px;'>
    Predict whether a customer will churn based on their profile.
</p>
<br>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar Inputs (Grouped)
# -------------------------------
st.sidebar.header("Customer Input Features")
st.sidebar.markdown("Fill the customer details below:")

# Mappings for categorical features
gender_map = {"Male": 0, "Female": 1}
yes_no_map = {"No": 0, "Yes": 1}
internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}

# Example options for categorical fields
city_options = ["Proddatur", "Hyderabad", "Bangalore"]
country_options = ["India", "USA", "UK"]
state_options = ["Andhra Pradesh", "Telangana", "Karnataka"]
payment_options = ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]

user_input = {}

# --- Customer Info ---
st.sidebar.subheader("Customer Info")
for feature in ["CustomerID", "Count", "Country", "State", "City", "Zip Code", "Lat Long", "Latitude", "Longitude"]:
    if feature in ["City"]:
        user_input[feature] = city_options.index(st.sidebar.selectbox(feature, city_options, index=0))
    elif feature in ["Country"]:
        user_input[feature] = country_options.index(st.sidebar.selectbox(feature, country_options, index=0))
    elif feature in ["State"]:
        user_input[feature] = state_options.index(st.sidebar.selectbox(feature, state_options, index=0))
    elif feature in ["CustomerID", "Zip Code"]:
        user_input[feature] = st.sidebar.text_input(feature, value="310")
    else:
        user_input[feature] = st.sidebar.number_input(feature, value=0)

# --- Service Details ---
st.sidebar.subheader("Service Details")
for feature in ["Phone Service", "Multiple Lines", "Internet Service", "Online Security", "Online Backup",
                "Device Protection", "Tech Support", "Streaming TV", "Streaming Movies"]:
    if feature == "Internet Service":
        user_input[feature] = internet_map[st.sidebar.selectbox(feature, ["DSL", "Fiber optic", "No"], index=0)]
    else:
        user_input[feature] = yes_no_map[st.sidebar.selectbox(feature, ["Yes", "No"], index=1)]

# --- Contract & Billing ---
st.sidebar.subheader("Contract & Billing")
for feature in ["Contract", "Paperless Billing", "Payment Method", "Monthly Charges", "Total Charges",
                "Tenure Months", "Gender", "Partner", "Dependents", "Senior Citizen"]:
    if feature == "Contract":
        user_input[feature] = contract_map[st.sidebar.selectbox(feature, ["Month-to-month", "One year", "Two year"], index=0)]
    elif feature == "Payment Method":
        user_input[feature] = payment_options.index(st.sidebar.selectbox(feature, payment_options, index=0))
    elif feature in ["Gender"]:
        user_input[feature] = gender_map[st.sidebar.selectbox(feature, ["Male", "Female"], index=0)]
    else:
        user_input[feature] = st.sidebar.number_input(feature, value=50)

# -------------------------------
# Prepare Input Data
# -------------------------------
input_data = pd.DataFrame([user_input], columns=model_features)

# -------------------------------
# Predict Churn
# -------------------------------
if st.button("Predict Churn"):
    try:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            st.error(f"❌ Customer is likely to CHURN! (Probability: {probability*100:.1f}%)")
        else:
            st.success(f"✅ Customer will NOT Churn. (Probability: {(1-probability)*100:.1f}%)")

        st.subheader("Churn Probability")
        st.progress(int(probability*100))

    except ValueError as e:
        st.error(f"Error in prediction: {e}")
