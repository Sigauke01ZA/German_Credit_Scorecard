import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

model = joblib.load(MODEL_DIR / "german_scorecard_model.pkl")
features = joblib.load(MODEL_DIR / "german_features.pkl")

st.set_page_config(page_title="German Credit Scorecard", layout="wide")
st.title("🏦 Classical Credit Scorecard")
st.markdown("This interactive scorecard calculates the credit score based on a WoE-transformed Logistic Regression model.")

st.sidebar.header("Applicant Profile (WoE Values)")
st.sidebar.markdown("*(Drag sliders to simulate different borrowers. Positive WoE = Good Risk, Negative WoE = Bad Risk)*")

# UPDATED: Defaults are now set to 1.0 (Safer applicant)
installment = st.sidebar.slider("Installment Commitment (WoE)", -1.5, 1.5, 1.0)
payment_plans = st.sidebar.slider("Other Payment Plans (WoE)", -1.5, 1.5, 1.0)
savings = st.sidebar.slider("Savings Status (WoE)", -1.5, 1.5, 1.0)
employment = st.sidebar.slider("Employment Length (WoE)", -1.5, 1.5, 1.0)
duration = st.sidebar.slider("Loan Duration (WoE)", -1.5, 1.5, 1.0)

input_dict = {feat: 0.0 for feat in features}

input_dict['installment_commitment'] = installment
input_dict['other_payment_plans'] = payment_plans
input_dict['savings_status'] = savings
input_dict['employment'] = employment
input_dict['duration'] = duration

input_df = pd.DataFrame([input_dict])[features]

pd_prob = model.predict_proba(input_df)[0][1]

# Scorecard Scaling
base_score = 600
base_odds = 50
pdo = 20
factor = pdo / np.log(2)
offset = base_score - (factor * np.log(base_odds))

log_odds = np.log(pd_prob / (1 - pd_prob))
score = offset - (factor * log_odds)
score = int(np.clip(score, 300, 850))

st.header("Scorecard Output")
col1, col2 = st.columns(2)
col1.metric("Probability of Default (PD)", f"{pd_prob:.2%}")
col2.metric("Final Credit Score", score)

# UPDATED: Thresholds adjusted for the German Credit Dataset distribution
if score > 600:
    st.success(f"**Decision: APPROVE.** Score of {score} is above the cut-off. The borrower is low risk.")
elif score > 520:
    st.warning(f"**Decision: REFER.** Score of {score} requires manual review.")
else:
    st.error(f"**Decision: DECLINE.** Score of {score} is below the cut-off. The borrower is high risk.")