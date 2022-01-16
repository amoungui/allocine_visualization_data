import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns

# set the style for seaborn
sns.set_style('darkgrid')

def app():
    st.title('DashBoard')

    @st.cache
    def load_data():
        df = pd.read_csv('https://samoungui.com/wp-content/uploads/2022/01/allocine_movies.csv')
        
        return df 

    # load dataset
    data = load_data()
    st.write(data)
