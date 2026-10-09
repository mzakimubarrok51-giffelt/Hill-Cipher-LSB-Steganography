import streamlit as st
from PIL import Image
from io import BytesIO
from collections import Counter

def extracted():
    x, y = st.columns([0.8, 0.2])
    with x:
        st.title("🔎 Stego Image Analyzer")
        st.markdown("""
        <p>Ekstraksi pesan rahasia dan analisis karakteristik gambar menggunakan metode LSB. 
        <span style="color: red">⚠️ keterbatasan: hanya dapat membaca pesan dengan penanda <b>utf-8</b></span></p>
        """, unsafe_allow_html=True)
    with y:
        st.image("https://media.tenor.com/A-3XvSb8TjoAAAAj/doge-dogelon.gif")

    def extract_message(img):
        bits = []

        for pixel in img.getdata():
            # Urutan harus sama dengan proses embedding: R, G, B
            for channel in pixel[:3]:
                bits.append(str(channel & 1))

        # Gabungkan bit menjadi byte, lalu cari penanda akhir b'\0'
        result = bytearray()

        for i in range(0, len(bits) - 7, 8):
            byte_bits = ''.join(bits[i:i + 8])
            value = int(byte_bits, 2)

            if value == 0:
                try:
                    return result.decode("utf-8"), True
                except UnicodeDecodeError:
                    return (
                        "Data ditemukan, tetapi bukan teks UTF-8 yang valid.",
                        False
                    )

            result.append(value)

        return (
            "Penanda akhir pesan tidak ditemukan. "
            "Gambar mungkin bukan hasil embedding dari program ini.",
            False
        )

    def analyze_lsb(img):
        total_channels = 0
        lsb_ones = 0
        lsb_zeros = 0

        channel_stats = {
            "R": {"0": 0, "1": 0},
            "G": {"0": 0, "1": 0},
            "B": {"0": 0, "1": 0}
        }

        for pixel in img.getdata():
            for index, channel_name in enumerate(["R", "G", "B"]):
                bit = pixel[index] & 1

                total_channels += 1

                if bit == 1:
                    lsb_ones += 1
                    channel_stats[channel_name]["1"] += 1
                else:
                    lsb_zeros += 1
                    channel_stats[channel_name]["0"] += 1

        return {
            "total": total_channels,
            "ones": lsb_ones,
            "zeros": lsb_zeros,
            "ones_pct": lsb_ones / total_channels * 100,
            "zeros_pct": lsb_zeros / total_channels * 100,
            "channels": channel_stats
        }

    uploaded_file = st.file_uploader(
        "Upload gambar yang ingin dianalisis",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:
        raw_bytes = uploaded_file.getvalue()

        try:
            img = Image.open(BytesIO(raw_bytes)).convert("RGB")
        except Exception:
            st.error("File gambar tidak dapat dibaca.")
            st.stop()

        st.divider()

        tab_extract, tab_analyze = st.tabs([
            "🔓 Ekstraksi Pesan",
            "📊 Analisis Gambar"
        ])

        with tab_extract:
            st.subheader("Ekstraksi Pesan Rahasia")

            left, right = st.columns(2)

            with left:
                st.image(img, caption="Gambar yang dianalisis",
                        use_container_width=True)

            with right:
                st.write("**Nama file:**", uploaded_file.name)
                st.write("**Dimensi:**", f"{img.width} × {img.height}")
                st.write("**Format asli:**", 
                        Image.open(BytesIO(raw_bytes)).format or "Tidak diketahui")

                if st.button("Ekstrak Pesan", type="primary"):
                    message, success = extract_message(img)

                    if success:
                        st.success("Penanda akhir pesan ditemukan.")
                        st.text_area(
                            "Pesan hasil ekstraksi",
                            value=message,
                            height=180
                        )
                    else:
                        st.warning(message)

        with tab_analyze:
            st.subheader("Analisis Karakteristik Gambar")

            stats = analyze_lsb(img)

            # Informasi dasar gambar
            st.markdown("### Informasi Gambar")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Lebar", f"{img.width} px")
            col2.metric("Tinggi", f"{img.height} px")
            col3.metric("Total Piksel", f"{img.width * img.height:,}")
            col4.metric("Ukuran File", f"{len(raw_bytes) / 1024:.2f} KB")

            st.markdown("### Distribusi Bit LSB RGB")

            col1, col2 = st.columns(2)

            col1.metric(
                "LSB bernilai 0",
                f"{stats['zeros_pct']:.2f}%",
                f"{stats['zeros']:,} bit"
            )

            col2.metric(
                "LSB bernilai 1",
                f"{stats['ones_pct']:.2f}%",
                f"{stats['ones']:,} bit"
            )

            st.caption(
                "LSB 0 dan LSB 1 dihitung dari seluruh kanal RGB. "
                "Distribusi yang mendekati 50:50 tidak membuktikan "
                "bahwa gambar mengandung pesan rahasia."
            )

            # Tabel per kanal
            st.markdown("### Rincian per Kanal Warna")

            rows = []

            for channel, values in stats["channels"].items():
                total = values["0"] + values["1"]

                rows.append({
                    "Kanal": channel,
                    "LSB 0": values["0"],
                    "LSB 1": values["1"],
                    "Persentase LSB 1": (
                        values["1"] / total * 100
                    )
                })

            st.dataframe(
                rows,
                use_container_width=True,
                hide_index=True
            )

            # Visualisasi distribusi
            st.markdown("### Visualisasi Distribusi LSB")

            st.bar_chart({
                "LSB 0": [
                    stats["channels"][c]["0"] for c in ["R", "G", "B"]
                ],
                "LSB 1": [
                    stats["channels"][c]["1"] for c in ["R", "G", "B"]
                ]
            })

            # Histogram nilai piksel
            st.markdown("### Histogram Intensitas Piksel")

            histogram = Counter(img.getdata())
            st.write(
                "Jumlah warna RGB unik:",
                f"{len(histogram):,}"
            )

            st.info(
                "Analisis ini merupakan pemeriksaan statistik dasar. "
                "Untuk mendeteksi steganografi secara lebih meyakinkan, "
                "diperlukan gambar pembanding atau model steganalisis."
            )