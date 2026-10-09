import streamlit as st

def about():
    st.markdown("""
    <div style="margin-top: 20px">
    <h4>🚀 Hill Cipher - LSB Steganography</h4>
    <p>Program ini dikembangkan sebagai media pembelajaran kriptografi klasik dan steganografi, 
    khususnya metode <b>Hill Cipher</b> untuk proses enkripsi dan dekripsi pesan serta 
    <b>Least Significant Bit (LSB)</b> untuk menyisipkan pesan rahasia ke dalam citra digital. 
    Melalui program ini, pengguna dapat mempelajari konsep dasar, memahami proses kerja setiap metode, 
    dan mengeksplorasi penerapan keamanan informasi secara interaktif.</p>
    </div>
    <h5><em>~ ~ ~ ~ ~ Our Team ~ ~ ~ ~ ~</em></h5>
    """, unsafe_allow_html=True)

    a, b = st.columns([0.7, 0.3])
    with a:
        st.image("assets/members.png")
    with b:
        st.image("https://media.tenor.com/xXNzEkd7BYYAAAAi/yapapa-cat.gif")

    st.markdown("""
    <h5 style="text-align: right"><em>~ ~ ~ ~ ~ Thank You ~ ~ ~ ~ ~</em><h5>
    """, unsafe_allow_html=True)