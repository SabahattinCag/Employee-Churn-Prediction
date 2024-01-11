__author__ = "Sabahattin Cag"

import pandas as pd
import numpy as np
import joblib
import streamlit as st

st.markdown("""<p style="background-color:blue; color:floralwhite; font-size:300%; text-align:center; border-radius:10px 10px; font-family:newtimeroman; line-height: 1.4;">Employee Churn Prediction</p>""", unsafe_allow_html=True)
st.markdown('Employee churn refers to the phenomenon where employees leave an organization voluntarily. This project aims to predict which employees are likely to churn based on various features provided in the HR dataset.')

df = pd.read_csv('HR_Dataset.csv')
st.write(df.head(2))
st.markdown("I have determined that the following features have a high impact on the churn and Random Forest Algorithm gives the best result. Therefore, we can use them in machine learning algorithms.\n 'satisfaction_level','number_project','time_spend_company','average_montly_hours','last_evaluation'")
df_new = df[['satisfaction_level','number_project','time_spend_company','average_montly_hours','last_evaluation']]
st.write(df_new.head(2))

st.sidebar.header('Random Forest Algorithm')
st.sidebar.subheader('Select the properties of the employee')

#satisfaction level
sl_min = df_new.satisfaction_level.min()
sl_max = df_new.satisfaction_level.max()
satisfaction_level = st.sidebar.number_input("Satisfaction Level", min_value=sl_min,max_value=sl_max,value=0.82)
#number of projects
np_min = df_new.number_project.min()
np_max = df_new.number_project.max()
number_project = st.sidebar.slider("Number of Project", min_value=np_min,max_value=np_max,step=1,value=6)
#time spent in the company
ts_min = df_new.time_spend_company.min()
ts_max = df_new.time_spend_company.max()
time_spend_company = st.sidebar.slider("Time-Spend in the Company", min_value=ts_min,max_value=ts_max,step=1,value=7)
#average worked hours in a month
ah_min = df_new.average_montly_hours.min()
ah_max = df_new.average_montly_hours.max()
average_montly_hours = st.sidebar.number_input("Average-Worked Hours in a Month", min_value=ah_min, max_value=ah_max,value=310)
#last evaluation
le_min = df_new.last_evaluation.min()
le_max = df_new.last_evaluation.max()
last_evaluation=st.sidebar.number_input("Last Evaluation", min_value=le_min,max_value=le_max,value=0.82)



button_styles = """
    <style>
        div.stButton > button {
            background-color: #3498db;  /* Set your desired background color */
            color: #ffffff;             /* Set your desired text color */
        }
    </style>
"""

# Display the button with custom styles
st.markdown(button_styles, unsafe_allow_html=True)

predict = st.button('Predict the employee churn')

model = joblib.load('final_model.joblib')

my_dict = {"satisfaction_level":satisfaction_level, 
           "number_project":number_project, 
           "time_spend_company":time_spend_company,
           "average_montly_hours":average_montly_hours, 
           "last_evaluation":last_evaluation
           }

df_example = pd.DataFrame.from_dict([my_dict])

if predict:
    if model.predict(df_example)[0]==1:
        st.error('The employee will quit!',icon="🚨")
    else:
       
        st.success('The employee will stay!',icon="✅")
    


