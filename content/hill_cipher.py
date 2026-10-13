import streamlit as st

def hill_cipher():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown("""
    <h4>🤔Apa itu Hill Cipher? </h4>
    <div style="display: flex">
        <div>
            <p>
                <b>Hill Cipher</b> adalah salah satu algoritma kriptografi klasik yang digunakan 
                untuk menyandikan pesan teks menjadi pesan rahasia. Algoritma ini dikembangkan oleh <a href="https://en.wikipedia.org/wiki/Lester_S._Hill" target="_blank">Lester S. Hill</a> 
                pada tahun 1929 dan menggunakan konsep aljabar linear 😱, khususnya:
                <ul> 
                    <li> Matriks </li>
                    <li> Vektor </li>
                    <li> Perkalian matriks </li>
                    <li> Aritmetika modulo </li>
                    <li> Invers matriks </li>
                </ul>
            </p> 
        </div>
            <img src="https://tse1.mm.bing.net/th/id/OIP.aof-Myq7bzQ_PkS6NxYBowAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
            width=200px>
    </div>
    <p> 
        Berbeda dengan Caesar Cipher yang mengganti setiap huruf berdasarkan pergeseran tertentu, 
        Hill Cipher mengenkripsi beberapa huruf sekaligus menggunakan operasi matematika. 
        Contoh Hill Cipher dengan matriks kunci 2x2 (enkripsi setiap 2 huruf) 
    </p>""", unsafe_allow_html=True)
    
    st.latex(rf"""
    \large\begin{{aligned}}
        \mathbf{{C = K \cdot P \mod 26}}
    \end{{aligned}} \\
    \large\begin{{aligned}}
        \begin{{bmatrix}}
            C_1 \\
            C_2 \\
        \end{{bmatrix}}
        = 
        \begin{{bmatrix}}
            K_{11} & K_{12} \\
            K_{21} & K_{22} \\
        \end{{bmatrix}}
        \begin{{bmatrix}}
            P_1 \\
            P_2 \\
        \end{{bmatrix}}
        \mod 26  \\ 
    \end{{aligned}}""")
    
    st.markdown("""
    <p>
        <b>Keterangan:</b>
        <ul>
            <li>C adalah vektor ciphertext.</li>
            <li>K adalah matriks kunci.</li>
            <li>P adalah vektor plaintext.</li>
            <li>(mod 26) berarti setiap hasil akhirnya dihitung dengan modulo 26.</li>
        </ul>
        Berbeda dengan proses enkripsi, dekripsi Hill Cipher menggunakan invers matriks sebagai kunci.
        Contoh Hill Cipher dengan matriks kunci 2x2 (deskripsi setiap 2 huruf)
    </p>""", unsafe_allow_html=True)
    
    st.latex(rf"""
    \large\begin{{aligned}}
        \mathbf{{P = K^{{-1}} \cdot C \mod 26}}
    \end{{aligned}} \\
    \large\begin{{aligned}}
        \begin{{bmatrix}}
            P_1 \\
            P_2 \\
        \end{{bmatrix}}
        = 
        \begin{{bmatrix}}
            K_{{11}}^{{-1}} & K_{{12}}^{{-1}} \\
            K_{{21}}^{{-1}} & K_{{22}}^{{-1}} \\
        \end{{bmatrix}}
        \begin{{bmatrix}}
            C_1 \\
            C_2 \\
        \end{{bmatrix}}
        \mod 26  \\ 
    \end{{aligned}}""")
    
    st.markdown("""
    <p>
        <b>Keterangan:</b>
        <ul>
            <li>P adalah vektor plaintext.</li>
            <li>K^-1 adalah invers dari matriks kunci K.</li>
            <li>C adalah vektor ciphertext.</li>
            <li>(mod 26) berarti setiap hasil akhirnya dihitung dengan modulo 26.</li>
        </ul>
    </p>

    <h4>📢 Syarat matriks kunci dapat digunakan</h4>
    <p>
        ⚠️ Tidak semua matriks dapat digunakan sebagai kunci Hill Cipher. 
        Matriks harus memiliki invers modulo 26 agar pesan dapat didekripsi dengan benar.
        Syarat matematisnya adalah:
    </p>""", unsafe_allow_html=True)
    
    st.latex(rf"""
    \large\begin{{aligned}}
        \text{{gcd}}(\text{{det}}(K), 26) = 1
    \end{{aligned}}""")
    
    st.markdown("""
    <p>
        Artinya, <b>FPB antara determinan matriks kunci dan 26 harus sama dengan 1.</b> 
        Jika determinan matriks kunci K tidak memiliki invers modulo 26, 
        maka matriks tersebut tidak dapat digunakan untuk enkripsi dan dekripsi.</p>
    
    <h4>🧐 Bagaimana jika panjang pesan tidak sesuai ukuran matriks?</h4>
    <p> 
        Hill Cipher memproses pesan dalam blok yang ukurannya sesuai dengan matriks kunci.
        Misalnya, kita menggunakan matriks 2x2 dan ingin mengenkripsi: "BUS" 
        Pesan tersebut memiliki tiga huruf, kita dapat membaginya menjadi: 
    </p>
    <div style="text-align: center; text-justify: center">
        <b style="font-size: 24px"> BU | S </b>
    </div>
    <p style="margin-top: 12px"> Karena setiap blok harus berisi dua huruf. oleh karena itu, kita perlu menambahkan huruf pengisi untuk melengkapi blok terakhir.
        Misalnya, kita menambahkan huruf "X" sebagai pengisi, sehingga pesan menjadi "BUSX".
    </p>
    <div style="text-align: center; text-justify: center">
        <b style="font-size: 24px"> BU | SX </b>
    </div>
    <p style="margin-top: 12px"> 
        Dengan demikian, setiap blok memiliki panjang yang sesuai dengan ukuran matriks kunci, 
        dan proses enkripsi dapat dilakukan dengan benar.
    </p>

    <h4>📝 Kelebihan dan kekurangan Hill Cipher </h4>
    <table>
        <tr style="border: 2px solid #000; background-color: blue; color: #ffffff">
            <th style="border: 2px solid #000">No</th>
            <th style="border: 2px solid #000">Kelebihan</th>
            <th style="border: 2px solid #000">Kekurangan</th>
        </tr>
        <tr style="border: 2px solid #000">
            <td style="border: 2px solid #000">1</td>
            <td style="border: 2px solid #000">Lebih aman dibandingkan dengan cipher sederhana seperti Caesar Cipher karena mengenkripsi beberapa huruf sekaligus.</td>
            <td style="border: 2px solid #000">Jika kunci diketahui, maka seluruh pesan dapat dengan mudah didekripsi.</td>
        </tr>
        <tr style="border: 2px solid #000">
            <td style="border: 2px solid #000">2</td>
            <td style="border: 2px solid #000">Menggunakan konsep aljabar linear, sehingga lebih kompleks dan sulit dipecahkan tanpa kunci yang benar.</td>
            <td style="border: 2px solid #000">Tidak tahan terhadap serangan frekuensi karena mengenkripsi beberapa huruf sekaligus.</td>
        </tr>
        <tr style="border: 2px solid #000">
            <td style="border: 2px solid #000">3</td>
            <td style="border: 2px solid #000">Dapat mengenkripsi pesan dalam blok, sehingga lebih efisien untuk pesan panjang</td>
            <td style="border: 2px solid #000">Memerlukan perhitungan matriks dan invers modulo, sehingga lebih kompleks dibandingkan cipher sederhana.</td>
        </tr>
    </table>""",  unsafe_allow_html=True)

    st.markdown("""
    <h6><em>~ ~ Referensi ~ ~<em></h6>
    <div style="display: flex">
    <ul type="none" style="font-size: 14px">
        <li><b>Rinaldi Munir - IF4020 Kriptografi</b>, <em>akses melalui: <a href="https://informatika.stei.itb.ac.id/~rinaldi.munir/Kriptografi/">https://informatika.stei.itb.ac.id/~rinaldi.munir/</a></em><li>
        <li><b>Wikipedia - Lester S.Hill</b>, <em>akses melalui: <a href="https://en.wikipedia.org/wiki/Lester_S._Hill">https://en.wikipedia.org/wiki/Lester_S._Hill</a></em></li>
        <li><b>Geeksforgeeks - Hill Cipher</b>, <em>akses melalui: <a href="https://www.geeksforgeeks.org/dsa/hill-cipher/">https://www.geeksforgeeks.org/dsa/hill-cipher/</a></em></li>
    </ul>
    <img src="https://media.tenor.com/t3D8a8qI1wAAAAAi/cat-like.gif", width=100>
    </div>
    <h6 style="text-align: right"><em>~ ~ Thank You ~ ~<em></h6>
    """, unsafe_allow_html=True)