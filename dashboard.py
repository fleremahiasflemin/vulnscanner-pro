import streamlit as st

st.title("🔍 VulnScanner PRO Dashboard")
st.write("Escanea tus sistemas y visualiza vulnerabilidades en tiempo real.")

if st.button("Iniciar escaneo"):
    st.info("Escaneo simulado completado con éxito 🚀")
    st.dataframe([{"CVE": "CVE-2021-1234", "CVSS": 9.8, "Descripción": "Vuln de prueba"}])
