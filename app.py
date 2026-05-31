import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="For My Baby Jaan ❤️", 
    page_icon="❤️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Helper function to load animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# High-quality Lottie Animation JSON links
lottie_heart = load_lottieurl("https://lottiefiles.com") # Heart
lottie_proposal = load_lottieurl("https://lottiefiles.com") # Ring/Proposal

# 2. Advanced Professional Styling Injection
st.markdown("""
    <style>
    /* Hide default elements smoothly */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Glassmorphism Cards Styling */
    .stage-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        margin-bottom: 25px;
    }
    
    /* Clean text hierarchies */
    .main-title {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        background: -webkit-linear-gradient(#ff4b4b, #ff8585);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States to maintain state cleanups
if 'stage' not in st.session_state:
    st.session_state.stage = 1
if 'married_status' not in st.session_state:
    st.session_state.married_status = None

# --- MAIN HERO TITLE SECTION ---
if lottie_heart:
    st_lottie(lottie_heart, height=180, key="hero_heart")

st.markdown("<h1 class='main-title'>For My Beautiful Ishita ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>Raj has crafted a special milestone questionnaire for you. Answer honestly, Oye meri bachi... 😉</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# --- STAGE 1 ---
with st.container():
    st.markdown("<div class='stage-card'>", unsafe_allow_html=True)
    st.subheader("📸 Stage 1: Humare 2 Saal 👩‍❤️‍👨")
    
    anniversary = st.radio(
        "Humare relationship ke in 2 saalon mein tumhein mere baare mein sabse best kya laga, cutie?",
        ["Select an answer...", 
         "Tum har situation mein mere liye hamesha time nikal lete ho", 
         "Tumhari har ek text aur call mere liye ekdum magic jaisi hoti hai", 
         "Jitna care tum meri karte ho, utna koi nahi kar sakta"],
        index=0
    )
    st.markdown("</div>", unsafe_allow_html=True)

if anniversary != "Select an answer...":
    st.session_state.stage = max(st.session_state.stage, 2)


# --- STAGE 2 ---
if st.session_state.stage >= 2:
    with st.container():
        st.markdown("<div class='stage-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #ff4b4b;'>📱 Stage 2: Humari Pyaari Baatein</h3>", unsafe_allow_html=True)
        
        connection = st.radio(
            "Humara sabse favorite routine ya moment kaunsa hota hai? 🥰",
            ["Select an answer...", 
             "Late-night audio calls jab sab so jaate hain", 
             "Video call par jab hum chupchap ek doosre ko dekhte hain", 
             "Ghanton baith kar future ki planning karna"],
            index=0
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
    if connection != "Select an answer...":
        st.toast("Mmm, sachi bolu toh yeh moments mere liye bhi sabse zyada precious hain. 😘", icon="❤️")
        
        with st.container():
            st.markdown("<div class='stage-card'>", unsafe_allow_html=True)
            future_q = st.radio(
                "Jab hum pehli baar real life mein milenge, toh tum sabse pehle kya karogi? 🥹❤️",
                ["Select an answer...", 
                 "Bhaag kar seedhe tumhare gale lag jaungi aur kabhi nahi chhodungi", 
                 "Bas chupchap tumhara cute sa face dekhti rahungi", 
                 "Finally tumhare saath ek lambi drive par jaungi"],
                index=0
            )
            st.markdown("</div>", unsafe_allow_html=True)
            
        if future_q != "Select an answer...":
            st.session_state.stage = max(st.session_state.stage, 3)


# --- STAGE 3 ---
if st.session_state.stage >= 3:
    st.write("---")
    if lottie_proposal:
        st_lottie(lottie_proposal, height=200, key="proposal_ring")
        
    with st.container():
        st.markdown("<div class='stage-card' style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #ff4b4b;'>💍 Stage 3: Sabse Bada Sawaal</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size: 26px; font-weight: bold;'>Will You Marry Me, Ishita?</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("YES! 💖", use_container_width=True, type="primary"):
                st.session_state.married_status = "yes"
                
        with col2:
            if st.button("No 😢", use_container_width=True):
                st.session_state.married_status = "no"
        st.markdown("</div>", unsafe_allow_html=True)

    # Trigger layouts based on final decision actions
    if st.session_state.married_status == "yes":
        st.balloons()
        st.success("Awww! I love you so much, my wifey! Meri life ke sabse best 2 saal the, aur ab puri zindagi saath rehna hai. 👩‍❤️‍👨")
        
        nickname = st.text_input("Shaadi ke baad apne official husband ko pyaar se kya bulaogi? 🥰")
        if nickname:
            st.markdown(f"<h2 style='text-align: center; color: #ff4b4b; animation: pulse 2s infinite;'>I am officially your {nickname} forever, baby jaan! 💕</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-style: italic; color: #777;'>— Yours and only yours, Raj</p>", unsafe_allow_html=True)
            
    elif st.session_state.married_status == "no":
        st.error("Error 403: 'No' option has been restricted by system administrator Raj! Please choose access paths containing absolute love parameters. 😉😏")
