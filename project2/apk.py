import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    body {
        background-color: #b3d9ff; /* Warna latar belakang biru muda */
        color: rgb(20, 40, 60); /* Warna teks tetap sesuai */
        font-family: 'Poppins', Helvetica, Arial, sans-serif; /* Font baru: Poppins */
        font-size: 1.2em;
    }
    a {
        color: rgb(255, 111, 111); /* Warna tautan merah muda terang */
    }
    .sidebar .sidebar-content {
        background-color: #70a1ff;
        font-family: 'Poppins', Helvetica, Arial, sans-serif; /* Font sidebar */
    }
    h1, h2, h3 {
        color: maroon; /* Set all titles to maroon */
        text-align: center;
        font-family: 'Poppins', Helvetica, Arial, sans-serif; /* Font baru untuk judul */
        font-weight: 600; /* Menebalkan font judul */
    }
    .st-button button {
        background-color: #1e90ff;
        color: white;
        border-radius: 5px;
        font-family: 'Poppins', Helvetica, Arial, sans-serif; /* Font untuk tombol */
    }
    .st-button button:hover {
        background-color: #4682b4;
    }
    .dataframe {
        margin: auto;
        border: 1px solid #ccc;
        border-collapse: collapse;
        width: 80%;
        background-color: #f0f8ff;
        font-family: 'Poppins', Helvetica, Arial, sans-serif; /* Font tabel */
    }
    .dataframe th {
        background-color: #4682b4;
        color: white;
        text-align: center;
        padding: 8px;
    }
    .dataframe td {
        text-align: center;
        padding: 8px;
    }
    .dataframe tr:nth-child(even) {
        background-color: #eaf4fc;
    }
    .st-image img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# data untuk menu minuman
data_minuman = {
    "Nama Minuman": ["Es Teh", "Es Jeruk", "Cappuccino", "Latte", "Matcha", "Thai Tea", "Lemon Tea", "Lychee Tea", "Milkshake", "Es Krim"],
    "Harga (Rp)": [7000, 8000, 15000, 18000, 20000, 19000, 18000, 18000, 25000, 10000]
}
menu_minuman_df = pd.DataFrame(data_minuman)

# data unruk menu maknan
data_makanan = {
    "Nama Makanan": ["Nasi Goreng", "Spagheti Bolognaise", "Ayam Bakar", "Mie Ayam Teriyaki", "Ayam Buldak", "Bakso", "Pecel Lele", "Soto Ayam", "Pangsit Chili oil", "Chicken Steak"],
    "Harga (Rp)": [20000, 14000, 25000, 28000, 27000, 15000, 18000, 22000, 15000, 28000]
}
menu_makanan_df = pd.DataFrame(data_makanan)

# fungsi untuk menu utama
def menu_utama():
    st.title("Rumah Makan Keluarga")
    st.image("logo.jpeg", width=700, caption="Selamat Datang di Rumah Makan Keluarga")
    st.write("""
    ### Tentang Kami
    Rumah Makan Keluarga ini menyediakan berbagai menu makanan dan minuman yang lezat dan terjangkau. 
    Dengan suasana yang nyaman, kami ada untuk melayani Anda dan keluarga dengan sepenuh hati. 
    Semoga hari-hari Anda dan keluarga selalu bahagia. 
    Kami sangat senang Anda memilih Rumah Makan Keluarga sebagai tempat makan Anda hari ini. 
    Selamat datang dan selamat menikmati hidangan kami!
    """)

