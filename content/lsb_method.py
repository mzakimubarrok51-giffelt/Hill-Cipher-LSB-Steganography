import streamlit as st


def lsb():
    # ── Load CSS ──
    with open("style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # ── Header ──
    st.html("""
    <h4>🏞️ LSB (Least Significant Bit)</h4>
    <div style="display: flex; margin-bottom: 10px">
        <img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*4rATbGfDEv74zNtKk2HwyQ.png">
    </div>
    <p>
        <b>LSB</b> adalah salah satu metode steganografi yang digunakan untuk menyembunyikan pesan rahasia ke dalam media digital,
        misalnya gambar, dengan cara mengubah bit paling tidak signifikan dari nilai piksel. Ada dua konsep yang perlu dibedakan:
    </p>
    <ol>
        <li><b>Kriptografi:</b> mengubah pesan agar isinya tidak dapat dipahami tanpa kunci yang sesuai.</li>
        <li><b>Steganografi:</b> menyembunyikan keberadaan pesan agar orang lain tidak menyadari bahwa ada pesan rahasia.</li>
    </ol>
    <p>
        LSB termasuk steganografi, bukan algoritma enkripsi. Pesan yang disisipkan tidak otomatis terenkripsi.
    </p>
    """)

    # ── Konsep LSB ──
    st.html("""
    <h4>📖 Memahami Konsep Least Significant Bit</h4>
    <div style="display: flex; justify-content: space-between">
        <div>
            <p>
                Komputer menyimpan nilai warna piksel gambar dalam bentuk
                bilangan biner. Pada gambar RGB, setiap piksel umumnya memiliki
                tiga komponen warna:
            </p>
            <ul>
                <li style="background-color: red;"><span style="color: #ffffff"><strong>R (Red)</strong> — merah.</span></li>
                <li style="background-color: green;"><span style="color: #ffffff"><strong>G (Green)</strong> — hijau.</span></li>
                <li style="background-color: blue;"><span style="color: #ffffff"><strong>B (Blue)</strong> — biru.</span></li>
            </ul>
        </div>
        <img src="https://www.designyourway.net/blog/wp-content/uploads/2024/06/rgb-colors-and-additive-color-mixing.jpg" width="350">
    </div>
    <p>
        Masing-masing komponen biasanya memiliki nilai 0 sampai 255
        yang direpresentasikan menggunakan 8 bit. <b>Contoh bilangan desimal 150 dalam biner</b>
    </p>
    <div style="text-align: center; font-size: 24px">
        <b>150</b> = 10010110<sub>2</sub>
    </div>
    <p>
        Susunan bit dari kiri ke kanan adalah sebagai berikut:
    </p>
    """)

    st.image("assets/lsb1.png")

    st.html("""
    <p>
        LSB adalah bit paling kanan, yaitu bit dengan bobot nilai 1.
        Perubahan bit tersebut hanya mengubah nilai desimal sebesar 1.
    </p>
    <div style="text-align: center; font-size: 24px">
        10010110 = <b>150</b> &#10140; 10010111 = <b>151</b>
    </div>
    <p>
        Karena perubahan nilai warna sekecil ini umumnya sulit dilihat,
        bit tersebut dapat dimanfaatkan untuk menyisipkan informasi
        rahasia.
    </p>
    """)

    # ── Cara Kerja LSB ──
    st.html("<h4>🙋‍♂️ Bagaimana cara kerja LSB?</h4>")
    st.html("<p>Secara umum, proses LSB terdiri dari tiga tahap.</p>")

    # Card 1
    st.html("""
    <div class="dark-card" style="background-color: #000; display: flex; border-radius: 10px; padding: 10px; margin-bottom: 10px;">
        <img src="https://images.openai.com/static-rsc-4/vYfLkrbI7PFINKDmtp-Tr0kvNqzuoA2ve13bvw7sMeW07DTUR76GZ1ze_gpNkVC6GsGlbvpDcQMpdorer71y8p5W7vGsZeSTYckf2UuuPiufg85qOaYTn3NHbsqUt41ARPDRIVnlXdiHUQvdgz9t7dCCYSwf3q1ddd1lz12IBpsx4Bd4vz2SJo_cINAeKpFt?purpose=fullsize"
            width="110" style="margin-left: 10px;">
        <div style="margin-left: 10px">
            <b class="card-title">1. Menyiapkan cover image</b>
            <p>Gambar asli yang akan digunakan sebagai media penyisipan pesan. Gambar ini disebut <em>cover image.</em></p>
        </div>
    </div>
    """)

    # Arrow
    st.html('<div style="font-size: 50px; text-align: center; color: #000;">&#11015;</div>')

    # Card 2
    st.html("""
    <div class="dark-card" style="background-color: #000; display: flex; border-radius: 10px; padding: 10px; margin-bottom: 10px;">
        <img src="https://images.openai.com/static-rsc-4/x53CBMsL8LDuL8C1s4uW2Y84W4eZb-h9zrdC-HcHmsfhVf1md2iCNt6Yz6nh2P_Hg1I2fy69XI72s658LKaFZB7RjXpmRl-YAJfGeUv-C2NIJ0Ygea7A1PbpOiY0aqOHOXSlHiQe_sJ_I88kZD93Z7ufxy8oxSdWO8B0HRuJjKYsjWPPHkQSHDIgorzr_OlV?purpose=fullsize"
            width="110" style="margin-left: 10px;">
        <div style="margin-left: 10px">
            <b class="card-title">2. Menyisipkan pesan</b>
            <p>Pesan diubah menjadi bit 0 dan 1. Bit pesan kemudian digunakan untuk mengganti LSB dari nilai piksel gambar.</p>
        </div>
    </div>
    """)

    # Arrow
    st.html('<div style="font-size: 50px; text-align: center; color: #000;">&#11015;</div>')

    # Card 3
    st.html("""
    <div class="dark-card" style="background-color: #000; display: flex; border-radius: 10px; padding: 10px; margin-bottom: 10px;">
        <img src="https://images.openai.com/static-rsc-4/6kOJAJW4C8IQkD_f26P3shqn4sOOb02oKIi8V67YDsfgCeWWEE1xQ-Tdi8c3xZu2UrBhy6EhILnP81-6bI16lpKgfXy75DZ-V819Ezq3VnH8l5SIw_HoIYP1rtpKheNrB_FYpUU-p-nxCBVZVXlOlOcwa4ynaeo8iKBbbYG4shcuAcVi9i5Q3ptsO1mxcUWk?purpose=fullsize"
            width="110" style="margin-left: 10px;">
        <div style="margin-left: 10px">
            <b class="card-title">3. Menghasilkan stego image</b>
            <p>Gambar hasil penyisipan disebut <em>stego image.</em> Penerima membaca kembali bit-bit yang telah disisipkan untuk mendapatkan pesan.</p>
        </div>
    </div>
    """)

    # ── Ekstraksi Pesan ──
    st.html("""
    <h4>🙋🏻‍♀️ Lalu bagaimana proses ekstraksi pesan?</h4>
    <p>
        Ekstraksi adalah proses mengambil pesan dari stego image.
        Jika penyisipan menggunakan LSB dari delapan komponen warna secara berurutan, penerima melakukan langkah berikut:
    </p>
    <ol>
        <li>Membaca komponen piksel sesuai urutan penyisipan.</li>
        <li>Mengambil bit paling kanan dari setiap komponen.</li>
        <li>Menggabungkan bit menjadi kelompok delapan bit.</li>
        <li>Mengubah kelompok biner menjadi karakter.</li>
    </ol>
    <p><b>Contohnya:</b></p>
    <div style="text-align: center; font-size: 24px">
        <b>01000001<sub>2</sub></b> &#10140; A
    </div>
    <p>
        Pada metode LSB sederhana, penerima perlu mengetahui aturan urutan piksel dan jumlah bit yang dibaca.
        Informasi panjang pesan juga perlu ditentukan, misalnya disimpan sebagai header atau ditetapkan sebelumnya.
    </p>
    """)

    # ── Kapasitas ──
    st.html("""
    <h4>🙋‍♂️ Berapa banyak pesan yang dapat disisipkan?</h4>
    <p>
        Untuk gambar RGB berukuran W × H, jika setiap komponen warna menyimpan satu bit pesan,
        kapasitas teoritisnya adalah:
    </p>
    """)

    st.latex(r"""
    \large\begin{aligned}
        C &= W \times H \times 3 \text{ bit}
    \end{aligned}
    """)

    st.html("""
    <p>
        Karena satu karakter ASCII umumnya membutuhkan 8 bit, perkiraan kapasitas karakter adalah:
    </p>
    """)

    st.latex(r"""
    \begin{aligned}
        N &= \frac{W \times H \times 3}{8}
    \end{aligned}
    """)

    st.html("""
    <p>
        Contoh gambar berukuran 100 × 100 piksel:
    </p>
    <ol>
        <li>Jumlah piksel: 10.000</li>
        <li>Komponen warna: 30.000</li>
        <li>Kapasitas teoritis: 30.000 bit</li>
        <li>Kapasitas karakter 8-bit: sekitar 3.750 karakter</li>
    </ol>
    <p>
        Angka tersebut adalah kapasitas maksimum teoritis untuk skema satu LSB per komponen RGB,
        sebelum memperhitungkan header, penanda akhir pesan, atau kebutuhan lain.
    </p>
    """)

    # ── Jenis-jenis LSB ──
    st.html('<h4>📌 Jenis-jenis metode LSB</h4>')

    # Card A — LSB Replacement
    st.html("""
    <div style="background-color: rgb(225, 225, 225); display: flex; border-radius: 10px; margin-bottom: 10px; color: #000;">
        <img src="https://images.openai.com/static-rsc-4/IzK5aceiP0Mw2tU6zLjT0TskTUiGISmB-H8jnBTRHSCclwYqGy-_M_N94nHgZ7a87Tqr0E4hBohDMsD2YGe5kNIEAiyqlTFIJ4pl7weThXSEvCZy8g00LHFyAo_KrlMKmPCDlWdCG6kjek6aOhVF0FzTJQ94zHiNTaJMp3bkKrga9nh08YbsALccccuBhEdG?purpose=fullsize"
            width="150" style="margin-left: 10px;">
        <div style="margin-left: 10px">
            <b style="background-color: #000; color: #ffffff;">A. LSB Replacement</b>
            <p>
                LSB piksel langsung diganti dengan bit pesan. Jika bitnya berbeda, nilai komponen warna berubah sebesar 1.
            </p>
            <p style="background-color: #ffffff">
                <em style="font-size: 12px"><b>Kelebihan:</b> sederhana, cepat, mudah diimplementasikan.</em>
            </p>
        </div>
    </div>
    """)

    # Card B — LSB Matching
    st.html("""
    <div style="background-color: rgb(225, 225, 225); display: flex; border-radius: 10px; margin-top: 10px; color: #000;">
        <img src="https://images.openai.com/static-rsc-4/bY_Pt1NL4hYr2V5weCbZDB4zZg4NKOYDV9ulxXYonPa4CFZTkw-skSB1tbFlbAjfWW5u2Tc7OcfXDnonBW2Bune6_YBzTJRlfAPBPXNTmZS77YIJGIfFHTgUwecQHlzooFq88faTL5EbBclLStFZcFISMnVuzc0pHST-M26yrT_1916MPUJuK9n_6pHQJifB?purpose=fullsize"
            width="150" style="margin-left: 10px;">
        <div style="margin-left: 10px">
            <b style="background-color: #000; color: #ffffff">B. LSB Matching</b>
            <p>
                Jika LSB tidak sesuai, nilai piksel dinaikkan atau diturunkan satu secara acak atau berdasarkan aturan tertentu.
                Metode ini tidak sekadar langsung mengganti bit paling kanan.
            </p>
            <p style="background-color: #ffffff">
                <em style="font-size: 12px"><b>Kelebihan:</b> ketahanan lebih baik, menghasilkan perubahan statistik yang berbeda dari LSB Replacement.</em>
            </p>
        </div>
    </div>
    """)

    # Card C — Adaptive / Edge-Based
    st.html("""
    <div style="background-color: rgb(225, 225, 225); display: flex; border-radius: 10px; margin-top: 10px; color: #000;">
        <img src="https://images.openai.com/static-rsc-4/132wmsEVQ2Z6SQL5j9QRLCS1v8r-_u_PVKqK12OEpggl_YnHxOUPsh68brMIYFrD0-jbkJjajFyD_SK3RnqXVS2l5kWUD_HOAKGkAoyMBmhSWf5O8JlusKIyM7haqGBimmcMI4NBlJBA8-k6s75DP7GB6PQyvtAib9Ggq8_WRCRqo4AcjsRBcB3Etz3MNJ3b?purpose=fullsize"
            width="150" style="margin-left: 10px;">
        <div style="margin-left: 10px">
            <b style="background-color: #000; color: #ffffff">C. Adaptive atau Edge-Based LSB</b>
            <p>
                Penyisipan diprioritaskan pada bagian gambar yang memiliki banyak detail atau tepi.
                Bagian tersebut sering lebih toleran terhadap perubahan kecil dibanding area yang halus.
            </p>
            <p style="background-color: #ffffff">
                <em style="font-size: 12px"><b>Kelebihan:</b> dapat mengatur penyisipan sesuai karakteristik gambar, tetapi membutuhkan logika tambahan.</em>
            </p>
        </div>
    </div>
    """)

    # ── Tabel Kelebihan & Kekurangan ──
    st.html("""
    <h4>📝 Kelebihan dan kekurangan LSB</h4>
    <table style="width: 100%; border-collapse: collapse;">
        <tr style="border: 2px solid #000; background-color: blue; color: #ffffff">
            <th style="border: 2px solid #000; padding: 6px;">No</th>
            <th style="border: 2px solid #000; padding: 6px;">Kelebihan</th>
            <th style="border: 2px solid #000; padding: 6px;">Kekurangan</th>
        </tr>
        <tr style="border: 2px solid #000">
            <td style="border: 2px solid #000; padding: 6px;">1</td>
            <td style="border: 2px solid #000; padding: 6px;">Mudah dipahami dan diimplementasikan</td>
            <td style="border: 2px solid #000; padding: 6px;">Dapat dideteksi melalui analisis statistik</td>
        </tr>
        <tr style="border: 2px solid #000">
            <td style="border: 2px solid #000; padding: 6px;">2</td>
            <td style="border: 2px solid #000; padding: 6px;">Proses penyisipan dan ekstraksi relatif cepat</td>
            <td style="border: 2px solid #000; padding: 6px;">Tidak otomatis mengenkripsi pesan</td>
        </tr>
        <tr style="border: 2px solid #000">
            <td style="border: 2px solid #000; padding: 6px;">3</td>
            <td style="border: 2px solid #000; padding: 6px;">Perubahan visual biasanya kecil</td>
            <td style="border: 2px solid #000; padding: 6px;">Rentan terhadap kompresi JPEG dan manipulasi gambar</td>
        </tr>
        <tr style="border: 2px solid #000">
            <td style="border: 2px solid #000; padding: 6px;">4</td>
            <td style="border: 2px solid #000; padding: 6px;">Kapasitas cukup besar pada gambar RGB</td>
            <td style="border: 2px solid #000; padding: 6px;">Dapat merusak pesan jika piksel yang digunakan berubah</td>
        </tr>
    </table>
    """)

    # ── Referensi ──
    st.html("""
    <h6><em>~ ~ Referensi ~ ~</em></h6>
    <ul type="none" style="font-size: 14px">
        <li><b>Rinaldi Munir - IF4020 Kriptografi</b>, <em>akses melalui: <a href="https://informatika.stei.itb.ac.id/~rinaldi.munir/Kriptografi/">https://informatika.stei.itb.ac.id/~rinaldi.munir/</a></em></li>
        <li><b>Yashikamahawar - Image Steganography Using LSB Technique in Python</b>, <em>akses melalui: <a href="https://medium.com/%40yashikamahawar1805/image-steganography-using-lsb-technique-in-python-f2fe7cccc49f">https://yashikamahawar/image-lsb-in-python/</a></em></li>
        <li><b>Geeksforgeeks - Image Based Steganography Python</b>, <em>akses melalui: <a href="https://www.geeksforgeeks.org/python/image-based-steganography-using-python/">https://geeksforgeeks.org/python/image-based-steganography/</a></em></li>
        <li><b>TextStudio - What Is Steganography?</b>, <em>akses melalui: <a href="https://www.textstudio.com/hide-text-in-image">https://www.textstudio.com/hide-text-in-image</a></em></li>
        <li><b>RRST - Image Steganography Explained: Hide Messages in Pictures</b>, <em>akses melalui: <a href="https://www.redsecuretech.co.uk/blog/post/image-steganography-explained-hide-messages-in-pictures/1063">https://redsecuretech.co.uk/image-steganography-explained/</a></em></li>
        <li><b>Scientific Reports - An improved hybrid image steganography method using AES algorithm</b>, <em>akses melalui: <a href="https://www.nature.com/articles/s41598-025-28140-0">https://nature.com/articles/</a></em></li>
    </ul>
    <h6 style="text-align: right"><em>~ ~ Thank You ~ ~</em></h6>
    """)