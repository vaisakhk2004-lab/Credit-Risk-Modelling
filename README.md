# Credit Risk Modelling System

## 1. Overview

The Credit Risk Modelling System is a machine learning application that predicts a borrower's probability of default, calculates a credit score, and assigns a corresponding risk rating. It is deployed as an interactive Streamlit web application that allows users to input applicant details and instantly receive a risk assessment.

## 2. Problem Statement

Financial institutions need a reliable way to assess the creditworthiness of loan applicants before approval. This project addresses that need by:

- Predicting the **probability of default** for a given applicant
- Translating that probability into a **credit score**

## 3. Target Variable

| Property | Details |
|---|---|
| **Column name** | `default` |
| **Classes** | `0` — No Default, `1` — Default |

## 4. Features Used

The model was trained on the following features, including several engineered ratio features:

- `number_of_open_accounts`
- `credit_utilization_ratio`
- `age`
- `loan_tenure_months`
- `loan_to_income_ratio`
- `delinquent_to_loan_ratio`
- `loan_purpose`
- `loan_type`
- `resident_type`

Additional derived/engineered features were created to capture ratio-based risk signals (e.g. loan-to-income, delinquency-to-loan ratios) rather than relying solely on raw input values.

## 5. Data Preprocessing

The following preprocessing steps were applied to the raw dataset:

- ✅ Missing value handling
- ✅ Duplicate removal
- ✅ Outlier treatment
- ✅ One-Hot Encoding
- ✅ Feature scaling
- ✅ SMOTETomek for class imbalance correction
- ✅ Weight of Evidence (WOE) and Information Value (IV) for feature selection/binning
- ✅ Variance Inflation Factor (VIF) for multicollinearity checks

## 6. Model Training

Two models were trained and compared:

| Model | Notes |
|---|---|
| Logistic Regression | Baseline model |
| **XGBoost Classifier** | **Best performing — selected as the final model** |

The **XGBoost Classifier** outperformed Logistic Regression and was chosen as the final production model for predicting default probability, credit score, and risk rating.

## 7. Streamlit Application

The Streamlit app provides an interactive UI where users can input the following applicant details:

- Number of Open Accounts
- Average DPD (Days Past Due)
- Delinquent Ratio
- Credit Utilization Ratio
- Loan Amount
- Age
- Income
- Residence Type
- Loan Tenure (Months)
- Loan Type
- Loan Purpose

Based on these inputs, the app outputs:
- Probability of default
- Calculated credit score
- Credit score rating

## 8. Tech Stack

- **Language:** Python
- **ML Libraries:** scikit-learn, XGBoost, imbalanced-learn (SMOTETomek)
- **Data Handling:** pandas, numpy
- **Web App:** Streamlit

## 9. Project Structure

```
credit-risk-modelling/
├── main.py             # Streamlit application
├── prediction.py                 
├── requirements.txt       # Project dependencies
└── model pickle           # Saved model, scaler, columns to scale and features
```

## 10. How to Run

1. Clone the repository
   ```bash
   git clone <https://github.com/vaisakhk2004-lab/Credit-Risk-Modelling.git>
   cd credit-risk-modelling
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app
   ```bash
   streamlit run main.py
   ```
