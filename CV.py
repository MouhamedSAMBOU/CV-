import streamlit as st

st.title ("📋 CURRICULUM VITAE")

st.markdown("*Mouhamed SAMBOU* - Géomaticien")
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
st.sidebar.image("Pro.jpeg", width=150)
st.sidebar.header("📞 *Contacts*")
st.sidebar.markdown("""
*Adresse*  
Keur Massar, Boune

*Téléphone*  
+221 777777777

*Email*  
Sambouameth2002@gmail.com 
""")



st.sidebar.markdown("---")
st.sidebar.markdown("Géomaticien - L2 en cours")
   