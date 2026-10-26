# German_Credit_Scorecard
Traditional retail credit scorecard using WoE/IV variable selection, Logistic Regression, and PDO scaling (300-850).

# German Credit Scorecard

An end-to-end classical MRM (Model Risk Management) pipeline for building an **Application Credit Scorecard**. This project demonstrates the full model development lifecycle: data auditing, Weight of Evidence (WoE) transformation, Logistic Regression, PDO scaling (300–850), and SR 11-7 validation.

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-red.svg)

## Overview
Unlike machine learning black-box models, this project builds a transparent, interpretable scorecard that is widely used in banking for credit decisions. Using the standard German Credit dataset (1,000 records), the model predicts the probability of default (bad risk) and scales the log-odds into a points-based credit score. 

## Model Performance & Validation
The model was built using strict classical MRM standards, including a correlation matrix for multicollinearity, WoE/IV for feature selection, and a fair-lending exclusion policy (dropping protected characteristics like `personal_status` and `foreign_worker`).

> **Validation Rating: 9.2 / 10 (FIT FOR USE)** 
> 
> *   **Out-of-Sample Gini:** **0.6412** (Top of benchmark for German Credit)
> *   **KS Statistic:** **0.5460**
> *   **Hosmer-Lemeshow p-value:** **0.3784 (PASS)** (Excellent calibration)
> *   **Score PSI:** **0.0355** (Green zone, highly stable)

📄 **[Click here to read the full Model Validation Report](german_scorecard_validation_v1.md)**

## Interactive Dashboard
The Streamlit app allows users to input an applicant's profile and instantly see their credit score, probability of default, and the resulting approval decision.

**1. Approved Scenario (Strong Credit Profile)**
<img src="streamlit_approve.png" width="100%">

**2. Declined Scenario (High Risk Profile)**
<img src="streamlit_decline.png" width="100%">

## Key Analytical Steps

### 1. Data Audit & Winsorization
We checked for missing values and identified extreme outliers in continuous variables (like `credit_amount` and `duration`). To prevent these outliers from skewing the Logistic Regression coefficients, we applied Winsorization (capping extreme values at the 1st and 99th percentiles).

<img src="german_winsorization.png" width="100%">
*Figure 1: Winsorization of continuous variables to handle outliers.*

### 2. Feature Selection: Information Value (IV)
Categorical variables were binned and transformed using WoE. We filtered out features with an Information Value (IV) below 0.02, removing noise. 
*   **Strongest Feature:** `checking_status` (IV = 0.666).
*   **Excluded Features:** `job`, `own_telephone`, `num_dependents` (IV < 0.02).

📊 **[Click here to view the full IV Table](german_iv_table.csv)**

### 3. Logistic Regression & Coefficients
A Logistic Regression model was trained on the WoE-transformed data. As required for a valid scorecard, all coefficients are correctly signed (negative). A higher WoE (good borrower) reduces the log-odds of default.

<img src="german_coefficients.png" width="100%">
*Figure 2: Model Coefficients. All features correctly exhibit negative coefficients.*

### 4. PDO Scaling
The log-odds were converted into a credit score using Points to Double the Odds (PDO) scaling:
*   **Base Score:** 600
*   **Base Odds:** 50:1 Good to Bad
*   **PDO:** 20
*   **Score Range:** 300 to 850

---
**Author:** Raymond Sibanda | [LinkedIn](https://www.linkedin.com/in/raymond-sibanda-91850613b)
FRM | BSc Mathematics | BCom Honours Accounting
