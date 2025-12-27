import pickle 
import streamlit as st
import pandas as pd 
with open("final_model.pkl","rb") as f:
    final_model = pickle.load(f)


item = st.selectbox("Select Item", ["Sandwich", "Coffee ", "Cake"])
total_spent = st.number_input("Total Spent", min_value=0.0, step=0.01)
quantity = st.number_input("Quantity", min_value=1, step=1)
location = st.selectbox("Location", ["takeaway", "In-store"])
payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Digital Wallet"])
day = st.number_input("enter the day", min_value=1)

month = st.number_input("enter the month in numbers:",min_value=1)

year = st.number_input("enter the year:",min_value=2015)




if st.button("predict"):
    input_df = pd.DataFrame([{
        "Item": item,
        "Total Spent": total_spent,
        "Quantity": quantity,
        "Location": location,
        "Payment Method":payment_method,
        "day":day,
        "month":month,
        "year": year
        
    }])
    prediction = final_model.predict(input_df)
    print(prediction)
    st.write("prediction",prediction)

if st.button("Predict Price per Unit"):
    predicted_price = total_spent / quantity
    st.success(f"Predicted Price per Unit: {predicted_price}")

    
    
#host on streamlit cloud
#chatbot page to chat with your data(data we give it)
#kaggle.com (place where we can get csv files)
