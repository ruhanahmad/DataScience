import streamlit as st
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


header = st.container()
data_set = st.container()
features = st.container()
model_training = st.container()


with header:
     st.title("kashti doob rhi h")
     st.text("noooo")


with data_set:
    st.header("datasts")
    st.text("nooooasdja")
    df = sns.load_dataset("titanic")
   

    df = df.dropna()

    st.write(df.head())
    st.bar_chart(df['sex'].value_counts())
    st.subheader("Clas k hisab sy faraq")
    st.bar_chart(df['class'].value_counts())
    st.subheader("Sex k lehax sy frq")
    st.bar_chart(df['age'].sample(10))


with model_training: 
    st.header("kashit sal")
    input,display = st.columns(2)

    max_depth = input.slider("how many people do you know?",min_value=10,max_value=100,value=20,step=5)
    
n_estimators = input.selectbox("how many",options=[50,100,200,300,'No Limit'])
 
#adding list of features
input.write(df.columns)


input_features= input.text_input("which features we should use")



model = RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)
 
# # machine learning model

X= df[[input_features]]
y = df[['fare']] 

model.fit(X,y)
pred = model.predict(y)


# Display metrices

display.subheader("mean absolute error")
display.write(mean_absolute_error(y,pred))
display.subheader("mean squareerror")
display.write(mean_squared_error(y,pred))
display.subheader("R squared score") 
display.write(r2_score(y,pred)) 



# st.header("This version")

# df = sns.load_dataset("iris")

# st.write(df.head())
# st.bar_chart(df['sepal_length'])
# st.line_chart(df['sepal_length'])