import folium
import streamlit as st
from geopy.geocoders import Nominatim
from folium.plugins import Realtime

from streamlit_folium import st_folium, folium_static

import osmnx as ox
import pandas as pd
import numpy as np
import ast
import zipfile
import os

import gpxpy
import gpxpy.gpx

import geopandas as gpd
from shapely.geometry import Point


@st.cache_data 
def load_graph(zip_filename, filepath):
    # Ouvrir le fichier zip et extraire le fichier GraphML temporairement
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extract(filepath, path='.')

    # Charger le graphe avec osmnx
    G = ox.load_graphml(filepath)

    # Supprimer le fichier temporaire
    os.remove(filepath)
    return G
    # return ox.load_graphml(filepath)

@st.cache_data 
def load_dataframe(zip_filename, filepath):
    # Ouvrir le fichier zip et extraire le fichier GraphML temporairement
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extract(filepath, path='.')

    # Charger le data frame
    df = pd.read_csv(filepath)

    # Supprimer le fichier temporaire
    os.remove(filepath)
    return df

# Fonction pour vérifier si un point est dans Paris
def est_dans_paris(paris_boundary, lat, lon):
    point = Point(lon, lat)
    return paris_boundary.contains(point).any()

def controle_in_paris(lat,lon):
    # Charger les limites administratives de Paris depuis un fichier GeoJSON
    paris_boundary = gpd.read_file('departement-75-paris.geojson')

    # Vérifier si les coordonnées sont dans Paris
    if est_dans_paris(paris_boundary, lat, lon):
        return True
    else:
        return False

# on initialise le centre de la map
CENTER_START = [48.854602840174394, 2.3476877892670753]
ZOOM_START = 12

# Fonction pour afficher la carte d'initialisation
def show_map_ini():
    # Créer une carte Folium
    m = folium.Map(location=CENTER_START, zoom_start=ZOOM_START)
    folium_static(m, width=725)

def home_nearest_nodes(G, X, Y, return_dist=False):
    """
    Find the nearest node to a point or to each of several points.

    If `X` and `Y` are single coordinate values, this will return the nearest
    node to that point. If `X` and `Y` are lists of coordinate values, this
    will return the nearest node to each point.

    If the graph is projected, this uses a k-d tree for euclidean nearest
    neighbor search, which requires that scipy is installed as an optional
    dependency. If it is unprojected, this uses a ball tree for haversine
    nearest neighbor search, which requires that scikit-learn is installed as
    an optional dependency.

    Parameters
    ----------
    G : networkx.MultiDiGraph
        graph in which to find nearest nodes
    X : float or list
        points' x (longitude) coordinates, in same CRS/units as graph and
        containing no nulls
    Y : float or list
        points' y (latitude) coordinates, in same CRS/units as graph and
        containing no nulls
    return_dist : bool
        optionally also return distance between points and nearest nodes

    Returns
    -------
    nn or (nn, dist) : int/list or tuple
        nearest node IDs or optionally a tuple where `dist` contains distances
        between the points and their nearest nodes
    """
    is_scalar = False
    if not (hasattr(X, "__iter__") and hasattr(Y, "__iter__")):
        # make coordinates arrays if user passed non-iterable values
        is_scalar = True
        X = np.array([X])
        Y = np.array([Y])

    if np.isnan(X).any() or np.isnan(Y).any():  # pragma: no cover
        msg = "`X` and `Y` cannot contain nulls"
        raise ValueError(msg)
    nodes = convert.graph_to_gdfs(G, edges=False, node_geometry=False)[["x", "y"]]

    if projection.is_projected(G.graph["crs"]):
        # if projected, use k-d tree for euclidean nearest-neighbor search
        if cKDTree is None:  # pragma: no cover
            msg = "scipy must be installed to search a projected graph"
            raise ImportError(msg)
        dist, pos = cKDTree(nodes).query(np.array([X, Y]).T, k=1)
        nn = nodes.index[pos]

    else:
        # if unprojected, use ball tree for haversine nearest-neighbor search
        if BallTree is None:  # pragma: no cover
            msg = "scikit-learn must be installed to search an unprojected graph"
            raise ImportError(msg)
        # haversine requires lat, lon coords in radians
        nodes_rad = np.deg2rad(nodes[["y", "x"]])
        points_rad = np.deg2rad(np.array([Y, X]).T)
        dist, pos = BallTree(nodes_rad, metric="haversine").query(points_rad, k=1)
        dist = dist[:, 0] * EARTH_RADIUS_M  # convert radians -> meters
        nn = nodes.index[pos[:, 0]]

    # convert results to correct types for return
    nn = nn.tolist()
    dist = dist.tolist()
    if is_scalar:
        nn = nn[0]
        dist = dist[0]

    if return_dist:
        return nn, dist

    # otherwise
    return nn

def generation(graph, df, lat, lon, distance):

    # orig = ox.distance.nearest_nodes(graph, X=lon, Y=lat)  
    orig = home_nearest_nodes(graph, X=lon, Y=lat) 

    route = df.loc[orig, 'route']
    route = ast.literal_eval(route)
    dist = df.loc[orig, 'dist_route']

    return dist, route

