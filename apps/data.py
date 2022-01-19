import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():
    st.title('Data')
    filename = 'https://samoungui.com/wp-content/uploads/2022/01/allocine_movies_brute.csv'
    
    @st.cache
    def load_data():
        df = pd.read_csv(filename)
        return df 
    
    data = load_data()
    st.dataframe(data)
