import streamlit as st
from PIL import Image
from io import BytesIO

def embedded():
    x, y = st.columns([0.8, 0.2])
    with x:
        st.title("🏞️ LSB Steganography")
        st.write("Sembunyikan pesan rahasia di dalam gambar.")
    with y:
        st.image("https://media.tenor.com/A-3XvSb8TjoAAAAj/doge-dogelon.gif")

    def binary(plaintext):
        return ''.join(format(byte, "08b")
                    for byte in plaintext.encode("utf-8") + b"\0")

    def modPix(pix, data):
        bits = binary(data)
        pixels = list(pix)

        if len(bits) > len(pixels) * 3:
            raise ValueError("Pesan terlalu panjang untuk gambar ini.")

        bit_index = 0

        for i, pixel in enumerate(pixels):
            if bit_index >= len(bits):
                break

            pixel = list(pixel)

            for channel in range(3):
                if bit_index >= len(bits):
                    break

                pixel[channel] = (
                    (pixel[channel] & 254) | int(bits[bit_index])
                )
                bit_index += 1

            pixels[i] = tuple(pixel)

        return pixels

    def encode_enc(newimg, data):
        pixels = modPix(newimg.getdata(), data)
        newimg.putdata(pixels)
        return newimg

    uploaded_file = st.file_uploader(
        "Upload gambar cover",
        type=["png", "jpg", "jpeg"]
    )

    message = st.text_area(
        "Pesan rahasia",
        placeholder="Masukkan pesan yang ingin disembunyikan..."
    )

    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")

        st.subheader("Gambar asli")
        st.image(img, use_container_width=True)

        capacity = (img.width * img.height * 3) // 8 - 1

        st.caption(
            f"Dimensi: {img.width} × {img.height} piksel | "
            f"Kapasitas pesan sekitar {capacity} byte"
        )

        if st.button("Sisipkan Pesan", type="primary"):
            if not message:
                st.warning("Masukkan pesan terlebih dahulu.")
            elif len(message.encode("utf-8")) + 1 > capacity:
                st.error("Pesan terlalu panjang untuk gambar ini.")
            else:
                stego = encode_enc(img.copy(), message)

                output = BytesIO()
                stego.save(output, format="PNG")
                image_bytes = output.getvalue()

                st.success("Pesan berhasil disisipkan!")

                st.subheader("Stego Image")
                st.image(stego, use_container_width=True)

                st.download_button(
                    "Download Stego Image",
                    data=image_bytes,
                    file_name="stego.png",
                    mime="image/png"
                )