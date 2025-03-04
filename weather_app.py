import streamlit as st
import pandas as pd
import pickle

# Header Of Application
st.subheader("Weather Forecasting Application")
# import pickle File
with open("df.pkl","rb") as file:
    df = pickle.load(file)
with open("pipe.pkl","rb") as file:
    pipe = pickle.load(file)
with open("Columns.pkl","rb") as file:
    columns = pickle.load(file)

# User input
location = st.selectbox("Location",df['Location'].unique())
Mintemp = st.number_input("Minimum_Temperature",format="%.2f")
Maxtemp = st.number_input("Maximum_Temperature",format="%.2f")
Rainfall = st.number_input("RainFall",format="%.2f")
windGustDire = st.selectbox("WindGustDirection",df['WindGustDir'].unique())
windGustSpeed = st.number_input("Wind_Speed",format="%.2f")
windDir9am = st.selectbox("WindDirection at 9:00 AM",df['WindDir9am'].unique())
windDir3pm = st.selectbox("WindDirection at 3:00 PM",df['WindDir3pm'].unique())
windspeed9am = st.number_input("WindSpeed at 9:00 AM",format="%.2f")
windspeed3pm = st.number_input("WindSpeed at 3:00 PM",format="%.2f")
humidity9am = st.number_input("Humidity at 9:00 AM",format="%.2f")
humidity3pm = st.number_input("Humidity at 3:00 PM",format="%.2f")
pressure9am = st.number_input("Pressure at 9:00 AM",format="%.2f")
pressure3pm = st.number_input("Pressure at 9:00 PM",format="%.2f")
raintoday = st.selectbox("RainToday",['Yes','No'])

 
if st.button("Predict"):

    # convert Raintoday to Numeric Format
    if raintoday == "Yes":
        raintoday=1
    else:
        raintoday=0

    # Convert all Numeric Value to Float Value


    predict_data = pd.DataFrame([[location, Mintemp, Maxtemp, Rainfall, windGustDire, windGustSpeed, windDir9am, windDir3pm, 
                                windspeed9am, windspeed3pm, humidity9am, humidity3pm, pressure9am, pressure3pm, raintoday]],
                                columns=['Location','MinTemp','MaxTemp','Rainfall','WindGustDir','WindGustSpeed','WindDir9am',
                                'WindDir3pm','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am',
                                'Pressure3pm','RainToday'])
    print(predict_data)

    # Convert all Numeric Value to Float Value
    num_features = ['MinTemp','MaxTemp','Rainfall','WindGustSpeed','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm']
    for num in num_features:
        predict_data[num]=predict_data[num].astype(float)
    
    # convert all Categorical Value to String Format
    cat_features = ['Location','WindGustDir','WindDir9am','WindDir3pm','RainToday']
    for col in cat_features:
        predict_data[col]=predict_data[col].astype(str)

try:
    if (location and Mintemp and Maxtemp and Rainfall and windGustDire and windGustSpeed and 
        windDir9am and windDir3pm and windspeed9am and windspeed3pm and humidity9am and 
        humidity3pm and pressure9am and pressure3pm and raintoday):
        
        # Make the prediction
        predict = pipe.predict(predict_data)
        print(predict)

        # Display the prediction result
        if predict == 'YES':
            st.markdown("Prediction: Rain will come tomorrow.")
        else:
            st.markdown("Prediction: No rain tomorrow.")

    else:
        st.warning("Please provide all the required data to make a prediction.")

except Exception as e:
    st.error(f"Error during prediction: {e}")

