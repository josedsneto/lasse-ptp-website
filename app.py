import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="LASSE - PTP Synchronization", page_icon=":stopwatch:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# lottie_coding = load_lottieurl("https://app.lottiefiles.com/share/7925750f-a112-4e85-a7cb-d62d29decb81.json")
path = "./clock-animation.json"
with open(path, "r") as file:
    lottie_coding = json.load(file)

img_testbed_demo = Image.open("images/testbed-demo.jpg")
testbed_img = Image.open("images/testbed.png")
logo_img = Image.open("images/LASSE_logo.png")

# Add logo at the top
with st.container():
    col1, col2, col3 = st.columns([5,1,5])
    with col2:
        st.image(logo_img, use_column_width=True)

with st.container():
    st.subheader("Welcome :satellite_antenna:,")
    st.title("Here you can find accurate nanoseconds precision PTP datasets from FPGA-based testbed")
    st.write("We are the Telecommunications, Automation and Electronics Research and Development Center")
    st.write("[Discover >](https://www.lasse.ufpa.br)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our project")
        st.write("##")
        st.write(
            """
            We aim to enhance the time synchronization over 6G networks and beyond. Our expertise
            comprises several use cases such as:
            - PTP networks with and without assisted nodes
            - Over-the-air synchronization
            - AI and synchronization algorithms
            - and so on.
            """
        )
        st.write("[Learn More >](https://www.lasse.ufpa.br/en/Projects/3)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    fh_img, fh_txt = st.columns(2)
    with fh_txt:
        st.header("Fronthaul PTP datasets")
        st.write("##")
        st.write(
            """
            Check out the data we used in our works. Useful features are:
            - Traffic type (e.g. TDD)
            - Synchronization period
            - Number of RRUs
            - and so on

            We encourage you to discover the project [repository](https://github.com/lasseufpa/ptp-dal)
            """
        )
        st.write("[Catalog >](https://nextcloud.lasseufpa.org/s/t5gqZjnftJrqN35)")
        st.write("[Download >](https://nextcloud.lasseufpa.org/s/F39ZH2yPjFPsqZ9)")
    with fh_img:
        st.image(testbed_img)

with st.container():
    st.write("---")
    st.header("Testbed demo")
    st.write("##")
    img_column, txt_column = st.columns((1, 2))
    with img_column:
        st.image(img_testbed_demo)
    with txt_column:
        st.subheader("PTP-Synchronized Ethernet Fronthaul Testbed Demonstration")
        st.write(
            """
            This video demonstrates the fronthaul testbed developed at the Federal \
            University of Pará in collaboration with Ericsson Research for investigations \
            on Ethernet-based fronthaul networks for 5G. We focus on the distribution \
            of clock synchronization over the network using the IEEE 1588 precision \
            time protocol (PTP). We also show the setup for evaluating the fronthaul \
            together with a full real-time LTE stack implemented through the Open Air \
            Interface (OAI) software.
            """
        )
        st.markdown("[Watch](https://youtu.be/MPmGM559IGI?si=ccfjHCKOwTDZZrpp)")

with st.container():
    st.write("---")
    st.header("Contact us!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/nectxx@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()