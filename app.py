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
st.markdown("<p style='text-align: center; font-size: 16px; color: #555;'>Raj has designed a private interactive milestone tracking interface for you. Please answer sincerely... 😉</p>", unsafe_allow_html=True)
st.write("---")

# Initialize state tracker to keep user progression secure
if 'current_stage' not in st.session_state:
    st.session_state.current_stage = 1
if 'decision' not in st.session_state:
    st.session_state.decision = None

# --- STAGE 1: RELATIONSHIP TIMELINE ---
st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
st.subheader("📌 Stage 1: Our Beautiful 2-Year Journey 👩‍❤️‍👨")
anniversary = st.radio(
    "What has been the most meaningful aspect of our relationship over these past 2 years, cutie?",
    ["", "You seamlessly prioritize and make time for me in every single situation.", "Every single text message and call from you feels genuinely magical.", "The depth of care and emotional safety you provide is unmatched."],
    index=0
)
st.markdown("</div>", unsafe_allow_html=True)

if anniversary != "":
    st.session_state.current_stage = max(st.session_state.current_stage, 2)

# --- STAGE 2: CORE CONNECTION ---
if st.session_state.current_stage >= 2:
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #d94141;'>✨ Stage 2: Our Deepest Connections & Routines</h3>", unsafe_allow_html=True)
    connection = st.radio(
        "Which shared routine or moment holds the highest value to you? 🥰",
        ["", "Those quiet, dedicated late-night audio calls when the rest of the world is asleep.", "Our silent video calls where we simply appreciate each other's presence.", "Spending uninterrupted hours mapping out and planning our future together."],
        index=0
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    if connection != "":
        st.toast("To be completely honest, those moments are equally precious and irreplaceable to me. 😘", icon="❤️")
        
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        future_q = st.radio(
            "When we finally meet in real life, what is the very first thing you plan to do? 🥹❤️",
            ["", "Run straight into your arms, hold you close, and never let you go.", "Quietly look at your cute face and take in the moment.", "Finally set off on a long, peaceful drive together."],
            index=0
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
        if future_q != "":
            st.session_state.current_stage = max(st.session_state.current_stage, 3)

# --- STAGE 3: THE PROPOSAL ---
if st.session_state.current_stage >= 3:
    st.write("---")
    st.markdown("<div class='premium-card' style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #ff4b4b;'>💍 Stage 3: The Definitive Question</h2>", unsafe_allow_html=True)
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
        st.success("Thank you for making me the happiest person alive! These 2 years have been the absolute best chapter of my life, and I am incredibly excited to spend forever with you. 👩‍❤️‍👨")
        
        nickname = st.text_input("What affectionate nickname will you officially call your husband after marriage? 🥰")
        if nickname:
            st.markdown(f"<h2 style='text-align: center; color: #ff4b4b;'>I am officially your {nickname} forever, baby jaan! 💕</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-style: italic; color: #666;'>— Yours completely, Raj</p>", unsafe_allow_html=True)
                        
    elif st.session_state.decision == "no":
        st.error("Error 403: 'No' selection access denied. The administrator has restricted this interactive parameter. Please re-evaluate your choice! 😉😏")