# fungsi untuk menu minuman
def menu_minuman():
    st.title("Menu Minuman")
    st.write("### Pilih Menu Minuman")
    st.dataframe(menu_minuman_df)  # nampilin menu minuman dalam bentuk tabel
    
    # pilihan buat menu minuman dan jumlah
    pilihan_minuman = st.selectbox("Pilih Minuman", menu_minuman_df["Nama Minuman"])
    jumlah_minuman = st.number_input("Jumlah Pesanan", min_value=1, step=1)
    harga_minuman = menu_minuman_df[menu_minuman_df["Nama Minuman"] == pilihan_minuman]["Harga (Rp)"].values[0]
    total_harga = harga_minuman * jumlah_minuman
    st.write(f"Total harga yang akan anda bayar untuk {jumlah_minuman} {pilihan_minuman} adalah Rp {total_harga}")

# fungsi untuk membuat PDF dan mengembalikan sebagai bytes
def buat_pdf(data):
    pdf = FPDF() #membuat objek pdf baru
    pdf.add_page() #nambahin halaman baaru
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Struk Belanja", ln=True, align="C")
    pdf.ln(10)

    for key, value in data.items():
        pdf.cell(0, 10, txt=f"{key}: {value}", ln=True)

    # untuk simpan ke buffer
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)  # kembali ke awal buffer
    return buffer

# fungsi untuk pemesanan minuman
def pemesanan_minuman():
    st.title("Pemesanan Minuman")

    nama_pembeli = st.text_input("Nama Pembeli")
    no_telepon = st.text_input("Nomor Telepon")

    pesanan_minuman = []

    if "pesanan_minuman" not in st.session_state:
        st.session_state.pesanan_minuman = []

    st.write("### Pilih Menu Minuman")
    pilihan_minuman = st.multiselect("Pilih Minuman", menu_minuman_df["Nama Minuman"].tolist())
    jumlah_minuman = st.number_input("Jumlah Pesanan", min_value=1, step=1)

    if st.button("Tambahkan ke Pesanan"):
        if not nama_pembeli or not no_telepon or not pilihan_minuman:
            st.warning("Harap lengkapi Nama Pembeli, Nomor Telepon, dan Pilihan Minuman.")
        else:
            for minuman in pilihan_minuman:
                harga_minuman = menu_minuman_df[menu_minuman_df["Nama Minuman"] == minuman]["Harga (Rp)"].values[0]
                st.session_state.pesanan_minuman.append({
                    "Nama Pembeli": nama_pembeli,
                    "Nomor Telepon": no_telepon,
                    "Minuman": minuman,
                    "Jumlah": jumlah_minuman,
                    "Harga Satuan": harga_minuman,
                    "Total": jumlah_minuman * harga_minuman
                })
            st.success("Pesanan berhasil ditambahkan!")

    st.write(" Daftar Pesanan Minuman")
    if st.session_state.pesanan_minuman:
        df_pesanan = pd.DataFrame(st.session_state.pesanan_minuman)
        st.table(df_pesanan)

        total_harga = sum(item["Total"] for item in st.session_state.pesanan_minuman)
        st.write(f"Total Harga: Rp {total_harga}")

        if st.button("Selesaikan Pemesanan"):
            data_pesanan = {
                "Nama Pembeli": nama_pembeli,
                "Nomor Telepon": no_telepon,
                "Pesanan": st.session_state.pesanan_minuman,
                "Total Harga": f"Rp {total_harga}"
            }

            st.table(pd.DataFrame(data_pesanan["Pesanan"]))
            st.success("Pemesanan selesai!")

            pdf_buffer = buat_pdf(data_pesanan)
            st.download_button(
                label="Unduh Struk",
                data=pdf_buffer,
                file_name="struk_minuman.pdf",
                mime="application/pdf"
            )

            st.session_state.pesanan_minuman = []

# fungsi buat menu makanan
def menu_makanan():
    st.title("Menu Makanan")
    st.write("### Pilih Menu Makanan")
    st.dataframe(menu_makanan_df)  # nampilin menu makanan dalam bentuk tabel
    
    # pilihan menu makanan dan jumlah
    pilihan_makanan = st.selectbox("Pilih Makanan", menu_makanan_df["Nama Makanan"])
    jumlah_makanan = st.number_input("Jumlah Pesanan", min_value=1, step=1)
    harga_makanan = menu_makanan_df[menu_makanan_df["Nama Makanan"] == pilihan_makanan]["Harga (Rp)"].values[0]
    total_harga = harga_makanan * jumlah_makanan
    st.write(f"Total harga yang akan anda bayar untuk {jumlah_makanan} {pilihan_makanan} adalah Rp {total_harga}")

