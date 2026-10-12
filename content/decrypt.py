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

    def inverse_matrix(K):
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
            st.error(
                f"Determinan = {det} (mod 26 = {det_mod}) "
                f"tidak memiliki invers modulo 26. "
                f"Matriks K tidak dapat di-invers."
            )
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

        st.markdown(
            "Rumus invers matriks modulo 26:"
        )
        st.latex(
            r"K^{-1} = \dfrac{1}{\det(K)} \cdot \text{adj}(K) \pmod{26}"
        )

        # Tampilkan determinan
        col1, col2 = st.columns(2)
        with col1:
            st.metric("det(K)", det)
        with col2:
            st.metric("det(K)⁻¹ mod 26", det_inv)

        # Tampilkan K⁻¹
        st.markdown("**Hasil K⁻¹:**")
        display_matrix(K_inv)

        # Verifikasi K · K⁻¹ ≡ I (mod 26)
        st.markdown("**Verifikasi:** $K \\cdot K^{-1} \\pmod{26}$")
        identity_check = (K @ K_inv) % 26
        display_matrix(identity_check)

        if np.array_equal(identity_check, np.eye(K.shape[0], dtype=int)):
            st.success("Verifikasi berhasil: K · K⁻¹ = I (mod 26)")
        else:
            st.warning(
                "Hasil perkalian bukan matriks identitas. "
                "Periksa kembali matriks K."
            )

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