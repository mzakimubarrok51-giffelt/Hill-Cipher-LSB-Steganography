import numpy as np
import streamlit as st

def encryption():
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

    def plaintext_matrix():
        text = st.text_area(
            "Ketik plaintext:",
            placeholder="Masukkan pesan yang ingin dienkripsi.."
        ).upper()

        plaintext = np.array([
            ord(char) - ord("A")
            for char in text
            if char.isalpha()
        ])

        if len(plaintext) > 0:
            display = r"\begin{bmatrix}"
            display += " & ".join(map(str, plaintext))
            display += r"\end{bmatrix}"

            st.latex(display)

        return plaintext

    def encrypt(key, plaintext):
        n = key.shape[0]

        if len(plaintext) % n != 0:
            padding = n - (len(plaintext) % n)

            plaintext = np.append(
                plaintext,
                [23] * padding
            )

        ciphertext = []

        for i in range(0, len(plaintext), n):

            block = plaintext[i:i + n]

            block = block.reshape(n, 1)

            # C = K × P mod 26
            encrypted = (key @ block) % 26

            ciphertext.extend(encrypted.flatten())

        return np.array(ciphertext)

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
        st.header("🔐 Hill Cipher Encryption")
        st.write(
            "Enkripsikan pesan rahasia "
            "menggunakan metode Hill Cipher."
        )
    with y: 
        st.image("https://media.tenor.com/QhRvvwpCdVoAAAAi/rocket.gif")

    st.subheader("1. Key Matrix")
    K = key_matrix()

    st.subheader("2. Plaintext")
    P = plaintext_matrix()

    st.divider()

    if st.button("Encrypt", type="primary"):

        if K is None:
            st.error("Key matrix tidak valid.")
            st.stop()

        if len(P) == 0:
            st.error("Plaintext tidak boleh kosong.")
            st.stop()

        # Encrypt
        C = encrypt(K, P)

        st.subheader("Result Matrix")

        display_matrix(C)
        ciphertext = numbers_to_text(C)

        st.subheader("Ciphertext")

        st.success(ciphertext)