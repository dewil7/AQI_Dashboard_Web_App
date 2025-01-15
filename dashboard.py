import streamlit as st
import streamlit.components.v1 as components 

def app():
    st.markdown('##### Here you go 😊')
    url = "https://app.powerbi.com/view?r=eyJrIjoiMzE0MWViNDEtODQ1Mi00MGFmLWE0NzYtYWYwNzllZDZhY2M5IiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9"
    components.iframe(url, width=1080, height=590)
