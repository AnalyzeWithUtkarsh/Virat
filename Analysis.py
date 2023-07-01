import streamlit as st
import pandas as pd

data = pd.read_csv('D:\\Kaggle Datasets\\Virat Kohli Analysis\\Virat-Kohli-International-Cricket-Centuries.csv')
data['Stadium Name'] = data['Venue'].str.split(",").str.get(0)
data['City'] = data['Venue'].str.split(',').str.get(1)
centuries = data[['No.', 'Runs', 'Against', 'Position', 'Innings', 'Stadium Name', 'City', 'Ground', 'Date', 'Result']]
centuries['Day'] = centuries['Date'].str.split('-').str.get(0)
centuries['Month'] = centuries['Date'].str.split('-').str.get(1)
centuries['Year'] = centuries['Date'].str.split('-').str.get(2)
centuries = centuries[['No.', 'Runs', 'Against', 'Position', 'Innings', 'Stadium Name', 'City', 'Ground', 'Day', 'Month', 'Year', 'Result']]

user_input = st.sidebar.selectbox(
    'Select an option',
    ['About Virat Kohli', 'Dashboard', 'Centuries Analysis']
)

if user_input == 'Dashboard':
    st.header('Total Number of Centuries Scored')
    total = centuries['No.'].count()
    st.header(total)



