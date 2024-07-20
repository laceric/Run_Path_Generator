import streamlit

# Utilisation de st.markdown pour intégrer du HTML et du CSS
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
    """, unsafe_allow_html=True
)

# Fonction JavaScript pour gérer le clic du bouton
custom_button = st.markdown(
    """
    <a href="#" class="custom-button" id="custom-button">Custom Button</a>
    """, unsafe_allow_html=True
)

# Utiliser le script pour détecter le clic du bouton
st.markdown(
    """
    <script>
    document.getElementById('custom-button').onclick = function() {
        var parent = window.parent;
        parent.postMessage("customButtonClicked", "*");
    };
    </script>
    """, unsafe_allow_html=True
)

# Écouter les messages depuis le front-end
st.markdown(
    """
    <script>
    window.addEventListener("message", (event) => {
        if (event.data === "customButtonClicked") {
            console.log("Bouton personnalisé cliqué");
            const streamlitEvent = new CustomEvent("streamlitCustomButtonClicked");
            window.dispatchEvent(streamlitEvent);
        }
    });
    </script>
    """, unsafe_allow_html=True
)

# Gérer l'événement côté Python
custom_button_clicked = st.experimental_get_query_params().get("customButtonClicked", False)
if custom_button_clicked:
    st.write("Bouton personnalisé cliqué !")