def trace_gpx(route):
    # Créer un nouvel objet GPX
    gpx = gpxpy.gpx.GPX()

    # Ajouter un nouveau segment
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    # Ajouter les points de l'itinéraire aux gpx
    for y, x in route:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(y, x))
    
    if gpx:
        # Afficher le bouton de téléchargement
        download_gpx_file(gpx, "mon_itineraire.gpx") 

# Télécharger le fichier GPX
def download_gpx_file(gpx_data, file_name):
    gpx_str = gpx_data.to_xml()
    gpx_bytes = gpx_str.encode()

    
    st.write("")
    st.write("")
    st.download_button(label="Télécharger GPX", data=gpx_bytes, file_name=file_name, mime="application/gpx+xml")


def ctrl_click_map(st_data):
    if st_data['last_clicked']:
        # Stockage des infos
        st.session_state['last_clicked'] = [st_data['last_clicked']["lat"], 
                                            st_data['last_clicked']["lng"]
                                            ]
        st.session_state['location'] = [st_data['center']["lat"], 
                                        st_data['center']["lng"]
                                        ]
        st.session_state['zoom'] = st_data['zoom']

###############################################################################################################

###############################################################################################################

# Initialiser st.session_state["Bouton_Menu"] s'il n'existe pas
if "Bouton_Menu" not in st.session_state:
    st.session_state['Bouton_Menu'] = False

# Initialiser st.session_state["Liste_Menu"] s'il n'existe pas
if "Liste_Menu" not in st.session_state:
    st.session_state['Liste_Menu'] = {'Acceuil':0,
                                      'Démo':1}

# Initialiser st.session_state["Key_Menu"] s'il n'existe pas
if "Key_Menu" not in st.session_state:
    st.session_state['Key_Menu'] = 'Acceuil'

# Initialiser st.session_state["dist"] s'il n'existe pas
if "dist" not in st.session_state:
    st.session_state['dist'] = 10000

# Initialiser st.session_state["Bouton_Generation"] s'il n'existe pas
if "Bouton_Generation" not in st.session_state:
    st.session_state['Bouton_Generation'] = False

# Initialiser st.session_state["route"] s'il n'existe pas
if "route" not in st.session_state:
    st.session_state['route'] = False

# Initialiser st.session_state["dist_route"] s'il n'existe pas
if "dist_route" not in st.session_state:
    st.session_state['dist_route'] = False

# Initialiser st.session_state["location"] s'il n'existe pas
if "location" not in st.session_state:
    st.session_state['location'] = CENTER_START

# Initialiser st.session_state["zoom"] s'il n'existe pas
if "zoom" not in st.session_state:
    st.session_state['zoom'] = ZOOM_START

# Initialiser st.session_state["last_clicked"] s'il n'existe pas
if "last_clicked" not in st.session_state:
    st.session_state['last_clicked'] = None


###############################################################################################################

###############################################################################################################
# Création de la bar sur le côté gauche
with st.sidebar:
    # Création du Menu
    col1Menu, col2Menu, _ = st.columns([1, 3, 1])   
    with col1Menu:
        # Créer un bouton Menu
        Bouton_Menu = st.button('☰')

        if Bouton_Menu:
            st.session_state['Bouton_Menu'] = not st.session_state['Bouton_Menu']
            Bouton_Menu = False
    
    with col2Menu:
        col2menucont = st.empty()
        if st.session_state['Bouton_Menu']:
            with col2menucont:
            # Liste des options pour la selectbox
                options = ['Acceuil', 'Démo']

            # Affichage de la selectbox (markdown pour replacer la liste)
                st.markdown('')
                Menu_Liste = st.selectbox('', options, index=st.session_state['Liste_Menu'][st.session_state['Key_Menu']])
                if st.session_state['Key_Menu'] != Menu_Liste:
                    # réinitialisation des données
                    st.session_state['dist'] = 10000
                    st.session_state['Bouton_Generation'] = False
                    st.session_state['location'] = CENTER_START
                    st.session_state['zoom'] = ZOOM_START
                    st.session_state['last_clicked'] = [None, None]
                    st.session_state['route'] = False
                    st.session_state['dist_route'] = False

                    # Stockage du choix du menu
                    st.session_state['Key_Menu'] = Menu_Liste

                    # Une fois qu'on a choisi une option on supprime la selectbox
                    if st.session_state['Bouton_Menu']:
                        col2menucont.empty()
                    st.session_state['Bouton_Menu'] = False

###############################################################################################################

###############################################################################################################
if st.session_state['Key_Menu'] == "Acceuil":
    # Titre
    st.title("Running Path Generator")

    show_map_ini()
    
###############################################################################################################

###############################################################################################################

