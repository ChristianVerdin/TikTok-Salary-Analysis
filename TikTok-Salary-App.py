import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from hydralit import HydraApp
from hydralit import HydraHeadApp
import apps
import altair as alt
#when we import hydralit, we automatically get all of Streamlit
import hydralit as hy
import plotly.graph_objects as go


st.cache(persist=True)
df = pd.read_csv("final.csv") 

app = hy.HydraApp(title='TikTok Salary Analysis')

primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
base="light"





@app.addapp(is_home=True)
def home():
    st.title('US TikTok Salary Analysis')
    st.info('This web app was created to push ** pay transparency ** and customize the view of data for the users needs')
    st.header('Watch below...')
    video1 = open("C:/Users/chris/Videos/Captures/TikTok_Final.mp4", "rb") 
    st.video(video1)

@app.addapp(title='Summary')
def intro():
    st.info(''' 
    ** Data from this analysis was collected from google forms submitted anonymously by followers of ** [@chrristen 's TikTok page ](https://www.tiktok.com/@chrristen/) 
    * Analysis was performed by **[Christian Verdin.](https://www.linkedin.com/in/christian-verdin/)** 
    * Future surveys will be conducted to enable a true ETL process and limit the amount of data cleaning involved.
    * This app provides pay transparency in relation to multiple factors. 
    * Most charts are interactive and can be manipulated to your needs.
        * Data: ** 17,000 US employees **
            * Age Range, Job Title, 
            * Years of Experience
            * Industry
            * Highest Level of Education Completed
            * Annual Base Salary (USD)
            * Weekly Onsite Days
            * Gender
            * Diverse Identity
            * City
            * State
            * Closest Major City and State

    * Analysis is ONGOING and will be continually updated. Re-visit to not miss any updates
    ''')

@app.addapp(title='Analysis')
def summary():
 st.sidebar.markdown('**Filter here:** ')
 choosen_state = st.sidebar.multiselect("Choose state", df['state']).sort_values(df['state'])
 choosen_Age_Range = st.sidebar.multiselect("Choose Age Range", df['Age_Range'])
 choosen_Years_of_Experience = st.sidebar.multiselect("Choose years of experience", df['Years_of_Experience'])
 industry_type = st.sidebar.multiselect("Choose Industry", df['Industry'])
 industry_type = st.sidebar.multiselect("Choose Highest Level of Education Received", df['Highest_Level_of_Education_Received'])



@app.addapp(title='US Map')
def us_map():
 hy.info('US Map')
 

@app.addapp(title='More Visualizations')
def visualizations():
    import altair as alt
    

    source = df

    alt.Chart(source).mark_circle(size=60).encode(
        x='Years_of_Experience',
        y='Annual_Base_Salary',
        color='Age_Range',
        tooltip=['Job_Title', 'Age_Range', 'Gender', 'Annual_Base_Salary'].interactive())

@app.addapp(title='HeatMap')
def heatmap():
    df = pd.read_csv("final.csv") 
    st.subheader("Top 10 States in analysis")
    top_states = df['state'].value_counts().nlargest(10)
    st.bar_chart(top_states)  


    c = alt.Chart(df).mark_circle().encode(
    x='Age_Range', y='Annual_Base_Salary', size='Years_of_Experience', color='', tooltip=['Age_Range', 'Annual_Base_Salary', 'Years_of_Experience'])

    st.altair_chart(c, use_container_width=True)


@app.addapp(title='Gender Equality Analysis')
def gender():
    st.title('Analysis - Salary by Gender')
    st.title('Coming Soon!')
    st.info("""
        📢 **Update December 17 2021** 📢
        * If you would like to see the results and/or collaborate on pushing for gender pay equality please ** [REACH OUT](https://www.linkedin.com/in/christian-verdin/) **
        """)
 


@app.addapp(title='Diversity')
def diversity():
    st.title('Analysis - Salary by Ethnicity')
    st.title('Coming Soon!')
    st.info("""
        📢 **Update December 17 2021** 📢
        * If you would like to see the results and/or collaborate on pushing for salary equality/transparency please ** [REACH OUT](https://www.linkedin.com/in/christian-verdin/) **
        """)

@app.addapp(title='Contact')
def contact():
 st.title('Contact')
 st.header("""
        https://linktr.ee/christianverdin
        """)
 st.title('If you would like to volunteer or collaborate')
 form = st.form(key='my_form')
 form.text_input(label='Name')
 form.text_input(label='Email')
 form.text_input(label='LinkedIn profile link')
 submit_button = form.form_submit_button(label='Submit')
 if submit_button:
    st.write(f'Thank you')


#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()















































footer = st.markdown('Analysis and dashboard by: ** Christian Verdin ** ')

st.markdown('Powered by: \
            [<img src="https://justinlross.com.au/wp-content/uploads/2018/04/python-logo.png" height="30">](https://www.python.org/) \
            [<img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" height="30">](https://streamlit.io) \
            [<img src="https://raw.githubusercontent.com/TangleSpace/hydralit/main/docs/images/hydra.png" height="30">](https://github.com/TangleSpace/hydralit) \
            [<img src="https://altair-viz.github.io/_static/altair-logo-light.png" height="30">](https://altair-viz.github.io/)', \
            unsafe_allow_html=True)


# remove 'Made with Streamlit' footer
#MainMenu {visibility: hidden;}
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
