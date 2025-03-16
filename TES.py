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
    
    st.subheader("📦 Analisis Penjualan Produk")
    file_path_items = "https://raw.githubusercontent.com/vgalihpg/Kerjaan/refs/heads/main/olist_order_items_dataset.csv"
    df_items = pd.read_csv(file_path_items)
    
    product_sales = df_items.groupby("product_id").agg(
        quantity_sold=("order_id", "count"),
        unit_price=("price", "mean")
    ).reset_index()

    total_sold_products = product_sales["product_id"].nunique()
    st.metric(label="Total Jenis Produk Terjual", value=total_sold_products)

    min_price, max_price = st.slider("Filter Produk berdasarkan Harga Satuan", float(product_sales["unit_price"].min()), float(product_sales["unit_price"].max()), (float(product_sales["unit_price"].min()), float(product_sales["unit_price"].max())))
    filtered_sales = product_sales[(product_sales["unit_price"] >= min_price) & (product_sales["unit_price"] <= max_price)]

    st.write("### Data Penjualan Per Produk")
    st.dataframe(filtered_sales, use_container_width=True)

    csv_sales = filtered_sales.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Data Penjualan", data=csv_sales, file_name="product_sales.csv", mime="text/csv")

elif option == "Analisis Rating & Review":
    st.subheader("Pertanyaan 2: Produk manakah yang memiliki rating terbaik dan review terbanyak?")
    st.image("https://raw.githubusercontent.com/vgalihpg/Kerjaan/refs/heads/main/Pertanyaan_2.png")
    with st.expander("Lihat penjelasan plot"):
        st.text("Plot di atas dibuat berdasarkan review pelanggan terhadap suatu produk yang sudah direview paling sedikit lima belas kali terhitung dari tahun 2016 hingga 2018. Produk dengan ID '37eb69...' memiliki rating tertinggi, yang berarti para pelanggan sangat puas dengan produk ini sepanjang rentang tahun tersebut.")
    
    file_path_reviews = "https://raw.githubusercontent.com/vgalihpg/Kerjaan/refs/heads/main/olist_order_reviews_dataset.csv"
    df_reviews = pd.read_csv(file_path_reviews)
    file_path_items = "https://raw.githubusercontent.com/vgalihpg/Kerjaan/refs/heads/main/olist_order_items_dataset.csv"
    df_items = pd.read_csv(file_path_items)
    
    df_merged = df_reviews.merge(df_items, on="order_id", how="inner")

    total_products = df_merged["product_id"].nunique()
    
    review_stats = df_merged.groupby("product_id").agg(
        total_reviews=("review_id", "count"),
        avg_rating=("review_score", "mean")
    ).reset_index()

    st.subheader("📊 Dashboard Analisis Review Produk")

    st.metric(label="Total Jenis Produk Unik", value=total_products)

    min_reviews = st.slider("Filter Produk dengan Minimal Jumlah Review", 1, 250, 50)
    filtered_data = review_stats[review_stats["total_reviews"] >= min_reviews]

    st.write("### Data Review Per Produk")
    st.dataframe(filtered_data, use_container_width=True)

    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Data", data=csv, file_name="review_stats.csv", mime="text/csv")
