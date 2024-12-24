import streamlit as st 

st.title("Halaman Dashboard")
st.image("web.jpg", caption="Gambar Web")

# fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(t["Jumlah"]
                       for t in st.session_state["Total_Semua"]
                       if t ["Tipe"] == "Menabung")
    
    return total_nabung

total_semua = st.session_state["Total_semua"]
total_nabung = total()

st.metric("Total Menabung", f"rp {total_nabung}")

