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
The Streamlit app allows users to input an applicant's profile and instantly see their credit score, probability of default, and the underlying points contribution. 

*(Note: Update the image name below if your screenshot is named differently)*
<img src="streamlit_german.png" width="100%">

## Key Analytical Steps

### 1. Data Audit & Feature Selection
We checked for missing values, winsorized continuous outliers (e.g., capping `credit_amount`), and applied a correlation matrix to drop highly collinear features. We also enforced fair-lending compliance by excluding gender and nationality proxies.

### 2. Weight of Evidence (WoE) & Information Value (IV)
Categorical variables were binned and transformed using WoE to create a monotonic relationship with the target. We filtered out features with an Information Value (IV) below 0.02.
*   **Strongest Feature:** `checking_status` (IV = 0.666).
*   **Excluded Features:** `job`, `own_telephone`, `num_dependents` (IV < 0.02).

### 3. Logistic Regression & PDO Scaling
A Logistic Regression model was trained on the WoE-transformed data. All coefficients were correctly signed (negative). The log-odds were then converted into a credit score using PDO scaling:
*   **Base Score:** 600
*   **Base Odds:** 50:1 Good to Bad
*   **PDO (Points to Double the Odds):** 20
*   **Score Range:** 300 to 850

---
**Author:** Raymond Sibanda | [LinkedIn](https://www.linkedin.com/in/raymond-sibanda-91850613b) |
FRM | BSc Mathematics | BCom Honors Accounting
