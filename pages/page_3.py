import streamlit as st

# Initialiser st.session_state["init"] s'il n'existe pas
if "click" not in st.session_state:
    st.session_state['click'] = False

# Fonction pour injecter du CSS et HTML pour le bouton personnalisé
def custom_button():
    button_style = """
        <style>
        .custom-button {
            display: inline-block;
            padding: 0.5em 1em;
            font-size: 1em;
            font-weight: bold;
            color: #ffffff;
            background-color: #4CAF50;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
        </style>
    """
    button_html = """
        <a href="#" class="custom-button" id="custom-button">Custom Button</a>
    """
    
    # Injecter le CSS et HTML
    st.markdown(button_style, unsafe_allow_html=True)
    st.markdown(button_html, unsafe_allow_html=True)

    # Détecter le clic du bouton
    if st.session_state.get("button_clicked", False):
        st.session_state.button_clicked = False
        return True
    else:
        return False

# Appeler la fonction pour afficher le bouton personnalisé
button_clicked = custom_button()

# Ajouter un script JavaScript pour détecter le clic et mettre à jour l'état de session
st.markdown("""
    <script>
    document.getElementById("custom-button").onclick = function() {
        // Utiliser la fonction Streamlit pour mettre à jour l'état de session
        window.parent.postMessage({isStreamlit: true, data: {type: 'button_clicked'}}, '*');
    };
    </script>
    """, unsafe_allow_html=True)

# Ajouter un écouteur pour les messages
st.markdown("""
    <script>
    window.addEventListener("message", (event) => {
        if (event.data && event.data.type === 'button_clicked') {
            // Mettre à jour l'état de session pour indiquer que le bouton a été cliqué
            window.parent.postMessage({isStreamlit: true, data: {type: 'update_session_state', state: {button_clicked: true}}}, '*');
        }
    });
    </script>
    """, unsafe_allow_html=True)

# Gérer l'événement côté Python
st.markdown(f"position bouton save: {st.session_state['click']}")

if button_clicked:
    st.session_state['click'] = True
    st.write("Bouton personnalisé cliqué !")
