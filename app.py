import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the model and data
model = pickle.load(open('Model.pkl', 'rb'))
car = pd.read_csv('Cleaned Quikr Car Dataset.csv')

def predict_price(company, car_model, year, fuel_type, kms_driven):
    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                           data=np.array([car_model, company, year, kms_driven, fuel_type]).reshape(1, 5)))
    return np.round(prediction[0], 2)

def render_input_form():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    st.subheader("Select the company:")
    company = st.selectbox("", ["Select Company"] + companies)

    st.subheader("Select the model:")
    car_model = st.selectbox("", car_models)

    st.subheader("Select Year of Purchase:")
    year = st.selectbox("", years)

    st.subheader("Select the Fuel Type:")
    fuel_type = st.selectbox("", fuel_types)

    st.subheader("Enter the Number of Kilometres that the car has travelled:")
    driven = st.text_input("", "")

    if st.button("Predict Price"):
        if company != "Select Company" and car_model and year and fuel_type and driven:
            prediction = predict_price(company, car_model, year, fuel_type, float(driven))
            st.success(f"Prediction: ₹{prediction}")
        else:
            st.warning("Please fill in all the details.")

def main():
    st.set_page_config(page_title='Car Price Predictor', page_icon=':car:', layout='centered')
    st.title('Welcome to Car Price Predictor')
    st.write('This app predicts the price of a car you want to sell. Try filling the details below:')

    # Call the function to render the input form
    render_input_form()

if __name__ == '__main__':
    main()

