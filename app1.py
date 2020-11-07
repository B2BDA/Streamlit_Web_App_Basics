import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Explorer")
file = st.file_uploader("Upload Dataset", type = ["CSV"])
if file is not None:
    file.seek(0)
    df = pd.read_csv(file)
    st.dataframe(df)
    try:
        if st.button("Shape"):
            st.write(df.shape)
        if st.button("DataTypes"):
            st.write(df.dtypes)
        if st.button("Describe"):
            st.write(df.describe())
        if st.button("Viz"):
            st.write(sns.pairplot(df))
            st.pyplot();
    except Exception as e:
        print(e)
else:
    st.write("Upload CSV")
    

    