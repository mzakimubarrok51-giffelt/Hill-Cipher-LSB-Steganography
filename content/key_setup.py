import numpy as np
import streamlit as st


# ─────────────────────────────────────────────────────────────
# Inisialisasi state kunci (dipanggil sekali di awal)
# ─────────────────────────────────────────────────────────────
def init_key_state():
    if "hill_key" not in st.session_state:
        st.session_state["hill_key"] = None


# ─────────────────────────────────────────────────────────────
# Ambil kunci dari state. Return np.array atau None.
# ─────────────────────────────────────────────────────────────
def get_key():
    return st.session_state.get("hill_key", None)


# ─────────────────────────────────────────────────────────────
# UI setup kunci — dipakai di halaman Encryption & Decryption
# ─────────────────────────────────────────────────────────────
def key_setup():
    st.subheader("1. Key Matrix")

    size = st.number_input(
        "Ukuran matriks n × n",
        min_value=2,
        max_value=5,
        value=2,
        step=1,
        key="key_size"
    )

    raw_rows = []
    for i in range(size):
        raw_rows.append(
            st.text_input(
                f"Baris {i + 1} (pisahkan dengan spasi):",
                key=f"key_row_{i}"
            )
        )

    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        simpan = st.button("💾 Simpan Kunci", type="primary", key="save_key_btn")

    # ── Validasi & simpan ──
    if simpan:
        # 1) Baris kosong?
        if any(r.strip() == "" for r in raw_rows):
            st.error(f"⚠️ Lengkapi semua {size} baris terlebih dahulu.")
            return

        # 2) Parsing int
        try:
            rows = [list(map(int, r.split())) for r in raw_rows]
        except ValueError:
            st.error("⚠️ Semua elemen harus berupa bilangan bulat. Contoh: 3 3")
            return

        # 3) Panjang baris seragam?
        if any(len(row) != size for row in rows):
            st.error(f"⚠️ Setiap baris harus memiliki tepat {size} elemen.")
            return

    # ── Tampilkan kunci yang sedang aktif ──
    K = get_key()
    display = r"\begin{bmatrix}"

    for r in K:
        display += " & ".join(map(str, r))
        display += r" \\ "

    display += r"\end{bmatrix}"

    st.latex(display)

    return K