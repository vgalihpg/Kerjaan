echo import streamlit as st > analisis.py
echo st.title("Dashboard Analisis Data E-Commerce") >> analisis.py
echo st.subheader("Pertanyaan 1: Produk apa yang menjadi penjualan terbesar berdasarkan total harga?") >>analisis.py
echo st.image("C:/Users/vgali/Pertanyaan_1.png") >> analisis.py
echo st.subheader("Pertanyaan 2: Produk manakah yang memiliki rating terbaik dan review terbanyak?") >> analisis.py
echo st.image("C:/Users/vgali/Pertanyaan_2.png") >> analisis.py
streamlit run analisis.py
