import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('data1.csv')


st.title('Zomato Data Analysis')

st.sidebar.title("Please Select The Options")

restaurant_type = st.sidebar.selectbox('Select Restaurant Type', df['listed_in(type)'].unique())

filtered_data = df[df['listed_in(type)'] == restaurant_type]

st.subheader(f"Displaying data for '{restaurant_type}' restaurants:")
st.write(filtered_data)

st.sidebar.subheader("Additional Filters")

online_order = st.sidebar.radio('Filter by Online Order', ('All', 'Yes', 'No'))
if online_order != 'All':
    filtered_data = filtered_data[filtered_data['online_order'] == online_order]

table_booking = st.sidebar.radio('Filter by Table Booking', ('All', 'Yes', 'No'))
if table_booking != 'All':
    filtered_data = filtered_data[filtered_data['book_table'] == table_booking]

st.subheader(f"Filtered Data ({online_order} Online Order, {table_booking} Table Booking)")
st.write(filtered_data)    




