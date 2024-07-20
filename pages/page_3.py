import streamlit as st

# Ajouter du CSS pour styliser le bouton
st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)

# Créer le bouton personnalisé
button_clicked = st.markdown(
    """
    <a href="javascript:void(0)" class="custom-button" id="custom-button">Custom Button</a>
    """,
    unsafe_allow_html=True
)

# Ajouter un script JavaScript pour gérer le clic du bouton
st.markdown(
    """
    <script>
    const button = document.getElementById('custom-button');
    button.addEventListener('click', function() {
        // Utiliser Streamlit pour déclencher une interaction
        window.parent.postMessage({isStreamlit: true, data: {type: 'customButtonClicked'}}, '*');
    });
    </script>
    """,
    unsafe_allow_html=True
)

# Écouter les messages et mettre à jour l'état de session
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

st.markdown(
    """
    <script>
    window.addEventListener("message", (event) => {
        if (event.data && event.data.type === 'customButtonClicked') {
            // Mettre à jour l'état de session de Streamlit
            const streamlitDoc = window.parent.document;
            const streamlitInput = streamlitDoc.querySelectorAll('input[name="custom-button-clicked"]')[0];
            streamlitInput.click();
        }
    });
    </script>
    """,
    unsafe_allow_html=True
)

# Ajouter un champ d'entrée caché pour détecter le clic
if st.button("hidden_button", key="custom-button-clicked"):
    st.session_state.button_clicked = True

# Afficher un message si le bouton personnalisé a été cliqué
if st.session_state.button_clicked:
    st.write("Bouton personnalisé cliqué !")
