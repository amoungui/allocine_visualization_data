import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
#import ast
import matplotlib.pyplot as plt

from Utils.Cleaner import Cleaner as cleaner
from Utils.Plotlyfy import Plotlyfy as ply

# set the style for seaborn
sns.set_style('whitegrid') 
st.set_option('deprecation.showPyplotGlobalUse', False)
dataframe = 'https://samoungui.com/wp-content/uploads/2022/01/allocine_movies_brute.csv'

def app():
    st.title('DashBoard')
    # instanciation of class
    ploty = ply(dataframe) 
    clean_obj = cleaner(dataframe) # cleaning dataset brut
    # initialization of dataframe 
    df_s = clean_obj.movie_rating_cleaner()
    data = clean_obj.country_production()
    arr = clean_obj.insight_critics_cleaner(df_s)
    allocine = clean_obj.convert_data(dataframe)

    #####################################################################################
    ########################  visualization header| TOP KPI's  ##########################
    #####################################################################################

    total_movies = int(allocine['title'].count()) # we get here a total of movies that appear in the allocine dataset
    average_rating_press = round(allocine['press_rating'].mean(), 1) # we get average of press rating
    average_rating_spec = round(allocine['spec_rating'].mean(), 1) # we get average of user rating
    start_rating_press = ":star:"*int(round(average_rating_press, 0)) # we get the number of star according press rating
    start_rating_spec = ":star:"*int(round(average_rating_spec, 0)) # we get the number of star according user rating
    average_nb_press = round(allocine['nb_press'].mean(), 2) # we get average of number of press
    average_nb_spec = round(allocine['nb_spec'].mean(), 2) # we get average of number of spectator

    left_column, middle_column_1,middle_column_2, right_column = st.beta_columns(4)

    with left_column: 
        # display here the total of movies 
        st.markdown("#### Total Movies:")
        st.markdown("#### {}".format(total_movies))
    
    with middle_column_1:
        # display here average press rating and the average of number of star
        st.markdown("#### Average rating press:")
        st.markdown("#### {} {}".format(average_rating_press, start_rating_press))
    
    with middle_column_2:
        # display here average user rating and the average of number of star
        st.markdown("#### Average rating user:")
        st.markdown("#### {} {}".format(average_rating_spec, start_rating_spec))
    
    with right_column:
        # display here average of spectator 
        st.markdown("#### Average number of user:")
        st.markdown("#### {}".format(average_nb_spec))
    st.markdown("---")                
    #####################################################################################
    ########################  visualization header| all plot   ##########################
    #####################################################################################

    left_column_1, right_column_1 = st.beta_columns(2)
    st.markdown('### Correlation of differents notations')
    with left_column_1:
        ## figure n_1
        fig1 = ploty.average_ratings(data)
        st.pyplot(fig1)        
    
    with right_column_1:
        ## figure n_2
        fig2 = ploty.distribution(df_s)
        st.pyplot(fig2)

    ## figure n_5
    fig4 = ploty.ratings_distributions(allocine)
    st.pyplot(fig4)
            
    ## figure n_4
    fig5 = ploty.second_insight(df_s)
    st.pyplot(fig5)
            
    ## figure n_3
#    fig3 = ploty.first_insight(arr)
#    st.pyplot(fig3)
    
    left_column_2, middle_column_2 = st.beta_columns(2)
    st.markdown('### Correlation of differents notations')
    with left_column_2:
        ## figure n_6
        fig6_0 = ploty.correlation_ratings(allocine)
        st.pyplot(fig6_0)
        
    with middle_column_2:
        fig6_1 = sns.jointplot(data=allocine, x="press_rating", y="spec_rating", kind='hist')
        st.pyplot(fig6_1)

    ## figure n_7
    fig7 = ploty.compare_to_users_ratings(allocine)
    st.pyplot(fig7)

    ## figure n_8
    fig8 = ploty.five_star_movie(allocine)
    st.pyplot(fig8)

    ## figure n_9
    fig9 = ploty.ploting_the_distribution(allocine)
    st.pyplot(fig9) 