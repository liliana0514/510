import streamlit as st

st.set_page_config(
    page_title="Liliana Hsu ",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

st.header('''
          :red[Hi] :green[,] :blue[I] :violet[am]:rainbow[Liliana] :gray[.]:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:''')
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


# Interesting project
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Zhan Zhan Sweet Lab")
   st.image('liliana.jpg', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")

with col2:
   st.header("Zhuǎn zhuǎn")
   st.image('liliana.jpg', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")

with col3:
   st.header("Machine Learning-Aided Design")
   st.image('liliana.jpg', caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br style='top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
