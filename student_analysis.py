import pandas as pd
import streamlit as st
st.title("Student Performance Analysis")
df = pd.read_csv("student_Performance.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())
st.subheader("Data Summary")
st.write(df.describe())

if st.button("Show Dataset"):
    st.dataframe(df)

min_Age = st.slider("Select Minimum Age", 0, 10, 20, 30, 40, 50)
filtered_df = df[df["Age"] >= min_Age]
st.dataframe(filtered_df)

uploaded_file = st.file_uploaded("Upload CSV file")

if upoladed_file:
    df = df.read_csv(uploaded_file)
    st.dataframe(df)

st.bar_chart(df["Age"].value_counts())