# Car Price Predictor

Car Price Predictor is a web application that predicts the price of a car based on various features such as company, model, year of purchase, fuel type, and kilometers driven.

## Getting Started

### Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage
Make sure you have the trained model (Model.pkl) and the car feature dataset (Cleaned Quikr Car Dataset.csv) in the project directory.

Run the Streamlit app:

```bash
streamlit run app.py
```

## Features
1. Interactive web interface for predicting car prices.
2. Easy selection of various car features using dropdowns and input fields.
3. Real-time prediction based on user input.
4. Predicted price is displayed in Indian Rupees (₹).
5. Validation checks to ensure all required details are provided before prediction.

