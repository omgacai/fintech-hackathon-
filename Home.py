import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

#page set up 
st.set_page_config(page_title = "slaxers", page_icon=":sparkles:" )
st.title("Home Page")
#st.sidebar.success("Select a hotel")

lottie_coding = "https://lottie.host/d1163032-7c62-4d12-88d4-2cad8014e266/5ZtHSL0g6T.json"
img_1 = Image.open("images/IMG_2742 copy.PNG")
img_2 = Image.open("images/IMG_2772 copy.PNG")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status.code != 200:
        return None
    return r.json()

#header
with st.container():
    st.subheader("Hi we are slaxers :wave:")
    st.title("slaxers reviews")
    st.write("review-lution awaits you: where reviews reflect trust")
    st.write("[Learn more >](https://www.youtube.com/watch?v=VqgUkExPvLY)")

with st.container():
    st.write("---") #divider
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what we do")
        st.write("trust us pls")
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")

#About us segment?
with st.container():
    st.write("---")
    st.header("About us")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_1)
    
    with text_column:
        st.write("helloooooooooooo this is us")
        st.markdown("[watch video](https://www.youtube.com/watch?v=VqgUkExPvLY)")

#contact us 
with st.container():
    st.write("---")
    st.header("Get in touch with us!")
    st.write("##")

    contact_form = """
<form action="https://formsubmit.co/yongsm1223@gmail.com" method="POST">
    <input type = "hidden", name = "_captcha" value = "false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder = "your email" required>
     <input type="text" name="text" placeholder = "your message" required>
     <button type="submit">Send</button>
</form>
"""
with st.container():
    st.markdown(contact_form, unsafe_allow_html=True)





























