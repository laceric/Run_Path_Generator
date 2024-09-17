import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space
import os

from css_code.css_home import *

st.set_page_config(
    page_title="10K in Paris - Home",
    page_icon="🏃‍♂️",
    initial_sidebar_state="expanded",
)

st.markdown(css_sidebar, unsafe_allow_html=True)



st.title("Votre itinéraire de 10 Km dans Paris !")
st.write(css_orange_sep, unsafe_allow_html=True)


# Définir le chemin relatif vers l'image
image_path = os.path.join('Images', 'home', 'couple_runners.jpg')

# Vérifier que le fichier existe avant d'essayer de le charger
if os.path.exists(image_path):
    st.image(image_path)
else:
    st.error(f"Le fichier '{image_path}' n'existe pas.")

st.write("""
            **Le principe est simple...**  
            Générer un itinéraire de **10km** où qu'on soit dans **Paris** !
        
            **Mon objectif à travers ce projet...**  
            Vous donner un aperçu de mes **compétences professionnelles** à travers une de mes passions **le sport**.  
         
            **A vous de jouer...**  
        """)

add_vertical_space(2)

_, demo, _ = st.columns([1, 2, 1])

with demo:
    with stylable_container(
            key="Bouton_DEMO",
            css_styles = css_styles_demo 
        ):
        if st.button("Démo ➡"):
            switch_page("démo")
