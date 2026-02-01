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

min_Age = st.slider("Select Minimum Age", 0, 100, 20)
filtered_df = df[df["Age"] >= min_Age]
st.dataframe(filtered_df)


uploaded_file = st.file_uploader("Upload CSV file")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.bar_chart(df["Score"].value_counts())

st.line_chart(df["Score"])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df["Score"])
st.pyplot(fig)


st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose View",
    ["Dataset", "Summary", "Visualizations"]
)


if option == "Dataset":
    st.dataframe(df)

elif option == "Summary":
    st.write(df.describe())

elif option == "Visualizations":
    st.bar_chart(df["Gender"].value_counts())


