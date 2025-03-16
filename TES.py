import streamlit as st
import pandas as pd

st.title("Analisis Data E-Commerce")
st.subheader("Tentang data")

with st.expander("Lihat penjelasan tentang data"):
    st.text("Data yang dianalisis merupakan data transaksi e-commerce dari Brasil mulai dari tahun 2016 hingga 2018. Dataset ini disediakan oleh Olist, sebuah perusahaan marketplace di Brasil.")

option = st.radio("Pilih analisis yang ingin ditampilkan", ("Analisis Penjualan", "Analisis Rating & Review"))

if option == "Analisis Penjualan":
    st.subheader("Pertanyaan 1: Produk apa yang menjadi penjualan terbesar berdasarkan total harga?")
    st.image("https://raw.githubusercontent.com/vgalihpg/Kerjaan/refs/heads/main/Pertanyaan_1.png")
    with st.expander("Lihat penjelasan plot"):
        st.text("Plot di atas dibuat berdasarkan hasil penjualan produk-produk E-Commerce dalam rentang tahun 2016 sampai 2018. Produk dengan ID 'bb50f2...' memiliki total harga tertinggi, menunjukkan bahwa produk ini adalah yang paling menguntungkan dalam hal nilai transaksi selama rentang tahun tersebut.")

elif option == "Analisis Rating & Review":
    st.subheader("Pertanyaan 2: Produk manakah yang memiliki rating terbaik dan review terbanyak?")
    st.image("https://raw.githubusercontent.com/vgalihpg/Kerjaan/refs/heads/main/Pertanyaan_2.png")
    with st.expander("Lihat penjelasan plot"):
        st.text("Plot di atas dibuat berdasarkan review pelanggan terhadap suatu produk yang sudah direview paling sedikit lima belas kali terhitung dari tahun 2016 hingga 2018. Produk dengan ID '37eb69...' memiliki rating tertinggi, yang berarti para pelanggan sangat puas dengan produk ini sepanjang rentang tahun tersebut.")

# Load dataset ulasan
file_path_reviews = "/mnt/data/olist_order_reviews_dataset.csv"
df_reviews = pd.read_csv(file_path_reviews)

# Load dataset produk dalam pesanan
file_path_items = "/mnt/data/olist_order_items_dataset.csv"
df_items = pd.read_csv(file_path_items)

# Gabungkan dataset berdasarkan order_id
df_merged = df_reviews.merge(df_items, on="order_id", how="inner")

# Hitung jumlah jenis produk unik
total_products = df_merged["product_id"].nunique()

# Hitung jumlah review & rata-rata rating per produk
review_stats = df_merged.groupby("product_id").agg(
    total_reviews=("review_id", "count"),
    avg_rating=("review_score", "mean")
).reset_index()

st.subheader("📊 Dashboard Analisis Review Produk")

# Menampilkan total produk unik
st.metric(label="Total Jenis Produk Unik", value=total_products)

# Filter interaktif berdasarkan jumlah minimum review
min_reviews = st.slider("Filter Produk dengan Minimal Jumlah Review", 1, 50, 5)
filtered_data = review_stats[review_stats["total_reviews"] >= min_reviews]

# Menampilkan tabel data yang dapat dieksplorasi
st.write("### Data Review Per Produk")
st.dataframe(filtered_data, use_container_width=True)

# Tambahkan opsi download data
csv = filtered_data.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Data", data=csv, file_name="review_stats.csv", mime="text/csv")
