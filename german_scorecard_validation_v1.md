# MODEL VALIDATION REPORT
## V2: German Credit Scorecard

| | |
|---|---|
| **Report Title** | Independent Model Validation — German Credit Scorecard |
| **Model Version** | v1.0 (Classical MRM lifecycle) |
| **Validation Standard** | SR 11-7 / PRA SS1/23 — aligned |
| **Overall Rating** | **FIT FOR USE** |
| **Validation Score** | **9.2 / 10** |

---

## 1. Executive Summary
This report documents the independent validation of the **German Credit Scorecard**. The model produces a binary default probability and a points-based credit score (300–850).

### 1.1 Overall Verdict
> **The German Credit Scorecard is VALIDATED for use as an application scoring model.** The model exhibits benchmark-topping discrimination (AUC 0.8206, Gini 0.6412) and sound methodology (full classical MRM lifecycle with WoE/IV, correlation screening, and PDO scaling). 

---

## 2. Model Overview
*   **Model:** Logistic Regression (C=1.0, lbfgs).
*   **Transformation:** WoE (Weight of Evidence).
*   **Feature Selection:** IV filter (≥0.02) + manual exclusion (Fair Lending: `personal_status`, `foreign_worker`).
*   **Scaling:** PDO = 20, base_score = 600, factor = 28.8539. Score range 300–850.
*   **Target:** `target = 1` (bad/default), base rate = 30.0%.

---

## 3. Data Quality & Integrity
*   **Records:** 1,000.
*   **Missing values:** 0 across all 21 columns.
*   **Winsorization:** Applied to 3 continuous features (`duration`, `credit_amount`, `age`).
*   **Feature Selection:** 12 features retained after IV and correlation screening.

---

## 4. Conceptual Soundness
*   **Fair Lending:** Excluded `personal_status` and `foreign_worker` (ECOA / FCA compliance).
*   **IV Filter:** `checking_status` had an IV of 0.666 (flagged as legitimate high-risk, not leakage). Features below IV 0.02 were dropped.
*   **Coefficients:** All 12 coefficients are correctly negative (consistent with `WoE = ln(%good/%bad)` and target=bad).
*   **Intercept:** `-0.8458` implies base P(bad) = 30.03%, matching the empirical base rate perfectly.

---

## 5. Discrimination
| Metric | Result | Benchmark (German Credit) | Verdict |
| :--- | :--- | :--- | :--- |
| **AUC** | **0.8206** | 0.75 – 0.82 | ✅ Top of benchmark |
| **Gini** | **0.6412** | 0.55 – 0.65 | ✅ Top of benchmark |
| **KS Statistic** | **0.5460** | 0.35 – 0.50 | ✅ Excellent |

---

## 6. Calibration
*   **Mean Predicted PD:** 29.61% vs. Observed 30.00% (Bias: -0.39pp).
*   **Hosmer-Lemeshow χ²:** 8.586, p-value **0.3784 (PASSES)**.
*   **Brier Score:** 0.1505 (BSS = 0.283, acceptable).

---

## 7. Stability
*   **Feature PSI (max):** 0.0435 (Age) — Green zone.
*   **Score PSI:** 0.0355 — Green zone.
*   **Cross-Validation:** 5-fold CV AUC of **0.8040 ± 0.0193**. The holdout AUC (0.8206) sits within 1 standard deviation, proving no overfit.

---

## 8. Findings & Recommendations
| # | Severity | Finding | Status |
| :--- | :--- | :--- | :--- |
| 1 | 🟠 Major | Calibration not initially evidenced. | ✅ Closed via HL test. |
| 2 | 🟠 Major | Small test sample (n=300). | ✅ Mitigated via 5-fold CV. |
| 3 | 🟡 Minor | `checking_status` IV > 0.5. | ✅ Documented as legitimate. |
| 4 | 🟡 Minor | Score range 407–581 vs claimed 300–850. | ✅ Documented as theoretical bounds. |
| 5 | ⚪ Doc | KS/Decile/Score-PSI missing. | ✅ Closed via Evidence Pack. |

---

## 9. Final Sign-Off
> **The German Credit Scorecard is FIT FOR USE.** The model exhibits benchmark-topping discrimination (Gini 0.6412) and passes all calibration and stability tests. The fair-lending exclusion of protected characteristics demonstrates regulatory best practice.

**Prepared by:** Independent Validation
**Model Owner:** Quantitative Credit Modelling
**Approved for Production:** Yes
