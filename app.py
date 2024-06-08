import streamlit as st
import joblib
import pandas as pd

import joblib
def predict(data):
    clf=joblib.load('rf.sav')
    return clf.predict(data)

def main():
    # Title of the web app
    st.title('Customer Churn Prediction')

    # Add description and instructions
    st.write('Enter the details.')

    # Input fields for the features
    gender = st.selectbox('Gender:', ['male', 'female'])
    seniorcitizen= st.selectbox('Customer is a senior citizen:', [0, 1])
    partner= st.selectbox('Customer has a partner:', ['yes', 'no'])
    dependents = st.selectbox('Customer has  dependents:', ['yes', 'no'])
    phoneservice = st.selectbox('Customer has phoneservice:', ['yes', 'no'])
    multiplelines = st.selectbox('Customer has multiplelines:', ['yes', 'no', 'no_phone_service'])
    internetservice= st.selectbox('Customer has internetservice:', ['dsl', 'no', 'fiber_optic'])
    onlinesecurity= st.selectbox('Customer has onlinesecurity:', ['yes', 'no', 'no_internet_service'])
    onlinebackup = st.selectbox('Customer has onlinebackup:', ['yes', 'no', 'no_internet_service'])
    deviceprotection = st.selectbox('Customer has deviceprotection:', ['yes', 'no', 'no_internet_service'])
    techsupport = st.selectbox('Customer has techsupport:', ['yes', 'no', 'no_internet_service'])
    streamingtv = st.selectbox('Customer has streamingtv:', ['yes', 'no', 'no_internet_service'])
    streamingmovies = st.selectbox('Customer has streamingmovies:', ['yes', 'no', 'no_internet_service'])
    contract= st.selectbox('Customer has a contract:', ['month-to-month', 'one_year', 'two_year'])
    paperlessbilling = st.selectbox(' Customer has a paperlessbilling:', ['yes', 'no'])
    paymentmethod= st.selectbox('Payment Option:', ['bank_transfer_(automatic)', 'credit_card_(automatic)', 'electronic_check' ,'mailed_check'])
    tenure = st.number_input('Number of months the customer has been with the current telco provider :', min_value=0, max_value=240, value=0)
    monthlycharges= st.number_input('Monthly charges :', min_value=0, max_value=240, value=0)
    totalcharges = tenure*monthlycharges
    
    # Convert the input data into a dictionary
    input_data={
                "gender":gender,
                "seniorcitizen": seniorcitizen,
                "partner": partner,
                "dependents": dependents,
                "phoneservice": phoneservice,
                "multiplelines": multiplelines,
                "internetservice": internetservice,
                "onlinesecurity": onlinesecurity,
                "onlinebackup": onlinebackup,
                "deviceprotection": deviceprotection,
                "techsupport": techsupport,
                "streamingtv": streamingtv,
                "streamingmovies": streamingmovies,
                "contract": contract,
                "paperlessbilling": paperlessbilling,
                "paymentmethod": paymentmethod,
                "tenure": tenure,
                "monthlycharges": monthlycharges,
                "totalcharges": totalcharges
            }

    # Convert the input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict churn
    if st.button('Predict Churn'):
        churn = predict(input_df)
        churn_probability = 'Yes' if churn[0] == 1 else 'No'
        st.write(f'The predicted value for churn is: {churn_probability}')

if __name__ == '__main__':
    main()