import streamlit as st
from multiapp import MultiApp
from apps import home, data #, model # import your app modules here

st.set_page_config(page_title="AlloCiné data visualization", page_icon=":bar_chart:", layout="wide")

app = MultiApp()

# Add all your application here
app.add_app("DashBoard", home.app)
app.add_app("View Data", data.app)
#app.add_app("Model", model.app)
# The main app
app.run()

# ---- HIDE STREAMLIT STYLE ----
#  MainMenu {visibility: hidden;}
#  footer {visibility: hidden;}
#  header {visibility: hidden;}
hide_st_style = """
            <style>
                footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
