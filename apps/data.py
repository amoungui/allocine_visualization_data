import streamlit as st
import numpy as np
import pandas as pd
from Utils.Cleaner import Cleaner as cleaner

filename = 'https://samoungui.com/wp-content/uploads/2022/01/allocine_movies_brute.csv'
@st.cache
def load_data():
    # cleaning dataset brut
    clean_obj = cleaner(filename)
    data = clean_obj.movie_rating_cleaner()  
    return data

def show():
    st.write(
        """
        ## 📑 Pagination
        
        Too much data to display? Now you can paginate through items (e.g. a table), 
        storing the current page number in `st.session_state`. 
        """
    )
    
    st.write("")
    if "page" not in st.session_state:
        st.session_state.page = 0

    def next_page():
        st.session_state.page += 1

    def prev_page():
        st.session_state.page -= 1

    col1, col2, col3, _ = st.beta_columns([0.1, 0.17, 0.1, 0.63])

    if st.session_state.page < 4:
        col3.button(">", on_click=next_page)
    else:
        col3.write("")  # this makes the empty column show up on mobile

    if st.session_state.page > 0:
        col1.button("<", on_click=prev_page)
    else:
        col1.write("")  # this makes the empty column show up on mobile

    col2.write(f"Page {1+st.session_state.page} of {5}")
    start = 30 * st.session_state.page
    end = start + 10
    st.write("")
    st.write(load_data().iloc[start:end])


def app():
    st.title('Data')
    show()
