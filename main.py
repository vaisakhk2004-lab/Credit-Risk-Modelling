import streamlit as st
from prediction import predict


st.set_page_config(
    page_title="Credit Risk Modelling",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Credit Risk Modelling")
st.write(
    "Predict whether an applicant is in **Low**, **Medium**, or **High** credit risk."
)

st.divider()
col1,col2,col3 = st.columns(3)
with col1:
    number_of_open_accounts = st.number_input(
        "Number of Open Accounts",
        min_value=1,
        max_value=2


    )

    credit_utilization_ratio = st.number_input(
        "Credit Utilization Ratio",
        1.0,
        100.0,

    )
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )
    loan_tenure_months = st.number_input("Loan Tenure (Months)",
                                         min_value=3,
                                         max_value=100
                                         )




with col2:
    dpd_to_delinquent_ratio = st.number_input(
        "Avg DPD",
        1.0,
        100.0,
        2.0
    )

    loan_amount = st.number_input("Loan Amount",
                                         min_value=1000,
                                         max_value=5000000
                                         )
    income = st.number_input("Income",
                                  min_value=5000,
                                  max_value=1200000
                                  )
    loan_type = st.selectbox(
        "Loan Type",
        ["Secured", "Unsecured"]
    )

loan_to_income_ratio = (loan_amount/ income if income > 0 else 0)


with col3:
   delinquent_to_loan_ratio= st.number_input("Delinquent  Ratio",
        1,
        100,

    )
   st.write('Loan To Income Ratio')
   st.write(loan_to_income_ratio)


   residence_type= st.selectbox(
        "Residence Type",
        ["Owned", "Rented"]
    )
   loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Education", "Home", "Personal"]
    )


st.divider()


if st.button("Predict Credit Risk"):

    credit_score,rating,def_probability=predict(number_of_open_accounts, credit_utilization_ratio, age, income, loan_amount,
        loan_tenure_months, delinquent_to_loan_ratio, dpd_to_delinquent_ratio, residence_type,
        loan_purpose, loan_type)
    st.success(f"Credit Score: {round(credit_score)}")
    st.write(f"Chance Of  Getting Defaulted : {round(def_probability * 100)}%")
    st.metric('Rating',rating)

