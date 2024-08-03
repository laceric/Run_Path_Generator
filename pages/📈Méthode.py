import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

from css_code.css_methode import *

st.set_page_config(
    page_title="10K in Paris - Méthode",
    page_icon="🏃‍♂️",
    initial_sidebar_state="expanded",
)

# Définition du style de la sidebar
st.markdown(css_sidebar, unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Introduction", "L'algorithme", "Le jeux de données", "Les modèles de Machine Learning", "Optimisation des résultats"])

#####################################################################################################
# Introduction
#####################################################################################################

with tab1:
    add_vertical_space(2)
    col1, col2 = st.columns([2,5])
    with col1:
        st.image("Images\methode\Methode_animation.gif")
    with col2:
        st.markdown("""
                        La méthode principale de ce projet tourne autour de la capacité à déterminer les bonnes valeurs des paramètre d'un algorithme qui génère un itinéraire.
                                
                        Pour cela J'ai du coder un algorithme, créer des jeux de données, entraîner des modèles de prédictions.
                        Et enfin optimiser ces prédictions à travers l'analyse et des méthodes d'optimisations.
                    """)

#####################################################################################################
# L'algorithme
#####################################################################################################

with tab2:
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("Images\methode\map_animation.gif")
    with col2:
        add_vertical_space(2)
        st.markdown("""
                        Le principe de base de l'algorithme pour générer un itinéraire est la création de points de passages.
                    """)
    
    col1, col2 = st.columns([5,5])
    with col1:
        st.markdown("""
                        1) On définit un point centrale qui se trouve entre le point de départ le centre de Paris et à une certaine distance (topographique) R du point de départ.
                    """)
        st.markdown(css_sous_titre_start +
                    """
                        (Dans l'ordre de gauche à droite : Point de Départ, Point Centrale, Centre de Paris)
                    """
                    + css_sous_titre_end, unsafe_allow_html=True)
    with col2:
        st.image("Images\methode\\algo_paris_1.png")

    add_vertical_space(2)
    col1, col2 = st.columns([5,5])
    with col1:
        st.image("Images\methode\\algo_paris_2.png")
    with col2:
        st.markdown("""
                        2) Ensuite on définit un certain nombre de points de passage à cette même distance R du point centrale selon différents angles. 
                    """)
        st.markdown(css_sous_titre_start +
                    """
                        (Point de Départ: Jaune, Point Centrale: Rouge, Points de Passage: Blanc)
                    """
                    + css_sous_titre_end, unsafe_allow_html=True)

    add_vertical_space(2)
    col1, col2 = st.columns([3,5])
    with col1:
        st.markdown("""
                        3) Enfin on relies les points de passage via un algorithme de pathfinding.  
                    """)
    with col2:
        st.image("Images\methode\\algo_paris_3.png")



#####################################################################################################
# Le jeux de données
#####################################################################################################

with tab3:
    st.markdown("""
                    La création du premier jeux de données s'appuye sur le découpage de Paris en zone.  
                    Une répartition uniforme des valeurs des différents paramètres de l'algorithme a été faite pour éviter d'avoir un biais au départ.
                """)
    
    st.image("Images\methode\paris_jdd_decoupe.png")

    st.markdown(css_sous_titre_start +
                """
                    On supprime les zones qui n'ont pas de noeud (point) et on génères des échantillons dans les autres de sorte à couvrir uniformément la surface de Paris.
                """
                + css_sous_titre_end, unsafe_allow_html=True)


#####################################################################################################
# Les modèles de Machine Learning
#####################################################################################################

with tab4:
    
    col1, col2 = st.columns([10,1])
    with col1:
        st.markdown("""
                    On utilise des modèles de Regression pour optimiser les paramètres de sorte à optenir une distance proche des 10km.
                    (RandomForestRegressor, DecisionTreeRegressor, GradientBoostingRegressor, GaussianProcessRegressor, KernelRidge, SVR)
                """)

        add_vertical_space(2)
        st.markdown("""
                        La comparaison de modèles avec afutage des hyper-paramètres a donné des résultats positif en particulier pour le modèle SVR.  
                        Cependant l'écart entre la distance optenue et les 10km était souvent trop important.
                    """)
    
    add_vertical_space(3)
    st.image("Images\methode\cible_avant.jpg")

    _, col2= st.columns([1,5])
    with col2:
        st.markdown(css_sous_titre_start +
                    """
                    Les lignes rouges représente les bornes cibles pour l'écart (entre 0 et +300 mètres).
                    """
                    + css_sous_titre_end, unsafe_allow_html=True)
        st.markdown(css_sous_titre_start +
                    """
                    Les autres lignes représente les quantiles des écarts (légende dans le tableau à droite).
                    """
                    + css_sous_titre_end, unsafe_allow_html=True)


#####################################################################################################
# Optimisation des résultats
#####################################################################################################

with tab5:
    st.markdown("""
                    Afin d'améliorer les résultats je suis parti sur des méthodes d'optimisation.  
                    J'ai créer un nouveau jeu de données qui reprend uniquement les noeuds du réseau.
                    J'ai ensuite utiliser mon meilleur modèle de regression pour avoir des paramètres plus optimisés.
                    Puis j'ai utilisé deux méthodes.

                    1) La première méthode est l'optimisation pas à pas.  
                    J'ai ainsi optenue pour chaque noeud la valeur du paramètres la plus optimale possible.
                
                    2) La seconde méthode est l'optimisation par le meilleur voisin.
                    J'ai cherché le voisin qui donné le meilleur résultat en cumulant son parcours avec la distance du noeud initiale.
                    Cette dernière a véritablement permise de compenser une partie des défauts de l'algorithme de départ.
                """)

    add_vertical_space(3)
    col1, col2 = st.columns([1,1])
    with col1:
        _, col1b = st.columns([1,17])
        with col1b:
            st.markdown("**Résultat avant optimisation**")
            st.markdown(css_orange_sep, unsafe_allow_html=True)
            
        add_vertical_space(2)
        col1c, _ = st.columns([6,2])
        with col1c:
            st.image("Images\methode\cible_avant.jpg")
        add_vertical_space(2)
        st.image("Images\methode\image_res_avant_opti.jpg")
        st.markdown(css_sous_titre_start +
                    """
                    Avant optimisation : jeux de données de 1180 lignes.
                    """
                    + css_sous_titre_end, unsafe_allow_html=True)
        
    with col2:
        _, col2b = st.columns([1,17])
        with col2b:
            st.markdown("**Résultat après optimisation**")
            st.markdown(css_orange_sep, unsafe_allow_html=True)
            
        add_vertical_space(2)
        col2c, _ = st.columns([5,2])
        with col2c:
            st.image("Images\methode\cible_apres.jpg")
        add_vertical_space(2)
        st.image("Images\methode\image_res_apres_opti.jpg")
        st.markdown(css_sous_titre_start +
                    """
                    Après optimisation : jeux de données de 15844 lignes.
                    """
                    + css_sous_titre_end, unsafe_allow_html=True)
