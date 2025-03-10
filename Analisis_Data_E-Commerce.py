import streamlit as st

st.title("Analisis Data E-Commerce")
st.subheader("Tentang data")

with st.expander("Lihat penjelasan tentang data"):
    st.text("Data yang dianalisis merupakan data transaksi e-commerce dari Brasil mulai dari tahun 2016 hingga 2018. Dataset ini disediakan oleh Olist, sebuah perusahaan marketplace di Brasil.")

option = st.radio("Pilih analisis yang ingin ditampilkan", ("Analisis Penjualan", "Analisis Rating & Review"))

if option == "Analisis Penjualan":
    st.subheader("Pertanyaan 1: Produk apa yang menjadi penjualan terbesar berdasarkan total harga?")
    st.image("C:/Users/vgali/Pertanyaan_1.png")
    with st.expander("Lihat penjelasan plot"):
        st.text("Plot di atas dibuat berdasarkan hasil penjualan produk-produk E-Commerce dalam rentang tahun 2016 sampai 2018. Produk dengan ID 'bb50f2...' memiliki total harga tertinggi, menunjukkan bahwa produk ini adalah yang paling menguntungkan dalam hal nilai transaksi selama rentang tahun tersebut.")

elif option == "Analisis Rating & Review":
    st.subheader("Pertanyaan 2: Produk manakah yang memiliki rating terbaik dan review terbanyak?")
    st.image("C:/Users/vgali/Pertanyaan_2.png")
    with st.expander("Lihat penjelasan plot"):
        st.text("Plot di atas dibuat berdasarkan review pelanggan terhadap suatu produk yang sudah direview paling sedikit lima belas kali terhitung dari tahun 2016 hingga 2018. Produk dengan ID '37eb69...' memiliki rating tertinggi, yang berarti para pelanggan sangat puas dengan produk ini sepanjang rentang tahun tersebut.")
