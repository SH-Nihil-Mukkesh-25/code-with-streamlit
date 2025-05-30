import streamlit as st
import pandas as pd

st.title("Streamlit Elements Demo")

# Dataframe Section

st.subheader("Dataframe")

df = pd.DataFrame({
    'Name' : ['Dustin' , 'Mike' , 'Lucas' , 'Will' , 'Eleven' , 'Max' , 'Steve' , 'Nancy' , 'Joyce' , 'Hopper' , 'Jonathan']
    'Age' : [16,16,16,16,16,16,]
    
})