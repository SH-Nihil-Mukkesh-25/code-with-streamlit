import streamlit as st
import pandas as pd

st.title("Streamlit Elements Demo")

# Dataframe Section

st.subheader("Dataframe")

df = pd.DataFrame({
    'Name' : ['Dustin' , 'Mike' , 'Lucas' , 'Will' , 'Eleven' , 'Max' , 'Steve' , 'Nancy' , 'Joyce' , 'Hopper' , 'Jonathan']
    'Age' : [16,16,16,16,16,16,19,19,50,54,19]
    'Occupation' : ['Kids' , 'Kids' , 'Kids' , 'Kids' , 'Kids' , 'Kids' , 'Teenagers' , 'Teenagers' , 'Mom' , 'P']
    
})