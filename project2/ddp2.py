import streamlit as st
import pandas as pd

# style css nya
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
    </style>
    """,
    unsafe_allow_html=True
)


# datanya untuk menu minuman
data_minuman = {
    "Nama Minuman": ["Es Teh", "Es Jeruk", "Cappuccino", "Latte", "Matcha", "Thai Tea", "Lemon Tea", "Lychee Tea", "Milkshake", "Es Krim"],
    "Harga (Rp)": [7000, 8000, 15000, 18000, 20000, 19000, 18000, 18000, 25000, 10000]
}
menu_minuman_df = pd.DataFrame(data_minuman)

# datanya untuk menu makanan
data_makanan = {
    "Nama Makanan": ["Nasi Goreng", "Spagheti Bolognaise", "Ayam Bakar", "Mie Ayam Teriyaki", "Ayam Buldak", "Bakso", "Pecel Lele", "Soto Ayam", "Pangsit Chili oil", "Chicken Steak"],
    "Harga (Rp)": [20000, 14000, 25000, 28000, 27000, 15000, 18000, 22000, 15000, 28000]
}
menu_makanan_df = pd.DataFrame(data_makanan)

#  untuk fungsi menu utama - nampilin dan milih menu minuman (apk ke 1)
def menu_minuman():
    st.title("Rumah Makan Keluarga")
    st.image("logo.jpeg")
    st.title("Menu Minuman")
    st.write("### Pilih Menu Minuman")
    st.dataframe(menu_minuman_df)
    
    st.write("### Menu Minuman")
    st.dataframe(menu_minuman_df)  # buat nampilin menu minuman pake tabel

    # untuk milih menu minuman sama jumlahnya
    pilihan_minuman = st.selectbox("Pilih Minuman", menu_minuman_df["Nama Minuman"])
    jumlah_minuman = st.number_input("Jumlah Pesanan", min_value=1, step=1)

    harga_minuman = menu_minuman_df[menu_minuman_df["Nama Minuman"] == pilihan_minuman]["Harga (Rp)"].values[0]
    total_harga = harga_minuman * jumlah_minuman
    st.write(f"### Total harga untuk {jumlah_minuman} {pilihan_minuman} adalah Rp {total_harga}")



# untuk fungsi menu kedua - aplikasi pemesanan minuman (apk ke 2)
def pemesanan_minuman():
    st.title("Pemesanan Minuman")

    # input untuk pemesanannya
    nama_pembeli = st.text_input("Nama Pembeli")
    no_telepon = st.text_input("Nomor Telepon")
    pilihan_minuman = st.selectbox("Pilih Minuman", menu_minuman_df["Nama Minuman"])
    jumlah_minuman = st.number_input("Jumlah Pesanan", min_value=1, step=1)
    tipe_pesanan = st.selectbox("Jenis Pesanan", ["Dine In", "Take Away"])

    if st.button("Pesan Minuman"):
        harga_minuman = menu_minuman_df[menu_minuman_df["Nama Minuman"] == pilihan_minuman]["Harga (Rp)"].values[0]
        total_harga = harga_minuman * jumlah_minuman
        st.write(f"Nama Pembeli: {nama_pembeli}")
        st.write(f"Nomor Telepon: {no_telepon}")
        st.write(f"Jumlah Pesanan: {jumlah_minuman} {pilihan_minuman}")
        st.write(f"Total yang harus dibayar: Rp {total_harga}")
        st.write(f"Pesanan: {tipe_pesanan}")
        st.success("Pesanan berhasil dilakukan!")

# fungsi menu ketiga  nampilin menu makanan dan memilih makanan (apk ke 3)
def menu_makanan():
    st.title("Menu Makanan")
    st.write("### Pilih Menu Makanan")
    st.dataframe(menu_makanan_df)  # nampilin menu makanan dalam bentuk tabel

    # pilihan menu makanan dan jumlah
    pilihan_makanan = st.selectbox("Pilih Makanan", menu_makanan_df["Nama Makanan"])
    jumlah_makanan = st.number_input("Jumlah Pesanan", min_value=1, step=1)

    harga_makanan = menu_makanan_df[menu_makanan_df["Nama Makanan"] == pilihan_makanan]["Harga (Rp)"].values[0]
    total_harga = harga_makanan * jumlah_makanan
    st.write(f"### Total harga untuk {jumlah_makanan} {pilihan_makanan} adalah Rp {total_harga}")

# fungsi menu keempat - aplikasi pemesanan makanan (apk ke 4)
def pemesanan_makanan():
    st.title("Pemesanan Makanan")

    # penginput untuk pemesanan
    nama_pembeli = st.text_input("Nama Pembeli")
    no_telepon = st.text_input("Nomor Telepon")
    pilihan_makanan = st.selectbox("Pilih Makanan", menu_makanan_df["Nama Makanan"])
    jumlah_makanan = st.number_input("Jumlah Pesanan", min_value=1, step=1)
    tipe_pesanan = st.selectbox("Jenis Pesanan", ["Dine In", "Take Away"])

    if st.button("Pesan Makanan"):
        harga_makanan = menu_makanan_df[menu_makanan_df["Nama Makanan"] == pilihan_makanan]["Harga (Rp)"].values[0]
        total_harga = harga_makanan * jumlah_makanan
        st.write(f"Nama Pembeli: {nama_pembeli}")
        st.write(f"Nomor Telepon: {no_telepon}")
        st.write(f"Jumlah Pesanan: {jumlah_makanan} {pilihan_makanan}")
        st.write(f"Total yang harus dibayar: Rp {total_harga}")
        st.write(f"Pesanan: {tipe_pesanan}")
        st.success("Pesanan berhasil dilakukan!")

# menu navigasi buat memilih aplikasi
menu = st.sidebar.selectbox(
    "Pilih Menu Aplikasi",
    ["Menu Minuman", "Pemesanan Minuman", "Menu Makanan", "Pemesanan Makanan"]
)

# buat menentukan aplikasi yang dipilih
if menu == "Menu Minuman":
    menu_minuman()
elif menu == "Pemesanan Minuman":
    pemesanan_minuman()
elif menu == "Menu Makanan":
    menu_makanan()
elif menu == "Pemesanan Makanan":
    pemesanan_makanan()

