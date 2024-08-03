import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

from css_code.css_home import *

st.set_page_config(
    page_title="10K in Paris - Home",
    page_icon="🏃‍♂️",
    initial_sidebar_state="expanded",
)

st.markdown(css_sidebar, unsafe_allow_html=True)



st.title("Run Path Generator 10K in Paris!")
st.write(css_orange_sep, unsafe_allow_html=True)

st.image("Images\home\couple runners.jpg")

st.write("""
            **Le principe est simple...**  
            Générer un itinéraire de **10km** où qu'on soit dans **Paris** !
        
            **Mon objectif à travers ce projet...**  
            Vous donner un aperçu de mes **compétences professionnelles** à travers une de mes passions **le sport**.  
         
            **A vous de jouer...**  
        """)

add_vertical_space(2)

_, demo, methode, _ = st.columns([1, 8, 8, 1])

with demo:
    with stylable_container(
            key="Bouton_DEMO",
            css_styles = css_styles_demo 
        ):
        if st.button("⬅ démo"):
            switch_page("démo")
with methode:
    with stylable_container(
            key="Bouton_Methode",
            css_styles = css_styles_methode
        ):
        if st.button("méthode ➡"):
            switch_page("Méthode")
