import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import folium
# from streamlit_folium import folium_static                                # Mis en commentaire => remplacer par Image_map.png


# Fonction pour afficher la carte d'initialisation                          # Mis en commentaire => remplacer par Image_map.png
# def show_map_ini():
#     # on initialise le centre de la map
#     CENTER_START = [48.854602840174394, 2.3476877892670753]
#     ZOOM_START = 12

#     # Créer une carte Folium
#     m = folium.Map(location=CENTER_START, zoom_start=ZOOM_START)
#     folium_static(m, width=725)

# Titre
st.title("Running Path Generator")

# show_map_ini()                                                            # Mis en commentaire => remplacer par Image_map.png

# Afficher l'image sauvegardée dans Streamlit
st.image("Image_map.png")

# Si click sur bouton demo alors on change de page
if st.button("demo"):
    switch_page("demo")
    st.rerun()
