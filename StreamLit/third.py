from turtle import color
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Potly and streamlit combination app")
df = px.data.gapminder()
st.write(df.describe())


year_option = df['year'].unique().tolist()
year = st.selectbox("which year should we plot", year_option,0)
# df =df[df["year"] == year]

fig = px.scatter(df,x = "gdpPercap", y = "lifeExp",size = "pop",color = "country",
hover_name = "country",log_x = True,size_max =55 ,range_x = [100,100000], range_y = [20,90],
animation_frame = "year" ,animation_group = "country"
)

st.write(fig)