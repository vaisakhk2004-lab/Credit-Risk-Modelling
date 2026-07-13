
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model pickle"
import joblib
model_data = joblib.load(MODEL_DIR/"model.joblib")
model=model_data['model']
features=model_data['features']
print(features)
scaler=model_data['scaler']
cols_to_scale=model_data['cols_to_scale']

def get_credit_rating(credit_score):
    if credit_score >= 800:
        return "🟢 Excellent"
    elif credit_score >= 740:
        return "🟢 Very Good"
    elif credit_score >= 670:
        return "🟡 Good"
    elif credit_score >= 580:
        return "🟠 Fair"
    else:
        return "🔴 Poor"
def calculate_credit_score(input_df):
    def_probability = model.predict_proba(input_df)[0][1]
    non_def_probability = 1-def_probability
    credit_score =300+non_def_probability*550
    return credit_score,def_probability
def create_df(number_of_open_accounts, credit_utilization_ratio, age,income,loan_amount,
       loan_tenure_months,delinquent_to_loan_ratio, dpd_to_delinquent_ratio,residence_type,
            loan_purpose,loan_type):
    columns =  {'number_of_open_accounts': number_of_open_accounts,
    'credit_utilization_ratio': credit_utilization_ratio,
    'age': age,
    'income':income,
    'loan_amount': loan_amount,
    'loan_tenure_months': loan_tenure_months,
    'delinquent_to_loan_ratio': delinquent_to_loan_ratio,
    'dpd_to_delinquent_ratio': dpd_to_delinquent_ratio,
    'residence_type_Owned': 1 if residence_type == 'Owned' else 0,
    'residence_type_Rented': 1 if residence_type == 'Rented' else 0,
    'loan_purpose_Education': 1 if loan_purpose =='Education' else 0,
    'loan_purpose_Auto': 1 if loan_purpose == 'Auto' else 0,
    'loan_purpose_Home': 1 if loan_purpose == 'Home' else 0,
    'loan_purpose_Personal': 1 if loan_purpose == 'Personal' else 0,
    'loan_to_income_ratio':loan_amount/income if income > 0 else 0,
    'loan_type_Unsecured': 1 if loan_type == 'Unsecured' else 0,
    'number_of_dependants':1,'years_at_current_address':1,'zipcode':1,'sanction_amount':1,'processing_fee':1,'gst':1,'net_disbursement':1,'principal_outstanding':1,'bank_balance_at_application':1,
        'number_of_closed_accounts':1,'enquiry_count':1
    }
    df=pd.DataFrame([columns])
    df[cols_to_scale]=scaler.transform(df[cols_to_scale])
    df=df[features]
    return df
def predict(number_of_open_accounts, credit_utilization_ratio, age,income,loan_amount,
       loan_tenure_months,delinquent_to_loan_ratio, dpd_to_delinquent_ratio,residence_type,
            loan_purpose,loan_type):
    input_df=create_df(number_of_open_accounts, credit_utilization_ratio, age,income,loan_amount,
       loan_tenure_months,delinquent_to_loan_ratio, dpd_to_delinquent_ratio,residence_type,
            loan_purpose,loan_type)
    credit_score,def_probability=calculate_credit_score(input_df)
    rating=get_credit_rating(credit_score)
    return credit_score,rating,def_probability


