import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import pandas_profiling
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.markdown(''' 
 # ** Exploratory Data Analysis Web Application**
 This app is developed by Ruhan Ahmad called **EDA APP

''' )

# how to upload file from pc

with st.sidebar.header("Upload your dataset .csv"):
      uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
      df = sns.load_dataset("titanic")
      st.sidebar.markdown("[Example CSV File]()")

# profiling report for pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df,explorative=True)
    st.header('**Input Df**')
    st.write("-----")
    st.header('**Profiling Report with Pandas**')
    st_profile_report(pr)
else:
    st.info("Awaiting for CSV file"),
    if st.button("Press to use example data"):

    
        def load_data():
             a = pd.DataFrame(np.random.rand(100,5),
                 columns=["age","bannana","picture","video","run"])



    

            
# import pandas as pd
# import pandas_profiling
# import streamlit as st

# from streamlit_pandas_profiling import st_profile_report

# df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
# pr = df.profile_report()

# st_profile_report(pr)