import streamlit as st

st.title("a beautiful blur - LANY")
st.write(
    "Cause You Have To - 2.19."
)
st.image("8b3564ad9388ea28edeb1c6048059eba.jpg", width=200)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.wrute(f"{angka} adalah Bilangan Ganjil")
