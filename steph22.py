import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
import altair as alt
import streamlit as st
import plotly.figure_factory as ff
import matplotlib 
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(page_icon="images.jpg",layout="wide")
font = "monospace"
st.subheader("MSBA350 Healthcare Analytics - Stephanie Abdelnour")
st.title("Road Traffic Accidents")
menu = option_menu(None, ["Home","Dataset","Dashboard"],icons=['house',"cloud","bar-chart-line"],menu_icon="cast", default_index=0, orientation="horizontal", styles={"container": {"padding": "0!important", "background-color": "#fafafa"},"icon": {"color": "black", "font-size": "25px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},"nav-link-selected": {"background-color": "#FF3366"},})

if menu=="Dataset": st.write("This data set is collected from Addis Ababa Sub city police departments for Masters research work. It has been prepared from manual records of road traffic accident of the year 2017-20.")


#EDA metrics
col1, col2, col3 = st.columns(3)
if menu=="Dataset":col1.metric("Number of Accidents", "12,316")
if menu=="Dataset":col2.metric("Features", "32")
if menu=="Dataset":col3.metric("Time frame", "2017-2020")

df= pd.read_csv("output(6).csv", sep='\t',  error_bad_lines=False)

if menu=="Dataset": st.write(df)

if menu=="Home":st.image('vehicle-damage-transport-crash-and-dangerous-vector-29448170.jpg')
if menu=="Home": st.write("Road traffic accidents (RTAs) have emerged as an important public health issue which needs to be tackled by a multi-disciplinary approach. The trend in RTA injuries and death is becoming alarming in countries like Lebanon. The number of fatal and disabling road accident happening is increasing day by day and is a real public health challenge for all the concerned agencies to prevent it. The approach to implement the rules and regulations available to prevent road accidents is often ineffective and half-hearted. Awareness creation, strict implementation of traffic rules, and scientific engineering measures are the need of the hour to prevent this public health catastrophe.")
#if menu=="Home": st.image("C:\Users\User\Desktop\myproject\SM286XhJ_400x400.jpg")
col1, col2=st.columns(2)
if menu=="Home":col2.metric("Road Traffic Accidents Deaths in Lebanon", "3.28%")



col1, col2, col3= st.columns(3)

#Gender piechart
if menu=="Dashboard": col1.markdown("Gender Distribution")
labels= {"Male":"94", "Female":"6"}
sizes = (94,6)
colors = ['#B7C3F3', '#DD7596']
explode = (0,0)
fig1, ax1 = plt.subplots(figsize=(5,3))
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
if menu=="Dashboard": col1.write(fig1)


#Severity piechart
labels= {"Slight Injuries":"84", "Serious Injuries":"14", "Fatal Injuries": "2"}
sizes = (84,14,2)
colors = ['#B7C3F3', '#DD7596', '#FF3366']
explode = (0,0,0)
fig1, ax1 = plt.subplots(figsize=(5,3))
if menu=="Dashboard": col1.markdown("Severity of Accidents")
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
if menu=="Dashboard": col1.write(fig1)

#Age groups
labels= {"18-30":"40", "31-50":"38", "51+": "15", "18-":"7"}
sizes = (40,38,15,7)
colors = ['#B7C3F3', '#DD7596', '#FF3366', '#9A9CA2']
explode = (0,0,0,0)
fig1, ax1 = plt.subplots(figsize=(5,3))
if menu=="Dashboard": col1.markdown("Age Distribution of drivers")
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
if menu=="Dashboard": col1.write(fig1)



#Fig1: Age/Gender/Severity
fig1 = alt.Chart(df).mark_point().encode(
    y='Age_of_driver',
    x='Gender_of_driver',
    color='Accident_severity',
    column='Accident_severity',
    
).properties(
    width=150,
    height=150,
    title= "Accident Severity by Gender and age of the Driver"
)
fig1.configure_header(
    titleColor='Set1[7]',
    titleFontSize=14,
    labelColor='#DD7596',
    labelFontSize=12
)
if menu=="Dashboard":col2.write(fig1)

#Number of Car involved +  Severity 
df2 = pd.DataFrame(
     df,
     columns=['Number_of_vehicles_involved', 'Accident_severity'])

c = alt.Chart(df2).mark_circle().encode(
     x='Accident_severity', y='Number_of_vehicles_involved', tooltip=['Number_of_vehicles_involved', 'Accident_severity']
     ).properties(
    width=500,
    height=300,
    title= "Accident Severity by the Number of Cars Involved"

)
if menu=="Dashboard":col2.altair_chart(c, use_container_width=True)


#fig2 heatmap: Severity/Day/light conditions
df1=df.groupby('Accident_severity')['Day_of_week'].value_counts().unstack().fillna(0)
import plotly.express as px
fig = px.imshow(df1,
                labels=dict(x="Day_of_Week", y="Light_conditions", color="Accident_severity"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'],
                y=['Daylight', 'Darkness - light', 'Darkness - no light'],
                title="Heatmap of Accident Severity by day of the week & Light Conditions",
)

fig.update_xaxes(side="top")
if menu=="Dashboard":col2.write(fig)





#Cause of accident count
fig2 = px.histogram(data_frame=df, x="Cause_of_accident", title="Cause of Accident")
if menu=="Dashboard":col1.write(fig2)
