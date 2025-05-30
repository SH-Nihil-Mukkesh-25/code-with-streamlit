import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Streamlit Charts Demo")

#Generate Sample Data

chart_data = pd.DataFrame (
    np.random.randn(20,3),
    columns=['A','B','C']
)

# Area Chart Section
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar Chart Section
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Line Chart Section
st.subheader("Line Chart")
st.line_chart(chart_data)

# Scatter Plot Section (added)
st.subheader("Scatter Plot")
