import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns
import ast
import matplotlib.pyplot as plt

from Utils.Cleaner import Cleaner as cleaner
from Utils.Plotlyfy import Plotlyfy as ply

# set the style for seaborn
sns.set_style('darkgrid') 
st.set_option('deprecation.showPyplotGlobalUse', False)
dataframe = 'https://samoungui.com/wp-content/uploads/2022/01/allocine_movies_brute.csv'

def app():
    st.title('DashBoard')
    ploty = ply(dataframe)
    # cleaning dataset brut
    clean_obj = cleaner(dataframe)
    df_s = clean_obj.movie_rating_cleaner()
    data = clean_obj.country_production()
    arr = clean_obj.insight_critics_cleaner(df_s)
    allocine = clean_obj.convert_data(dataframe)
    

    #st.write(clean_obj.convert_data(dataframe))  

    ## figure n_1
    fig1 = ploty.average_ratings(data)
    st.pyplot(fig1)
    
    ## figure n_2
    fig2 = ploty.distribution(df_s)
    st.pyplot(fig2)

    ## figure n_3
    fig3 = ploty.first_insight(arr)
    st.pyplot(fig3)

    ## figure n_4
    fig4 = ploty.second_insight(df_s)
    st.pyplot(fig4)

    ## figure n_5
    fig5 = ploty.ratings_distributions(allocine)
    st.pyplot(fig5)

    ## figure n_6
    fig6 = ploty.correlation_ratings(allocine)
    st.pyplot(fig6)

    ## figure n_7
    fig7 = ploty.compare_to_users_ratings(allocine)
    st.pyplot(fig7)
