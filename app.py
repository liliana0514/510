import streamlit as st

st.set_page_config(
    page_title="Liliana Hsu ",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

st.header("Hi! I am Liliana.:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.image('liliana.jpg', caption='Hi! I am Liliana!')

with col2:
    st.subheader("Education")
    st.write("University of Washington - M.S. Technology Innovation")
    st.write("Chiao Tung University - M.A. Applied Arts")
    st.subheader("Work Experience") 
    st.write("Prototyping Lab Specialist @ GIX")
    st.write("Innovation Committee @ Logitech Far East Ltd.")
    st.subheader("Hobbies")
    st.write("Obsessed in Material design")

st.divider()

st.header("My Interesting project")
# Interesting project
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Zhan Zhan Sweet Lab")

with col2:
   st.header("Zhuǎn zhuǎn")

with col3:
   st.header("Machine Learning-Aided Design")



st.link_button("LinkedIn", "https://www.linkedin.com/in/liliana-hsu-43896a16b/", help=None, type="secondary", disabled=False, use_container_width=False)

st.divider()

st.header("My Favorite Song")
st.video("https://youtu.be/wA3mVqo-jvg?si=6fWBvft5O7-k2TcY", format="video/mp4", start_time=0)



