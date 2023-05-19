# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date, timedelta
import numpy as np

def main():
    st.title("Cryptocurrency Price Prediction")
    with open('model_pickle1', 'rb') as f:
        model1 = pickle.load(f)
    with open('model_pickle2', 'rb') as f:
        model2 = pickle.load(f)
    with open('model_pickle3', 'rb') as f:
        model3 = pickle.load(f)
    days=["10", "20", "30"]
    option = st.selectbox('How many days you like to predict?', days)
    st.write('You selected:', option)
    form = st.form(key='my-form')
    submit = form.form_submit_button('Submit')
    if submit:
        if option == "10":
            prediction1 = model1.predict()
            forecast1 = prediction1.forecast
            st.write(forecast1)
            y_pred = forecast1['Close']
            fig, ax = plt.subplots()
            ax.plot(y_pred, label="Predicted")
            ax.legend()
            plt.xticks(rotation=90)
            plt.title("Forecast data")
            plt.xlabel("Date")
            plt.ylabel("Closing price")
            st.pyplot(fig)
        elif option == "20":
            prediction2 = model2.predict()
            forecast2 = prediction2.forecast
            st.write(forecast2)
            y_pred = forecast2['Close']
            fig, ax = plt.subplots()
            ax.plot(y_pred, label="Predicted")
            ax.legend()
            plt.xticks(rotation=90)
            plt.title("Forecast data")
            plt.xlabel("Date")
            plt.ylabel("Closing price")
            st.pyplot(fig)
        elif option == "30":
            prediction3 = model3.predict()
            forecast3 = prediction3.forecast
            st.write(forecast3)
            y_pred = forecast3['Close']
            fig, ax = plt.subplots()
            ax.plot(y_pred, label="Predicted")
            ax.legend()
            plt.xticks(rotation=90)
            plt.title("Forecast data")
            plt.xlabel("Date")
            plt.ylabel("Closing price")
            st.pyplot(fig)
        else:
            st.write('Not valid')
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
