import numpy as np
import streamlit as st

def decryption():
    def key_matrix():
        size = st.number_input(
            "Ukuran matriks n × n ",
            min_value=2,
            max_value=5,
            value=2,
            step=1
        )

        key = np.array([
            list(map(int, st.text_input(
                f"Ketik element baris {i + 1} pisahkan dengan spasi:",
                key=f"key_row_{i}"
            ).split()))
            for i in range(size)
        ])

        # Cek ukuran matriks
        if any(len(row) != size for row in key):
            st.error(f"Setiap baris harus memiliki {size} elemen.")
            return None

        # Tampilkan matriks
        display = r"\begin{bmatrix}"

        for r in key:
            display += " & ".join(map(str, r))
            display += r" \\ "

        display += r"\end{bmatrix}"

        st.latex(display)

        return key

    def ciphertext_matrix():
        text = st.text_area(
            "Ketik ciphertext:",
            placeholder="Masukkan pesan yang ingin dideskripsi.."
        ).upper()

        ciphertext = np.array([
            ord(char) - ord("A")
            for char in text
            if char.isalpha()
        ])

        if len(ciphertext) > 0:
            display = r"\begin{bmatrix}"
            display += " & ".join(map(str, ciphertext))
            display += r"\end{bmatrix}"

            st.latex(display)

        return ciphertext

    def decrypt(key, ciphertext):
        n = key.shape[0]

        if len(ciphertext) % n != 0:
            padding = n - (len(ciphertext) % n)

            ciphertext = np.append(
                ciphertext,
                [23] * padding
            )

        plaintext = []

        for i in range(0, len(ciphertext), n):

            block = ciphertext[i:i + n]

            block = block.reshape(n, 1)

            # P = K^-1 × C mod 26
            decrypted = (key @ block) % 26

            plaintext.extend(decrypted.flatten())

        return np.array(plaintext)

    def numbers_to_text(numbers):

        return "".join(
            chr(int(number) + ord("A"))
            for number in numbers
        )

    def display_matrix(matrix):

        display = r"\begin{bmatrix}"
        
        # Jika vector
        if matrix.ndim == 1:
            display += " & ".join(map(str, matrix))

        # Jika matrix
        else:
            for r in matrix:
                display += " & ".join(map(str, r))
                display += r" \\ "

        display += r"\end{bmatrix}"

        st.latex(display)

    x, y = st.columns([0.8, 0.2])
    with x:
        st.header("🔓 Hill Cipher Decryption")
        st.write(
            "Deskripsikan pesan rahasia "
            "hasil enkripsi Hill Cipher."
        )
    with y: 
        st.image("https://media.tenor.com/QhRvvwpCdVoAAAAi/rocket.gif")

    st.subheader("1. Key Matrix")
    K = key_matrix()

    st.subheader("2. Ciphertext")
    C = ciphertext_matrix()

    st.divider()

    if st.button("Decrypt", type="primary"):

        if K is None:
            st.error("Key matrix tidak valid.")
            st.stop()

        if len(C) == 0:
            st.error("Ciphertext tidak boleh kosong.")
            st.stop()

        # Decrypt
        P = decrypt(K, C)

        st.subheader("Result Matrix")

        display_matrix(P)
        plaintext = numbers_to_text(P)

        st.subheader("Plaintext")

        st.success(plaintext)