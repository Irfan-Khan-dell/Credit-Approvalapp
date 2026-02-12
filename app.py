import streamlit as st
import pandas as pd
import joblib

# 1. Load the Model
model = joblib.load('credit_model_simple.pkl')

# 2. Page Configuration
st.set_page_config(page_title="Credit Risk AI", layout="centered")

st.title("🏦 AI Powered Credit Risk Dashboard")
st.write("Enter applicant details to predict credit risk (P1 = Low Risk, P4 = High Risk).")

# 3. Create Input Fields for the Top 10 Features
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("CIBIL Score (300-900)", min_value=300, max_value=900, value=750)
    age_oldest_tl = st.number_input("Age of Oldest Trade Line (Months)", min_value=0, value=24)
    enq_l3m = st.number_input("Enquiries in Last 3 Months", min_value=0, value=0)
    time_recent_enq = st.number_input("Time Since Recent Enquiry (Months)", min_value=0, value=1)
    enq_l6m = st.number_input("Enquiries in Last 6 Months", min_value=0, value=0)

with col2:
    num_std_12mts = st.number_input("Standard Payments (Last 12m)", min_value=0, value=12)
    num_std = st.number_input("Standard Payments (Total)", min_value=0, value=24)
    recent_deliq = st.number_input("Recent Delinquency Level", min_value=0, value=0)
    max_recent_deliq = st.number_input("Max Recent Delinquency Level", min_value=0, value=0)
    num_times_deliq = st.number_input("Number of Times Delinquent", min_value=0, value=0)

# 4. Predict Button
if st.button("Assess Credit Risk"):
    # Create a DataFrame from inputs
    input_data = pd.DataFrame([[
        credit_score, age_oldest_tl, enq_l3m, time_recent_enq, enq_l6m,
        num_std_12mts, num_std, recent_deliq, max_recent_deliq, num_times_deliq
    ]], columns=['Credit_Score', 'Age_Oldest_TL', 'enq_L3m', 'time_since_recent_enq', 
                 'enq_L6m', 'num_std_12mts', 'num_std', 'recent_level_of_deliq', 
                 'max_recent_level_of_deliq', 'num_times_delinquent'])

    # Get Prediction
    prediction = model.predict(input_data)[0]
    
    # Get Probabilities (Confidence Score)
    probs = model.predict_proba(input_data)
    confidence = max(probs[0]) * 100

    # 5. Display Result
    st.markdown("---")
    st.subheader("Risk Assessment Result:")
    
    if prediction == 'P1':
        st.success(f"✅ Approved (Low Risk) - Confidence: {confidence:.2f}%")
        st.write("Customer has a strong credit history and high repayment probability.")
    elif prediction == 'P2':
        st.info(f"🔹 Review Required (Medium-Low Risk) - Confidence: {confidence:.2f}%")
    elif prediction == 'P3':
        st.warning(f"⚠️ High Risk (Warning) - Confidence: {confidence:.2f}%")
    else:
        st.error(f"❌ Rejected (Very High Risk) - Confidence: {confidence:.2f}%")
        st.write("Applicant shows signs of default behavior. Manual review recommended.")