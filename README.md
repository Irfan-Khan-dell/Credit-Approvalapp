# Credit-Approval-app
# 🏦 AI-Powered Credit Risk Dashboard

### 🚀 Live Demo
**[Click Here to Try the App](https://share.streamlit.io/your-username/credit-approval-app)** *(Replace this link after you deploy!)*

---

### 📖 Overview
This is a Machine Learning web application designed to automate the credit approval process. It helps banks and financial institutions assess the risk level of loan applicants in real-time.

By analyzing key financial factors—such as CIBIL score, recent delinquencies, and credit history—the AI model predicts the likelihood of default and categorizes applicants into risk buckets (**P1** to **P4**).

### ✨ Key Features
* **Real-Time Prediction:** Instant credit decision (Approved/Rejected) based on user input.
* **Risk Classification:** Categorizes users into 4 risk levels:
    * **P1:** Low Risk (High Approval Chance)
    * **P2:** Medium Risk
    * **P3:** High Risk
    * **P4:** Very High Risk (likely Reject)
* **Confidence Score:** Displays the probability percentage of the prediction.
* **Interactive Interface:** Built with **Streamlit** for a seamless user experience.

### 🛠️ Tech Stack
* **Frontend:** Streamlit (Python Web Framework)
* **Backend:** Python
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Data Processing:** Pandas, NumPy

### 📂 Project Structure
```text
/Credit-Risk-App
│
├── app.py                    # Main Streamlit application
├── credit_model_simple.pkl   # Pre-trained ML model (Random Forest)
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
