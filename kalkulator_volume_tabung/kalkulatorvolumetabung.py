# -*- coding: utf-8 -*-
import streamlit as st
import math

def kalkulator_volume_tabung_streamlit():
    """
    Kalkulator volume tabung menggunakan Streamlit.
    """
    st.title("Kalkulator Volume Tabung 🔎")
    st.write("---")

    st.write("Hai! Mari kita hitung volume tabung bersama-sama.")
    st.write("Sebelum itu, tahukah kamu apa itu tabung?")
    st.info("💡 Bayangkan sebuah kaleng susu atau pipa. Itu adalah contoh tabung.")
    st.write("Tabung memiliki dua bagian utama: **alas** (lingkaran) dan **tinggi**.")

    st.write("---")
    st.subheader("Langkah 1: Memahami Luas Alas")
    st.write("Nah, mari kita pikirkan tentang alasnya.")
    st.write("Alas tabung berbentuk lingkaran. Bagaimana kita menghitung **luas sebuah lingkaran**?")
    st.write("Ingat rumus luas lingkaran? Itu melibatkan 'pi' (sekitar 3.14 atau 22/7) dan jari-jari.")
    st.markdown("Luas Lingkaran = $\\pi \\times \\text{jari-jari} \\times \\text{jari-jari}$")
    st.markdown("Atau, Luas Lingkaran = $\\pi r^2$")

    st.write("---")
    st.subheader("Langkah 2: Masukkan Jari-jari dan Tinggi Tabung")

    # Input Jari-jari
    jari_jari = st.number_input("Masukkan panjang **jari-jari** alas tabung (misal: cm)", min_value=0.0, value=7.0, step=0.1, format="%.2f")
    if jari_jari <= 0:
        st.warning("Jari-jari harus lebih besar dari nol.")
        return # Menghentikan eksekusi jika input tidak valid

    # Input Tinggi
    tinggi = st.number_input("Masukkan **tinggi** tabung (dalam satuan yang sama dengan jari-jari)", min_value=0.0, value=10.0, step=0.1, format="%.2f")
    if tinggi <= 0:
        st.warning("Tinggi harus lebih besar dari nol.")
        return # Menghentikan eksekusi jika input tidak valid

    st.write(f"Oke, kita punya **jari-jari**: `{jari_jari}` dan **tinggi**: `{tinggi}`")

    st.write("---")
    st.subheader("Langkah 3: Perhitungan")

    if st.button("Hitung Volume!"):
        # Menentukan nilai pi yang paling sesuai
        selected_pi = 0
        pi_str = ""
        # Cek apakah jari-jari atau tinggi merupakan kelipatan 7
        if jari_jari % 7 == 0 or tinggi % 7 == 0:
            selected_pi = 22/7
            pi_str = "22/7"
        else:
            selected_pi = 3.14
            pi_str = "3.14"

        st.info(f"Menggunakan nilai $\\pi$ = **{pi_str}**")

        # Menghitung luas alas
        st.write("### Menghitung Luas Alas Tabung")
        luas_alas = selected_pi * (jari_jari ** 2)
        st.write(f"Menggunakan rumus **Luas Lingkaran** = $\\pi \\times r^2$")
        st.success(f"Luas Alas = `{selected_pi:.4f}` * `{jari_jari}`^2 = `{luas_alas:.2f}` satuan persegi.")

        st.write("### Menghitung Volume Tabung")
        st.write("Bayangkan luas alas itu seperti 'tumpukan' koin.")
        st.write("Jika kita menumpuk 'luas alas' itu setinggi 'tinggi' tabung, kita akan mendapatkan volumenya!")
        st.markdown("Jadi, **Volume Tabung** = **Luas Alas** $\\times$ **Tinggi**")

        volume = luas_alas * tinggi
        st.success(f"Volume Tabung = `{luas_alas:.2f}` * `{tinggi:.2f}` = `{volume:.2f}` satuan kubik.")

        st.balloons()
        st.write("---")
        st.subheader("Selamat!")
        st.write("Anda telah berhasil menghitung volume tabung.")
        st.write(f"Dengan jari-jari **{jari_jari}** dan tinggi **{tinggi}**,")
        st.success(f"Volume tabung adalah: **{volume:.2f}** satuan kubik.")

if __name__ == "__main__":
    kalkulator_volume_tabung_streamlit()
