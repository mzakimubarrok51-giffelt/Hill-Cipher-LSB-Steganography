import numpy as np
import streamlit as st
from content.key_setup import key_setup, get_key

def decryption():
    def inverse_matrix(K):def inverse_matrix(K):
    """
    Hitung invers matriks K modulo 26 menggunakan
    rumus: K⁻¹ = (1/det(K)) × adj(K) mod 26

    Return: (K_inv, det, det_inv) atau None jika gagal.
    """
    n = K.shape[0]
    det = int(round(np.linalg.det(K)))

    # Cari invers determinan modulo 26
    det_mod = det % 26
    try:
        det_inv = pow(det_mod, -1, 26)
    except ValueError:
        return None, det, None

    # Hitung matriks kofaktor
    cofactor = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(K, i, axis=0), j, axis=1)
            cofactor[i, j] = ((-1) ** (i + j)) * int(round(np.linalg.det(minor)))

    # Adjoin = transpose dari kofaktor
    adj = cofactor.T

    # K⁻¹ = det_inv × adj mod 26
    K_inv = (det_inv * adj) % 26
    K_inv = np.array(K_inv, dtype=int)

    return K_inv, det, det_inv
        def display_inverse_steps(K, det, det_inv, K_inv):
    st.subheader("3. Invers Matriks K (K⁻¹ mod 26)")

    # Kalau invers tidak ada → hanya tampilkan notifikasi
    if K_inv is None:
        det_mod = det % 26
        st.error(
            f"Matriks K tidak memiliki invers modulo 26 "
            f"(det = {det}, det mod 26 = {det_mod})."
        )
        return

    # Kalau invers ada → hanya tampilkan hasil K⁻¹
    display_matrix(K_inv)

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

    key_setup()
    K = get_key()


    K_inv = None
    if K is not None:
        K_inv, det, det_inv = inverse_matrix(K)
        if K_inv is not None:
            display_inverse_steps(K, det, det_inv, K_inv)

    st.divider()

    st.subheader("2. Ciphertext")
    C = ciphertext_matrix()

    st.divider()

    if st.button("Decrypt", type="primary"):

        if K is None:
            st.error("Key matrix tidak valid.")
            st.stop()

        if K_inv is None:
            st.error("Invers matriks K tidak valid. Tidak dapat mendekripsi.")
            st.stop()

        if len(C) == 0:
            st.error("Ciphertext tidak boleh kosong.")
            st.stop()

        # Decrypt menggunakan K⁻¹ (bukan K)
        P = decrypt(K_inv, C)

        st.subheader("Result Matrix")

        display_matrix(P)
        plaintext = numbers_to_text(P)

        st.subheader("Plaintext")

        st.success(plaintext)