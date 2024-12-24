import streamlit as st 

dashboard = st.Page("dashboard.py", title="Dashboard")
nabung= st.Page("nabung.py", title="Menabung")

pg = st.navigation(
    {
        " Menu Utama" : [dashboard],
        "Transaksi" : [nabung],
        
    }
)

if "Total_semua" not in st.session_state:
    st.session_state["Total_semua"] = []

pg.run()

