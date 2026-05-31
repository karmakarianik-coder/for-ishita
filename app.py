import streamlit as st

# Setup browser details
st.set_page_config(page_title="For My Baby Jaan ❤️", page_icon="❤️", layout="centered")

# Smoothly hide default Streamlit branding elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Elegant Content Card Styling */
    .premium-card {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        border: 1px solid rgba(0, 0, 0, 0.05);
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
    }
    </style>
    """, unsafe_allow_html=True)

# Main Title Section
st.markdown("<h1 style='text-align: center; color: #ff4b4b; font-family: sans-serif;'>For My Beautiful Ishita ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #555;'>Raj ne tumhare liye ek chota sa test banaya hai. Honestly answer dena, Oye meri bachi... 😉</p>", unsafe_allow_html=True)
st.write("---")

# Initialize state tracker to keep user progression secure
if 'current_stage' not in st.session_state:
    st.session_state.current_stage = 1
if 'decision' not in st.session_state:
    st.session_state.decision = None

# --- STAGE 1: RELATIONSHIP TIMELINE ---
st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
st.subheader("📌 Stage 1: Humare 2 Saal 👩‍❤️‍👨")
anniversary = st.radio(
    "Humare relationship ke in 2 saalon mein tumhein mere baare mein sabse best kya laga, cutie?",
    ["", "Tum har situation mein mere liye hamesha time nikal lete ho", "Tumhari har ek text aur call mere liye ekdum magic jaisi hoti hai", "Jitna care tum meri karte ho, utna koi nahi kar sakta"],
    index=0
)
st.markdown("</div>", unsafe_allow_html=True)

if anniversary != "":
    st.session_state.current_stage = max(st.session_state.current_stage, 2)

# --- STAGE 2: CORE CONNECTION ---
if st.session_state.current_stage >= 2:
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #d94141;'>✨ Stage 2: Humari Pyaari Baatein 📱✨</h3>", unsafe_allow_html=True)
    connection = st.radio(
        "Humara sabse favorite routine ya moment kaunsa hota hai? 🥰",
        ["", "Late-night audio calls jab sab so jaate hain", "Video call par jab hum chupchap ek doosre ko dekhte hain", "Ghanton baith kar future ki planning karna"],
        index=0
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    if connection != "":
        st.toast("Mmm, sachi bolu toh yeh moments mere liye bhi sabse zyada precious hain, Oye meri bachi. 😘", icon="❤️")
        
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        future_q = st.radio(
            "Jab hum pehli baar real life mein milenge, toh tum sabse pehle kya karogi? 🥹❤️",
            ["", "Bhaag kar seedhe tumhare gale lag jaungi aur kabhi nahi chhodungi", "Bas chupchap tumhara cute sa face dekhti rahungi", "Finally tumhare saath ek lambi drive par jaungi"],
            index=0
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
        if future_q != "":
            st.session_state.current_stage = max(st.session_state.current_stage, 3)

# --- STAGE 3: THE PROPOSAL ---
if st.session_state.current_stage >= 3:
    st.write("---")
    st.markdown("<div class='premium-card' style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #ff4b4b;'>💍 Stage 3: Sabse Bada Sawaal 💍</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 700;'>Will You Marry Me, Ishita?</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! 💖", use_container_width=True, type="primary"):
            st.session_state.decision = "yes"
    with col2:
        if st.button("No 😢", use_container_width=True):
            st.session_state.decision = "no"
    st.markdown("</div>", unsafe_allow_html=True)
            
    if st.session_state.decision == "yes":
        st.balloons()
        st.success("Awww! I love you so much, my wifey! Meri life ke sabse best 2 saal the, aur ab puri zindagi saath rehna hai. 👩‍❤️‍👨")
        
        nickname = st.text_input("Shaadi ke baad apne official husband ko pyaar se kya bulaogi? 🥰")
        if nickname:
            st.markdown(f"<h2 style='text-align: center; color: #ff4b4b;'>I am officially your {nickname} forever, jaan! 💕</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-style: italic; color: #666;'>— Yours and only yours, Raj</p>", unsafe_allow_html=True)
                        
    elif st.session_state.decision == "no":
        st.error("Error: 'No' bolna toh allowed hi nahi hai, Oye meri bachi! Raj ne yeh button block kar diya hai. Dusra try karo! 😏")
