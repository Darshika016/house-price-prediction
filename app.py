import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('C:\\Users\\DARSHIKA\\Desktop\\Darshika Hingu Portfolio\\House Price Predition using Machine Learning\\House_Price_Prediction.pkl', 'rb'))


#Header
st.header("Bengaluru House Price Prediction")

#load the dataset
data = pd.read_csv(r'C:\Users\DARSHIKA\Desktop\Darshika Hingu Portfolio\House Price Predition using Machine Learning\Final_cleaned_data.csv')

#input text
loc =st.selectbox("Choose the Location", data['location'].unique())
sqft = st.number_input('Enter total square Feet')
bedrooms = st.number_input("Enter the number of bedrooms")
bathrooms = st.number_input("Enter the number of bathrooms")
balconies = st.number_input("Enter the number of balconies")


input = pd.DataFrame([[loc, sqft, bedrooms, bathrooms, balconies]], columns = ['location','total_sqft','bedroom','bath','balcony'])

if st.button("PREDICT PRICE"):
    output = model.predict(input)
    out_str = "Price of house is " + str(output[0]*100000)
    st.success(out_str)