elif st.session_state['Key_Menu'] == 'Démo':
    # Chargement du graph
    zip_filename = "Graphe_prepro_paris.zip"
    filepath_graph = "Graphe_prepro_paris.graphml"
    graph = load_graph(zip_filename, filepath_graph)

    # Chargement du dataframe
    zip_filename = "X_end.zip"
    filepath_df = "X_end.csv"
    df = load_dataframe(zip_filename, filepath_df)
    
    # with col2Menu:
    # with place_holder_but_reini.container():
    reinitialisation = st.button("Réinitialisation")

    if reinitialisation:
        # réinitialisation des données
        st.session_state['dist'] = 10000
        st.session_state['location'] = CENTER_START
        st.session_state['zoom'] = ZOOM_START
        st.session_state['last_clicked'] = [None, None]
        st.session_state['route'] = False
        st.session_state['dist_route'] = False


    # Création de l'emplacement du bouton de réinitialisation
    place_holder_but_reini = st.empty()

    # Création de l'emplacement du message d'erreur
    place_holder_err = st.empty()

    # Création de l'emplacement de la carte
    place_holder_map = st.empty()

    # Initialisation (pas de last_clicked save)
    if st.session_state['last_clicked'][0] == None:
        st.markdown("Cliquer sur la carte pour placer le marker de départ")
        # Création de la carte    
        m = folium.Map(location=st.session_state['location'], 
                    zoom_start=st.session_state['zoom'])

        # affichage de la carte
        with place_holder_map.container():
            st_data = st_folium(m, height=400, width=725)

        ctrl_click_map(st_data)

    # Coordonnées déjà récupérées    
    else:
        # Création de la carte    
        m = folium.Map(location=st.session_state['location'],
                        zoom_start=st.session_state['zoom'])
        custom_popup = str(st.session_state['last_clicked'][0]) + ", " + str(st.session_state['last_clicked'][1])
        
        # Contrôle coordonnées si bien dans paris
        in_paris = controle_in_paris(st.session_state['last_clicked'][0],st.session_state['last_clicked'][1])

        if not in_paris:
            # st.markdown("Cliquer sur la carte pour déplacer le marker de départ dans Paris.")
            # Affichage de l'erreur
            with place_holder_err.container():
                st.error('''
                         Le point de départ n'est pas dans Paris.  
                         Cliquer sur la carte pour déplacer le marker dans Paris.
                         ''')
            # affichage de la carte
            folium.Marker([st.session_state['last_clicked'][0],st.session_state['last_clicked'][1]], popup=folium.Popup(html=custom_popup), tooltip="Départ", icon=folium.Icon(color='red')).add_to(m)
            with place_holder_map.container():
                st_data = st_folium(m, height=400, width=725)

            ctrl_click_map(st_data)

        else: 
            folium.Marker([st.session_state['last_clicked'][0],st.session_state['last_clicked'][1]], popup=folium.Popup(html=custom_popup), tooltip="Départ").add_to(m)          
            # geolocator = Nominatim(user_agent="rpg")
            # location = geolocator.reverse((st.session_state['last_clicked'][0], st.session_state['last_clicked'][1]), exactly_one=True)
            
            # Afficher du texte avec différentes styles
            # st.markdown("<h1 style='color: blue;'>Titre en bleu</h1>", unsafe_allow_html=True)
            # st.markdown("<p style='font-size: 20px; font-family: Arial;'>Texte de taille 20px en Arial</p>", unsafe_allow_html=True)
            # st.markdown("<p style='font-weight: bold;'>Texte en gras</p>", unsafe_allow_html=True)
            # st.markdown("<p style='text-decoration: underline;'>Texte souligné</p>", unsafe_allow_html=True)

            # Afficher l'adresse obtenue
            # if location:
            #     st.markdown(f"<p style='color: blue; font-size: 20px; font-weight: bold; text-decoration: underline;'>Adresse du point de départ :</p> {location}", unsafe_allow_html=True)
            #     st.write("")
            #     st.write("")
              
            st.markdown(f"<p style='color: blue; font-size: 20px; font-weight: bold; text-decoration: underline;'>Coordonnées du point de départ [lat, lon]:</p> {st.session_state['last_clicked']}", unsafe_allow_html=True)
            st.write("")
            st.write("")

            st.session_state['dist_route'], st.session_state['route'] = generation(graph, df, st.session_state['last_clicked'][0], st.session_state['last_clicked'][1], st.session_state['dist'])

            col1dist, col2dist, _ = st.columns([4, 4, 1])   
            with col1dist:
                st.markdown(f"<p style='color: blue; font-size: 20px; font-weight: bold; text-decoration: underline;'>Distance visée:</p> {st.session_state['dist']}", unsafe_allow_html=True)
            with col2dist:
                st.markdown(f"<p style='color: blue; font-size: 20px; font-weight: bold; text-decoration: underline;'>Distance du parcours généré:</p> {st.session_state['dist_route']}m.", unsafe_allow_html=True)

            # Tracez le trajet GPX sur la carte
            folium.plugins.AntPath(locations=st.session_state['route'], weight=6, color='blue').add_to(m)
            # affichage de la carte
            with place_holder_map.container():
                # st_data = st_folium(m, height=400, width=725)
                folium_static(m, height=400, width=725)

            trace_gpx(st.session_state['route'])
            



