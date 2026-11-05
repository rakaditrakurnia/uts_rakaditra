# Dashboard Visualisasi Data Performa UMKM Indonesia

Proyek ini merupakan bagian dari **Ujian Tengah Semester (UTS) Visualisasi Data**. Aplikasi ini dibangun menggunakan **Streamlit** dan **Plotly** untuk menyajikan dashboard interaktif yang menganalisis performa operasional, finansial, serta adopsi saluran pemasaran digital dari Usaha Mikro, Kecil, dan Menengah (UMKM) di Indonesia.

---

## 👤 Identitas
* **Nama**: Rakaditra Kurnia
* **NIM**: 241051017
* **Proyek**: UTS Visualisasi Data
* **Aplikasi Live**: [utsrakaditra.streamlit.app](https://utsrakaditra.streamlit.app)

---

## 📊 Deskripsi Dataset
Dataset `datase_usaha.csv` berisi informasi komprehensif mengenai **13.564 UMKM** di Indonesia dengan **14 atribut utama**, antara lain:

* **Identitas & Profil**: `id_umkm`, `nama_usaha`, `jenis_usaha`, `tahun_berdiri`, `status_legalitas`
* **Tenaga Kerja**: `tenaga_kerja_perempuan`, `tenaga_kerja_laki_laki`
* **Finansial**: `aset`, `omset`, `laba`, `biaya_karyawan`
* **Pemasaran & Operasional**: `marketplace`, `kapasitas_produksi`, `jumlah_pelanggan`

---

## 🚀 Fitur Dashboard Interaktif
1. **Filter Data (Sidebar)**:
   * Filter berdasarkan sektor `jenis_usaha`.
   * Filter berdasarkan saluran `marketplace` yang digunakan.
2. **Key Performance Indicators (KPIs)**:
   * Menampilkan total omset, total laba bersih, dan total penyerapan tenaga kerja.
3. **Visualisasi Data Interaktif**:
   * **Bar Chart**: Perbandingan Total Omset per Jenis Usaha.
   * **Pie Chart**: Distribusi Penggunaan Marketplace oleh UMKM.
   * **Scatter Plot**: Hubungan antara Aset dan Laba Bersih.
   * **Histogram**: Distribusi Tahun Berdiri UMKM.

---

## 🛠️ Teknologi & Pustaka
* **Python 3.10+**
* **Streamlit** (Framework Aplikasi Web)
* **Pandas** (Pengolahan & Analisis Data)
* **Plotly Express** (Visualisasi Data Interaktif)

---

## 💻 Cara Menjalankan Aplikasi Secara Lokal

1. **Clone Repositori**:
   ```bash
   git clone https://github.com/rakaditrakurnia/uts_rakaditra.git
   cd uts_rakaditra
   ```

2. **Install Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi Streamlit**:
   ```bash
   streamlit run app.py
   ```