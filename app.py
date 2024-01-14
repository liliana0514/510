import streamlit as st
import pandas as pd
import numpy as np


chart_data = pd.DataFrame(np.random.randn(20, 4), columns=["col1", "Angry", "Sad", "Happy"])

st.balloons()
st.header("Hi! I'm Liliana.:balloon:")
col1, col2 = st.columns(2)

with col1:
    st.image('liliana.JPG', caption='Me')
    st.link_button("LinkedIn", "https://www.linkedin.com/in/chinshanlee/", help=None, type="secondary", disabled=False, use_container_width=False)


with col2:
    st.write("tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    st.write("Obsessed in Material design")
    st.subheader("Education")
    st.write("University of Washington - M.S. Technology Innovation")
    st.write("Chiao Tung University - M.A. Applied Arts")
    st.write("Shih Chien University = B.A. Industrial Design")
    st.subheader("Work Experience") 
    st.write("Prototyping Lab Specialist @ GIX")
    st.write("Innovation Committee @ Logitech Far East Ltd.")
    st.write("Product Designer @ Prosol Corp.")
    st.subheader("Hobbies")
    st.write("Yoga:Yoga:")
    st.write("Travelling:Travel:")
    st.write("Reading:Reading:")
    st.subheader("Interesting project")
    st.write("Zhan Zhan Sweet Lab")
    st.write("Machine Learning-Aided Design")
st.divider()

st.header("My Favorite Song")
st.video("https://youtu.be/wA3mVqo-jvg?si=6fWBvft5O7-k2TcY", format="video/mp4", start_time=0)

st.divider()

st.header("My Mental Health Status")
st.line_chart(
   chart_data, x="col1", y=["Angry", "Sad", "Happy"], color=["#E07A5F", "#A9BCD0", "#F2CC8F"]
)

