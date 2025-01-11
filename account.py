import streamlit as st
import dashboard
import firebase_admin

from firebase_admin import credentials, auth

if not firebase_admin._apps:
    cred = credentials.Certificate('aqi-db-6ce3e27bee8f.json')
    default_app = firebase_admin.initialize_app(cred)

def app():

    if 'username' not in st.session_state:
        st.session_state.username= ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail= ''

    def f():
        try:
            user= auth.get_user_by_email(email)
            st.success('Login Successful')
 
            st.session_state.username= user.uid
            st.session_state.useremail= user.email

            st.session_state.signedout= True
            st.session_state.signout= True

        except:
            st.warning('Login Failed')
        
    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''

    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False

    if not st.session_state['signedout']:
        choice = st.selectbox('Login/Signup', ['Login','Sign Up'])   

        st.markdown("###### Please provide your details")   

        if choice=='Login':
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
    
            st.button('Login', on_click=f)
        
        else:

            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            username = st.text_input('Username')

            if st.button('Create Account'):
                user = auth.create_user(email= email, password= password, uid= username)
                st.success('Account created sccessfully')
                st.balloons()
                st.markdown('Please login using yor email and password')
    
    if st.session_state.signout:
        st.text('Welcome, '+st.session_state.username)
        st.button('Sign out', on_click=t)

        if st.button('Open Dashboard'):
            dashboard.app()

    