# fungsi buat pemesanan makanan
def pemesanan_makanan():
    st.title("Pemesanan Makanan")

    nama_pembeli = st.text_input("Nama Pembeli")
    no_telepon = st.text_input("Nomor Telepon")

    if "pesanan_makanan" not in st.session_state:
        st.session_state.pesanan_makanan = []

    st.write("### Pilih Menu Makanan")
    pilihan_makanan = st.multiselect("Pilih Makanan", menu_makanan_df["Nama Makanan"].tolist())
    jumlah_makanan = st.number_input("Jumlah Pesanan", min_value=1, step=1)

    if st.button("Tambahkan ke Pesanan"):
        if not nama_pembeli or not no_telepon or not pilihan_makanan:
            st.warning("Harap lengkapi Nama Pembeli, Nomor Telepon, dan Pilihan Makanan.")
        else:
            for makanan in pilihan_makanan:
                harga_makanan = menu_makanan_df[menu_makanan_df["Nama Makanan"] == makanan]["Harga (Rp)"].values[0]
                st.session_state.pesanan_makanan.append({
                    "Nama Pembeli": nama_pembeli,
                    "Nomor Telepon": no_telepon,
                    "Makanan": makanan,
                    "Jumlah": jumlah_makanan,
                    "Harga Satuan": harga_makanan,
                    "Total": jumlah_makanan * harga_makanan
                })
            st.success("Pesanan berhasil ditambahkan!")

    st.write(" Daftar Pesanan Makanan")
    if st.session_state.pesanan_makanan:
        df_pesanan = pd.DataFrame(st.session_state.pesanan_makanan)
        st.table(df_pesanan)

        total_harga = sum(item["Total"] for item in st.session_state.pesanan_makanan)
        st.write(f" Total Harga: Rp {total_harga}")

        if st.button("Selesaikan Pemesanan"):
            data_pesanan = {
                "Nama Pembeli": nama_pembeli,
                "Nomor Telepon": no_telepon,
                "Pesanan": st.session_state.pesanan_makanan,
                "Total Harga": f"Rp {total_harga}"
            }

            st.table(pd.DataFrame(data_pesanan["Pesanan"]))
            st.success("Pemesanan selesai!")

            pdf_buffer = buat_pdf(data_pesanan)
            st.download_button(
                label="Unduh Struk",
                data=pdf_buffer,
                file_name="struk_makanan.pdf",
                mime="application/pdf"
            )

            st.session_state.pesanan_makanan = []

# menu navigasi untuk memilih aplikasi
menu = st.sidebar.selectbox(
    "Pilih Menu Aplikasi",
    ["Menu Utama", "Menu Minuman", "Pemesanan Minuman", "Menu Makanan", "Pemesanan Makanan"]
)

# menentukan aplikasi yang dipilih
if menu == "Menu Utama":
    menu_utama()
elif menu == "Menu Minuman":
    menu_minuman()
elif menu == "Pemesanan Minuman":
    pemesanan_minuman()
elif menu == "Menu Makanan":
    menu_makanan()
elif menu == "Pemesanan Makanan":
    pemesanan_makanan()
    
st.markdown(
    """
    <style>
    .stApp{
        background-color: #FFF0DC; 
    }
    
    [data-testid="stSidebar"]{
        background-color: #FFF0DC;
        color.white;
    }
    
    [data-testid="stSidebar"]{
        color: white limportant;
        font-size: 16px;
        
    }
    
    </style>
    """,
    unsafe_allow_html= True
    
)
