# import streamlit as st
# import seaborn as sns
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# import pandas as pd

# import plotly.express as px





# st.title("Plotting the graph")
# df = px.data.gapminder()
# st.write(df)

# st.write(df.columns)

# st.write(df.describe())


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()





