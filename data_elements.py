import streamlit as st
import pandas as pd

st.title("Streamlit Elements Demo")

# Dataframe Section

st.subheader("Dataframe")

df = pd.DataFrame({
    'Name' : ['Dustin' , 'Mike' , 'Lucas' , 'Will' , 'Eleven' , 'Max' , 'Steve' , 'Nancy' , 'Joyce' , 'Hopper' , 'Jonathan'],
    'Age' : [16,16,16,16,16,16,19,19,50,54,19],
    'Occupation' : ['Kids' , 'Kids' , 'Kids' , 'Kids' , 'Kids' , 'Kids' , 'Teenagers' , 'Teenagers' , 'Mom' , 'Cop' , 'Teenager']
    })
st.dataframe(df)

# Data Editor Section (Editable dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df) #Updates in Real time


# Static Table Section ( CANNOT DOWNLOAD/SEARCH )
st.subheader("Static Table")
st.table(df)

# Metrics Section
st.subheader("Metrics")
st.metric(label="Total Rows",value=len(df))
st.metric(label="Avg Age",value=round(df['Age'].mean(),1)) # Rounds the result to 1 decimal place # Involves Pandas Concept

# JSON and Dict Section
st.subheader("JSON and Dictionary")
sample_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Science", "Machine Learning"]
}

st.json(sample_dict)

# Also show it as dictionary
st.write("Dictionary view:", sample_dict)
