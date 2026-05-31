import streamlit as st

st.set_page_config(page_title="Fun Quiz 🎮", page_icon="🔮", layout="centered")

st.title("Check Your Daily Luck! 🍀")
st.write("---")

st.write("### Choose a secret gift box to reveal your daily prediction:")

# Create 3 innocent-looking gift boxes
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎁 Box A"):
        st.info("Your luck score today is 85%! Expect a sweet message soon.")

with col2:
    if st.button("🎁 Box B"):
        st.warning("You will face a tough but beautiful question today... 😉")

with col3:
    # THIS IS THE TRAP BUTTON! 
    # Replace the URL below with your exact live Ishita website link
    st.link_button(
        "🎁 Box C", 
        "https://streamlit.app"
    )
