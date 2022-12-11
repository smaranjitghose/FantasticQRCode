"""
About Page
"""
import streamlit as st
from streamlit_lottie import st_lottie
from utils import *

st.set_page_config(
        page_icon="🤳",
        page_title = "Fantastic QR Code Gen",
        layout="centered"
    )
hide_footer()

st.title(":raising_hand: Frequently Asked Questions")

faq = {
    "What is the environment needed for this application?": "A: 🐍Python (preferably any version above 3.9)",
    "Who is the creator?": "@smaranjitghose",
    "Is this application open-source": "Yes, the appliation and all it's components are open-soruce",
    "Can we make an executable file for this?": "Yes",
    "Where can this application be deployed?": "A: 1) Heroku  2) Digital Ocean  3) AWS Beanstalk 4) Streamlit Sharing 5) Render 6)Cyclic"
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

