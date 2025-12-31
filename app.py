import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="My Love's New Year Gift ❤️", page_icon="💖", layout="wide")

# --- BGM aur Styles (Yaha Music add kiya hai) ---
# Maine ek hidden YouTube player dala hai jo background mein music bajayega
st.markdown("""
    <style>
    iframe {
        display: none; /* Music player ko chhupane ke liye */
    }
    .stButton>button {
        background-color: #FF69B4; /* Pink buttons */
        color: white;
        border-radius: 20px;
        font-weight: bold;
    }
    </style>
    
    <iframe width="0" height="0" src="https://www.youtube.com/embed/H5v3kku4y6Q?autoplay=1&loop=1&playlist=H5v3kku4y6Q" frameborder="0" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)

# --- Session State ---
if 'page' not in st.session_state:
    st.session_state.page = 'envelope_back'

# --- 1. Real Envelope Back & Teddy ---
if st.session_state.page == 'envelope_back':
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG5kZmFraXU1a2dwaGRxbHRkaHVtODJjaTA1bTIxdzkzbDc0eno2NiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/mcWRPJaO1s6rbiAejV/giphy.gif", width=600) # Envelope Image
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueGZ3bm9qZzR3eHByZzR3eHByZzR3eHByZzR3eHByZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/C9x0nrDQ74BXK1snUP/giphy.gif", width=150) # Teddy with Heart
    st.markdown("## Pls accept the gift Ishri Pishri ❤️")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES"):
            st.session_state.page = 'gift_selection'
            st.rerun()
    with col2:
        if st.button("NO"):
            st.session_state.page = 'angry_teddy'
            st.rerun()

# --- 2. Angry Teddy (Gussa wala) ---
elif st.session_state.page == 'angry_teddy':
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnB0ZzB6Z3R3Z3R3Z3R3Z3R3Z3R3Z3R3Z3R3Z3R3Z3R3Z3&ep=v1_internal_gif_by_id&rid=giphy.gif", width=300) 
    st.header("Why did u click NO?? 😠")
    if st.button("Try Again"):
        st.session_state.page = 'envelope_back'
        st.rerun()

# --- 3. Gift Selection (Teen Boxes) ---
elif st.session_state.page == 'gift_selection':
    st.header("Gift for you! 🎁")
    st.write("Click any gift to open:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎁 Gift 1"):
            st.session_state.page = 'gift1'
            st.rerun()
    with col2:
        if st.button("🎁 Gift 2"):
            st.session_state.page = 'gift2'
            st.rerun()
    with col3:
        if st.button("🎁 Gift 3"):
            st.session_state.page = 'gift3'
            st.rerun()

# --- Gift 1: Countdown & Rose ---
elif st.session_state.page == 'gift1':
    for i in range(3, 0, -1):
        st.title(f"Opening in... {i}")
        time.sleep(1)
        st.rerun if i==1 else None
    st.balloons()
    st.title("HAPPY NEW YEAR MY LOVE! 🎊")
    st.image("https://i.imgur.com/2s4gYqG.gif", width=400) # Realistic Rose
    st.write("You are the most precious person in my life. Let's make this year amazing! ❤️")
    if st.button("Back"):
        st.session_state.page = 'gift_selection'
        st.rerun()

# --- Gift 2: Certificate ---
elif st.session_state.page == 'gift2':
    st.success("### 🏆 CERTIFICATE FOR THE BEST BF IN THE WORLD")
    st.write("This is to certify that you are the most loving, caring and amazing boyfriend ever!")
    st.write("Awarded to: My Gadha ❤️")
    if st.button("Back"):
        st.session_state.page = 'gift_selection'
        st.rerun()

# --- Gift 3: Donkey Video ---
elif st.session_state.page == 'gift3':
    st.video("https://www.youtube.com/watch?v=kYc5tL8F01o") # Donkey video
    st.header("Yahi ho tm gadhe! 😂")
    if st.button("Aage Badho"):
        st.session_state.page = 'kiss_page'
        st.rerun()

# --- 4. Realistic Kiss ---
elif st.session_state.page == 'kiss_page':
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnhhZzB6Z3R3Z3R3Z3R3Z3R3Z3R3Z3R3Z3R3Z3R3Z3R3Z3&ep=v1_internal_gif_by_id&rid=giphy.gif", width=400) # Kiss GIF
    if st.button("💋 Click for Kiss"):
        st.audio("https://www.myinstants.com/media/sounds/mwah.mp3", autoplay=True)
        st.session_state.page = 'final_para'
        st.rerun()

# --- 5. Lovely Para ---
elif st.session_state.page == 'final_para':
    st.snow()
    st.write("""
    ### My Jaan,
    In this new year, I promise to love you even more. You are my happiness and my whole world. 
    Thank you for being mine. 
    
    **I love u so much Ishri Pishri ❤️**
    """)
    if st.button("Restart ❤️"):
        st.session_state.page = 'envelope_back'
        st.rerun()
