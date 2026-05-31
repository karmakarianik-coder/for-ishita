import streamlit as st

# Setup browser details
st.set_page_config(page_title="For My Baby Jaan ❤️", page_icon="❤️", layout="centered")

# Hide standard Streamlit header elements for a seamless app layout
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Main Title Section
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>For My Beautiful Ishita ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 19px;'>Raj ne tumhare liye ek chota sa test banaya hai. Honestly answer dena, Oye meri bachi... 😉</p>", unsafe_allow_html=True)
st.write("---")

# --- STAGE 1: THE RELATIONSHIP MILESTONE ---
st.subheader("Stage 1: Humare 2 Saal 👩‍❤️‍👨")
anniversary = st.radio(
    "Humare relationship ke in 2 saalon mein tumhein mere baare mein sabse best kya laga, cutie?",
    ["", "Tum har situation mein mere liye hamesha time nikal lete ho", "Tumhari har ek text aur call mere liye ekdum magic jaisi hoti hai", "Jitna care tum meri karte ho, utna koi nahi kar sakta"]
)

# --- STAGE 2: OUR REAL CONNECTION ---
if anniversary != "":
    st.write("###")
    st.markdown("<h3 style='color: #d94141;'>Stage 2: Humari Pyaari Baatein 📱✨</h3>", unsafe_allow_html=True)
    
    connection = st.radio(
        "Humara sabse favorite routine ya moment kaunsa hota hai? 🥰",
        ["", "Late-night audio calls jab sab so jaate hain", "Video call par jab hum chupchap ek doosre ko dekhte hain", "Ghanton baith kar future ki planning karna"]
    )
    
    if connection != "":
        st.write("###")
        st.write("Mmm, sachi bolu toh yeh moments mere liye bhi sabse zyada precious hain, Oye meri bachi. 😘")
            
        future_q = st.radio(
            "Jab hum pehli baar real life mein milenge, toh tum sabse pehle kya karogi? 🥹❤️",
            ["", "Bhaag kar seedhe tumhare gale lag jaungi aur kabhi nahi chhodungi", "Bas chupchap tumhara cute sa face dekhti rahungi", "Finally tumhare saath ek lambi drive par jaungi"]
        )
        
        # --- STAGE 3: THE LIVE PROPOSAL ---
        if future_q != "":
            st.write("###")
            st.write("Mera waada hai, hum bohot jald milenge aur main saari khushiyan poori karunga, Oye meri bachi. 😉")
                
            st.write("---")
            st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>Stage 3: Sabse Bada Sawaal 💍</h2>", unsafe_allow_html=True)
            st.write("<h3 style='text-align: center;'>Will You Marry Me, Ishita?</h3>", unsafe_allow_html=True)
            
            # Side-by-side alignment layout columns
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("YES! 💖", use_container_width=True):
                    st.balloons()
                    st.success("Awww! I love you so much, my wifey! Meri life ke sabse best 2 saal the, aur ab puri zindagi saath rehna hai. 👩‍❤️‍👨")
                    
                    nickname = st.text_input("Shaadi ke baad apne official husband ko pyaar se kya bulaogi? 🥰")
                    if nickname:
                        st.markdown(f"<h2 style='text-align: center; color: #ff4b4b;'>I am officially your {nickname} forever, baby jaan! 💕</h2>", unsafe_allow_html=True)
                        st.write("<p style='text-align: center;'>— Yours and only yours, Raj</p>", unsafe_allow_html=True)
                        
            with col2:
                if st.button("No 😢", use_container_width=True):
                    st.error("Error: 'No' bolna toh allowed hi nahi hai, Oye meri bachi! Raj ne yeh button block kar diya hai. Dusra try karo! 😏")
