import streamlit as st
st.set_page_config(page_title="AlloCiné data visualization", page_icon=":bar_chart:", layout="wide")

def Homepage():
    st.subheader('Dashboard')
    if st.button('Home', key="home"):
        st.session_state.runpage = main_page

def Viewpage():
    st.subheader('View data page')
    if st.button('HomePage', key="view"):
        st.session_state.runpage = main_page

def main_page():
    st.write('')
    btn1 = st.sidebar.button('Dashboard')
    btn2 = st.sidebar.button('View Data')

    if btn1:
        st.session_state.runpage = Homepage
        Homepage()

    if btn2:
        st.session_state.runpage = Viewpage
        Viewpage()


    if 'runpage' not in st.session_state:
        st.session_state.runpage = main_page
        st.session_state.runpage()


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
if __name__ == '__main__':
    main_page()