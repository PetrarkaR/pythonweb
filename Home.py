import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Petar :wave:")
    st.title("An embedded engineer and an electronics hobbyist")
    st.write(
        "Passionate embedded engineer exploring seamless system integration, tackling complex challenges, and continually learning in firmware development and microcontroller programming for optimal efficiency"
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            
            - Embedded Systems Development: Expertise in designing and developing embedded systems, ensuring seamless integration of hardware and software components.


            - Problem Solving: A knack for solving complex challenges in the realm of embedded systems, with a meticulous and analytical approach.


            - Firmware Development: Experience in writing and optimizing firmware code for embedded systems, ensuring reliability and functionality.


            - Microcontroller Programming: Skilled in programming a variety of microcontrollers, harnessing their full potential to create efficient and responsive systems.



            
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# ---- CONTACT ----
