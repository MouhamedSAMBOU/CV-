import streamlit as st

st.title ("Mouhamed SAMBOU")

st.subheader("🎓 FORMATIONS")

st.markdown("""
* BTS en Geomatique 2026
* Licence 2 en Physique Chimie 2024""")


st.subheader("🎯 COMPETENCES")

st.markdown("""
* Maitrise de logiciels SIG (QGIS, ArcGIS, etc)
* Teledetection
* Topographie
* Maitrise Word, Excel, PowerPoint, etc
* Pilotage de drone
""")

st.subheader("💻 *Logiciels maîtrisés*")
logiciels = [
    "QGIS / ArcGIS",
    "AutoCAD", 
    "Python",
    "Pix4D",
    "Erdas"
]
for logiciel in logiciels:
    st.markdown(f"• *{logiciel}*")

st.sidebar.title("PROFIL")
st.sidebar.markdown("Technicien Superieur en Geomatique")
st.sidebar.header("📞 *Contacts*")
st.sidebar.markdown("""
*Adresse :*  
Keur Massar, Boune

*Email :*  
Sambouameth2002@gmail.com 
""")

st.sidebar.markdown("---")
st.sidebar.markdown("Merci de me contacter")
   
