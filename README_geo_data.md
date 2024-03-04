#Donnée géographique

Concernant la récupération des données géographiques il y plusieurs outils possible pour python.

Le plus prométeur semble être OpenStreetMap (https://www.openstreetmap.org).

Il existe de nombreux outils pour récuperer les données et les travailler.

Liste des outils :
- openstreetmap
- osmnx
- folium
- Overpass API
- Overpass-turbo

- OSMnx est une bibliothèque qui permet d'accéder, extraire et analyser des données de réseaux de rues à partir d'OpenStreetMap. Elle est souvent utilisée pour créer des graphiques de réseaux routiers basés sur des données réelles d'OpenStreetMap.
  Voici quelques fonctionnalités clés d'OSMnx :
  - Téléchargement de données : OSMnx peut télécharger des données de réseaux routiers à partir d'OpenStreetMap en spécifiant des emplacements géographiques, des types de réseau (par exemple, piéton, voiture) et d'autres paramètres.
  - Création de graphiques de réseaux : La bibliothèque permet de créer des graphiques de réseaux à partir des données téléchargées. Ces graphiques peuvent être utilisés pour visualiser la structure des rues et des itinéraires possibles.
  - Analyse du réseau : OSMnx offre des fonctionnalités pour analyser les caractéristiques du réseau, telles que les centrality measures (mesures de centralité), la longueur des itinéraires, etc.
  - Visualisation : Vous pouvez utiliser OSMnx pour visualiser graphiquement les données de réseau sur des cartes ou des graphiques interactifs.


- Folium est une bibliothèque Python qui permet de créer des cartes interactives basées sur Leaflet, une bibliothèque JavaScript de cartographie. Folium facilite la création de cartes interactives avec des marqueurs, des formes géométriques, des tuiles de carte, et bien plus encore, le tout intégré dans un environnement Python.
  Voici quelques caractéristiques et fonctionnalités de Folium :
  - Intégration avec Leaflet : Folium utilise Leaflet.js, une bibliothèque JavaScript populaire pour la cartographie interactive. Cela signifie que les cartes générées par Folium sont riches en fonctionnalités et interactives.
  - Facilité d'utilisation : Folium est conçu pour être simple et facile à utiliser. Les utilisateurs peuvent créer des cartes avec seulement quelques lignes de code.
  - Support de marqueurs et de popups : Vous pouvez placer des marqueurs sur la carte pour indiquer des points d'intérêt, et ajouter des popups pour fournir des informations supplémentaires.
  - Styles personnalisables : Folium offre un contrôle complet sur l'apparence des cartes, des marqueurs et d'autres éléments. Vous pouvez personnaliser les couleurs, les icônes, les polices, etc.
  - Prise en charge de diverses tuiles de carte : Folium permet d'utiliser différentes tuiles de carte, telles que OpenStreetMap, Stamen Terrain, Stamen Toner, Mapbox, etc.
  - Intégration avec des données pandas : Folium s'intègre bien avec les structures de données pandas, ce qui facilite la visualisation de données géospatiales.


Overpass API est une API qui permet d'interroger la base de données OSM depuis des serveurs distants. 
Elle propose un langage de requête très complet qui permet de sélectionner les données à télécharger selon un grand nombre de critères (tags des objets, types d'objets, localisation géographique, etc.). 
Son utilisation nécessite la prise en main du langage selon les instructions fournies par la documentation.


Overpass-turbo est un site qui propose une interface graphique multilingue par-dessus l'Overpass API afin d'en faciliter la prise en main par les utilisateurs. 
Une carte intégrée permet de sélectionner la zone d'intérêt. Un assistant (wizard dans la version anglaise) permet de générer automatiquement le code du langage Overpass API pour les requêtes simples. 
Une prévisualisation des données récupérées est disponible sur la carte et il est possible de les exporter vers des formats de données géographiques (GPX, KML, GeoJSON).




###Quelle outils pour chaques besoin ?

Ici on va associé à chaque besoin un outils qu'on va devoir maitriser.

Selection et récupération des données => OpenStreetMap / Overpass API / Overpass-turbo
Transformation et assemblage des données => OSMnx / networkx / xml
Visualisation du graph et chemin => folium / ...
Utilisation d'algorythme de pathfinding => networkx / ...
Réalisation de vidéo => opencv (cv2) et glob 


Source et biblio :
Vidéo utilisation d'algo de pathfinding pour plus court chemin (itération, longueur, vitesse, temps de trajet)
- https://www.youtube.com/watch?v=oMgfGkFSgI0
- https://github.com/santifiorino/maps-pathfinding/blob/main/pathfinding.ipynb









