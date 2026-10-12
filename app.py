import streamlit as st
from streamlit_option_menu import option_menu
from content.key_setup import init_key_state

init_key_state()

st.markdown("""
    <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    """, unsafe_allow_html=True)

st.set_page_config(
    page_title="Hill Cipher - LSB Steganography",
    page_icon="🚀"
)
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <div class="topbar-title" style="font-size: 20px">🚀 Hill Cipher - LSB Steganography</div>
    <div class="topbar-midle">
        <form action="https://www.google.com/search" method="get" target="_blank">
            <input 
                type="text"
                name="q"
                placeholder="Cari di Google..."
                class="searchbox"
            >
        </form>
    </div>
    <div class="topbar-right">
            <a href="https://github.com/nichyas27-hash" target="_blank"><i class="fab fa-github"></i></a>  
            <a href="https://drive.google.com/drive/folders/1MVO_E5s5HNTEc7dL61gFSxYYjD54P_b_?usp=sharing" target="_blank"><i class="fas fa-folder-open"></i></a> 
    </div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://media1.tenor.com/m/pXVD0uOHIncAAAAC/rocket-flying.gif")
    option = option_menu(
        menu_title="Menu",
        options=["Introduction","Cryptography", "Steganography", "About"],
        icons=["book","key", "image", "info-circle"],
        menu_icon="rocket",
        default_index=0,
    )

if option == "Introduction":
    from content.hill_cipher import hill_cipher
    from content.lsb_method import lsb

    st.header("Introduction")
    option = option_menu(
        menu_title="Did you know?",
        options=["Hill Cipher", "Least Significant Bit"],
        icons=["lock","image"],
        menu_icon="book",
        default_index=0,
        orientation="horizontal"
    )
    if option == "Hill Cipher":
        hill_cipher()
    elif option == "Least Significant Bit":
        lsb()
    
if option == "Cryptography":
    from content.encrypt import encryption
    from content.decrypt import decryption

    st.header("Cryptography")
    option = option_menu(
        menu_title="Select Option",
        options=["Encryption", "Decryption"],
        icons=["lock", "unlock"],
        menu_icon="key",
        default_index=0,
        orientation="horizontal"
    )
    if option == "Encryption":
        encryption()
    elif option == "Decryption":
        decryption()

if option == "Steganography":
    from content.embed import embedded
    from content.extract import extracted

    st.header("Steganography")
    option = option_menu(
        menu_title="Select Option",
        options=["Embed Image", "Extract Image"],
        icons=["image", "file-earmark-image"],
        menu_icon="file-earmark-image",
        orientation="horizontal",
        default_index=0,
    )

    if option == "Embed Image":
        embedded()
    elif option == "Extract Image":
        extracted()

if option == "About":
    from content.about import about
    about()

st.markdown("""
<div class="footer">
    <div class="footer-title" style="font-size: 20px">🚀 Hill Cipher - LSB Steganography</div>
    <div class="footer-right">
            <p>&copy; 2026 Hill Cipher - LSB Steganography. All rights reserved.</p> 
    </div>
</div>
""", unsafe_allow_html=True)