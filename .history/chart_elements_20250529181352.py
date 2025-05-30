import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Streamlit Charts Demo")

#Generate Sample Data

chart_data = pd.DataFrame(
    np.random.randn(20,3)
    
)
