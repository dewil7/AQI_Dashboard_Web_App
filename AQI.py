import streamlit as st

from streamlit_option_menu import option_menu

import account, about, dataset

#setting page config
st.set_page_config(
    page_title= "Air Quality Index",
    layout="wide"
    )

st.title("📊 Clean Air Insights")

#multiapp definition
class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

#main function
    def run():

        with st.sidebar:
 
            app = option_menu(
                menu_title='Home',
                options=['About', 'Account','Dataset'],
                icons=['info', 'person'],
                menu_icon='house',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "backgroud-color":'#0000'},
                    "icon": {"color":"black", "font-size": "23px"},
                    "nav-link": {"color":"black", "font-size": "20px", "text-alignment": "left"},
                    "nav-link-selected": {"color":"white", "background-color": "#008DDA"}
                }
                )
            
            st.sidebar.image("logo.png", use_container_width=True)

        if app== 'About':
            about.app()
        if app== 'Account':
            account.app()
        if app== 'Dataset':
            dataset.app()

    run() 