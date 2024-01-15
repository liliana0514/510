import streamlit as st

st.set_page_config(
    page_title="Liliana Hsu ",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

st.header("Hi! I am Liliana.:sunflower::sunflower::sunflower::sunflower::sunflower::sunflower:")
col1, col2 = st.columns([0.4, 0.6], gap="medium")
with col1:
    st.image('liliana.jpg', caption='Hi! I am Liliana.', use_column_width="always")

    # Centered link_button using text-align
    st.markdown("""
    <style>
        .stLink {
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    st.link_button("LinkedIn", "https://www.linkedin.com/in/liliana-hsu-43896a16b/", help=None, type="secondary", disabled=False)


with col2:
    st.subheader("Education")
    st.write("University of Washington - M.S. Technology Innovation")
    st.write("Chiao Tung University - M.A. Applied Arts")
    st.subheader("Work Experience") 
    st.write("Prototyping Lab Specialist @ GIX")
    st.write("Innovation Committee @ Logitech Far East Ltd.")
    st.subheader("Interests")
    st.write("Obsessed in Material design :heart_eyes:")

st.divider()

st.header("My Project")

col1, col2= st.columns(2, gap = "medium")
with col1:
    st.write("Zhan Zhan Sweet Lab")
    st.image('zhan.jpg', use_column_width = "always")

with col2:
    st.write("Zhuǎn Zhuǎn")
    st.image('zhuan.jpg', use_column_width = "always")

st.divider()

st.header("My favourite Song")
st.subheader("Trivia 轉 : Seesaw · BTS @ Suga :dark_sunglasses:")
st.video("https://www.youtube.com/watch?v=NC_Lo8nRqfA", format="video/mp4", start_time=0)




