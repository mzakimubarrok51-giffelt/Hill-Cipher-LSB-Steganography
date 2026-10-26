import streamlit as st
st.markdown("""
    <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    """, unsafe_allow_html=True)

def about():
    st.markdown("""
    <div style="margin-top: 20px">
    <h3>🚀 Hill Cipher - LSB Steganography</h3>
    <p>Program ini dikembangkan sebagai media pembelajaran kriptografi klasik dan steganografi, 
    khususnya metode <b>Hill Cipher</b> untuk proses enkripsi dan dekripsi pesan serta 
    <b>Least Significant Bit (LSB)</b> untuk menyisipkan pesan rahasia ke dalam citra digital. 
    Melalui program ini, pengguna dapat mempelajari konsep dasar, memahami proses kerja setiap metode, 
    dan mengeksplorasi penerapan keamanan informasi secara interaktif.</p>
    </div>
    """, unsafe_allow_html=True)

    st.header("~ ~ ~ Our Team ~ ~ ~")
    with st.container():
        x, y = st.columns(2)
        with x:
            st.image("assets/zaki.png")
        with y:
            st.subheader("M. Zaki Mubarok")
            st.subheader("5002231051")
            st.markdown("""
            <div style="display: flex; gap: 20px">
                <a href="https://www.instagram.com/zakimubarrok__/" target="blank_" style="font-size: 24px"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/in/m-zaki-mubarrok-a3673a32b/" target="blank_" style="font-size: 24px"><i class="fab fa-linkedin"></i></a>
                <a href="https://github.com/mzakimubarrok51-giffelt" target="blank_" style="font-size: 24px"><i class="fab fa-github"></i></a>
            </div>
            """, unsafe_allow_html=True)    

    with st.container():
        x, y = st.columns(2)
        with x:
            st.subheader("Tisha Anargya Megandana")
            st.subheader("5002231079")
            st.markdown("""
            <div style="display: flex; gap: 20px">
                <a href="https://www.instagram.com/gyagiyem/" target="blank_" style="font-size: 24px"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/in/tisha-anargya-m-591047224/" target="blank_" style="font-size: 24px"><i class="fab fa-linkedin"></i></a>
                <a href="#" style="font-size: 24px"><i class="fab fa-github"></i></a>
            </div>
            """, unsafe_allow_html=True)    
        with y:
            st.image("assets/gya.png")

    with st.container():
        x, y = st.columns(2)
        with x:
            st.image("assets/yasa.png")
        with y:
            st.subheader("Jaya Perkasa")
            st.subheader("5002231086")
            st.markdown("""
            <div style="display: flex; gap: 20px">
                <a href="https://www.instagram.com/yassaya__/" target="blank_" style="font-size: 24px"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/in/jaya-perkasa/" target="blank_" style="font-size: 24px"><i class="fab fa-linkedin"></i></a>
                <a href="https://github.com/nichyas27-hash" target="blank_" style="font-size: 24px"><i class="fab fa-github"></i></a>
            </div>            
            """, unsafe_allow_html=True)    

    with st.container():
        x, y = st.columns(2)
        with x:
            st.subheader("M. Rangga Arisandy")
            st.subheader("5002231105")
            st.markdown("""
            <div style="display: flex; gap: 20px">
                <a href="https://www.instagram.com/raaaang27/" target="blank_" style="font-size: 24px"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/in/muhammadranggaarisandy/" target="blank_" style="font-size: 24px"><i class="fab fa-linkedin"></i></a>
                <a href="#" style="font-size: 24px"><i class="fab fa-github"></i></a>
            </div>
            """, unsafe_allow_html=True)    
        with y:
            st.image("assets/rangga.png")

    with st.container():
        x, y = st.columns(2)
        with x:
            st.image("assets/zidhan.png")
        with y:
            st.subheader("M. Zidhan Ikbar H.S")
            st.subheader("5002231119")
            st.markdown("""
            <div style="display: flex; gap: 20px">
                <a href="https://www.instagram.com/jidan.java/" target="blank_" style="font-size: 24px"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/in/muhammadzidhan/" target="blank_" style="font-size: 24px"><i class="fab fa-linkedin"></i></a>
                <a href="#" style="font-size: 24px"><i class="fab fa-github"></i></a>
            </div>           
            """, unsafe_allow_html=True)    

    with st.container():
        x, y = st.columns(2)
        with x:
            st.subheader("Yohana Ayudyah Pramesti")
            st.subheader("5002231124")
            st.markdown("""
            <div style="display: flex; gap: 20px">
                <a href="https://www.instagram.com/acissayu/" target="blank_" style="font-size: 24px"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/in/yohana-ayudyah-pramesti-91b1a1289/" target="blank_" style="font-size: 24px"><i class="fab fa-linkedin"></i></a>
                <a href="#" style="font-size: 24px"><i class="fab fa-github"></i></a>
            </div>           
            """, unsafe_allow_html=True)    
        with y:
            st.image("assets/yohana.png")

    with st.container():
        x, y = st.columns(2)
        with x:
            st.write("")
        with y:
            st.header("~ ~ ~ Thank You ~ ~ ~")
