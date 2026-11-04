import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman Dashboard
st.set_page_config(
    page_title="Dashboard Analisis Performa UMKM",
    page_icon="📊",
    layout="wide"
)

# 2. Memuat & Membersihkan Dataset (Konversi Angka)
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('dataset/datase_usaha.csv')
    except Exception:
        df = pd.read_csv('datase_usaha.csv')
        
    # Konversi kolom-kolom angka yang terbaca sebagai string ke numerik
    num_cols = [
        'omset', 'aset', 'laba', 'biaya_karyawan', 
        'tenaga_kerja_perempuan', 'tenaga_kerja_laki_laki', 
        'kapasitas_produksi', 'tahun_berdiri', 'jumlah_pelanggan'
    ]
    
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    return df

df = load_data()

# 3. Sidebar - Filter Interaktif
st.sidebar.header("🔍 Filter Data UMKM")

jenis_usaha_list = df['jenis_usaha'].dropna().unique().tolist()
selected_jenis = st.sidebar.multiselect(
    "Pilih Jenis Usaha:",
    options=jenis_usaha_list,
    default=jenis_usaha_list
)

marketplace_list = df['marketplace'].dropna().unique().tolist()
selected_market = st.sidebar.multiselect(
    "Pilih Marketplace:",
    options=marketplace_list,
    default=marketplace_list
)

df_filtered = df[
    (df['jenis_usaha'].isin(selected_jenis)) &
    (df['marketplace'].isin(selected_market))
]

# 4. Header & Title
st.title("📊 Dashboard Visualisasi Data Performa UMKM")
st.markdown("---")

# 5. Komponen KPI Cards (3 Kartu Utama)
col1, col2, col3 = st.columns(3)

total_omset = df_filtered['omset'].sum()
avg_omset = df_filtered['omset'].mean()
total_umkm = len(df_filtered)

col1.metric(label="Total Omset (Rp)", value=f"Rp {total_omset:,.0f}")
col2.metric(label="Rata-rata Omset (Rp)", value=f"Rp {avg_omset:,.0f}")
col3.metric(label="Total Usaha (UMKM)", value=f"{total_umkm:,}")

st.markdown("---")

# 6. Variasi Visualisasi (4 Jenis Bagan)
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("1. Total Omset per Jenis Usaha (Bar Chart)")
    omset_by_jenis = df_filtered.groupby('jenis_usaha')['omset'].sum().reset_index()
    fig_bar = px.bar(
        omset_by_jenis, 
        x='jenis_usaha', 
        y='omset',
        color='jenis_usaha',
        labels={'jenis_usaha': 'Jenis Usaha', 'omset': 'Total Omset (Rp)'},
        template="plotly_white"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with row1_col2:
    st.subheader("2. Distribusi UMKM di Marketplace (Pie Chart)")
    fig_pie = px.pie(
        df_filtered, 
        names='marketplace', 
        hole=0.4,
        title="Persentase Sebaran Marketplace",
        template="plotly_white"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("3. Pertumbuhan UMKM Berdasarkan Tahun Berdiri (Line Chart)")
    umkm_per_tahun = df_filtered.groupby('tahun_berdiri')['id_umkm'].count().reset_index()
    fig_line = px.line(
        umkm_per_tahun, 
        x='tahun_berdiri', 
        y='id_umkm',
        markers=True,
        labels={'tahun_berdiri': 'Tahun Berdiri', 'id_umkm': 'Jumlah UMKM'},
        template="plotly_white"
    )
    st.plotly_chart(fig_line, use_container_width=True)

with row2_col2:
    st.subheader("4. Hubungan Antara Aset dan Omset (Scatter Plot)")
    fig_scatter = px.scatter(
        df_filtered, 
        x='aset', 
        y='omset',
        color='jenis_usaha',
        hover_data=['nama_usaha'],
        labels={'aset': 'Aset (Rp)', 'omset': 'Omset (Rp)'},
        template="plotly_white"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")

# 7. Section Analisis & Wawasan (Storytelling)
st.subheader("💡 Analisis & Key Insights")
st.markdown("""
1. **Sektor Usaha Dominan:** Sektor Perdagangan dan Kesehatan mencatatkan akumulasi omset tertinggi.
2. **Penggunaan Platform Online:** Distribusi pendaftaran UMKM pada berbagai marketplace e-commerce tergolong merata.
3. **Korelasi Aset dan Omset:** Terlihat adanya hubungan positif di mana usaha dengan aset lebih tinggi cenderung memiliki omset yang lebih besar.
""")