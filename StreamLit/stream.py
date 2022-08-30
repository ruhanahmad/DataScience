import streamlit as st
import seaborn as sns

header = st.container()
data_set = st.container()
features = st.container()
model_training = st.container()


with header:
     st.title("kashti doob rhi h")
     st.text("noooo")


with data_set:
    st.title("datasts")
    st.text("nooooasdja")

st.header("This version")

df = sns.load_dataset("iris")

st.write(df.head())
st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])